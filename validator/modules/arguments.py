""" Argument Treatments Module.

This module provides functions for parsing and validating (user-provided or default) arguments when starting the
software in different execution modes (as a script, as library, or for testing). It offers capabilities for handling
command-line arguments and for initializing the global variable ARGUMENTS containing the arguments.
"""

import argparse
import inspect
import os
import pathlib

from .errors import report_error_requirement_not_met, report_error_invalid_parameter
from .globals import METADATA
from .logger import initialize_logger

ARGUMENTS = {}

LOGGER = initialize_logger()


def validate_input_file(input_path: str):
    """ Validate the input file format for RDFLib-compatible graph or JSON serialization.

    :param input_path: Path to the input file to be validated.
    :type input_path: str
    """
    # Formats for saving graphs supported by RDFLib
    # https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html#saving-rdf
    allowed_graph_formats = ["turtle", "ttl", "turtle2", "xml", "pretty-xml", "json-ld", "ntriples", "nt", "nt11", "n3",
                             "trig", "trix", "nquads"]

    file_extension = (os.path.splitext(input_path)[1])[1:]

    # Checking if provided input file type is valid
    if (file_extension != "json") and (file_extension not in allowed_graph_formats):
        report_error_requirement_not_met("Provided input file must be of a valid type. Execution finished.")


def treat_user_arguments() -> dict:
    """ This function parses the command-line arguments provided by the user and performs necessary validations.

    :return: Dictionary with arguments provided by the user or default values.
    :rtype: dict
    """

    LOGGER.debug("Parsing user's arguments...")

    about_message = METADATA["name"] + " - version " + METADATA["version"]

    # PARSING ARGUMENTS
    args_parser = argparse.ArgumentParser(prog=METADATA["name"],
                                          description=METADATA["description"] + ". Version: " + METADATA["version"],
                                          allow_abbrev=False, epilog="More information at: " + METADATA["repository"])

    args_parser.version = about_message

    # POSITIONAL ARGUMENT
    args_parser.add_argument("input_path", type=str, action="store",
                             help="The path of the graph or json input file to be validated.")

    # OPTIONAL ARGUMENT
    args_parser.add_argument("-s", "--silent", action="store_true",
                             help="Silent mode. Do not print warnings and errors on screen.")
    args_parser.add_argument("-a", "--assumption", action="store", choices=["owa", "cwa"], default="owa",
                             help="Format to save the decoded file. Default is 'ttl'.")

    # AUTOMATIC ARGUMENTS
    args_parser.add_argument("-v", "--version", action="version", help="Print the software version and exit.")

    # Execute arguments parser
    arguments = args_parser.parse_args()

    # Asserting dictionary keys
    arguments_dictionary = {"input_path": arguments.input_path,
                            "silent": arguments.silent,
                            "assumption": arguments.assumption}

    validate_input_file(arguments.input_path)

    LOGGER.debug(f"Arguments parsed. Obtained values are: {arguments_dictionary}.")

    return arguments_dictionary


def initialize_arguments(input_path: str = "not_initialized",
                         silent: bool = True,
                         assumption: str = "owa",
                         execution_mode: str = "import"):
    """ This function initializes the global variable ARGUMENTS of type dictionary, which contains user-provided
    (when executed in script mode) or default arguments (when executed as a library or for testing).
    The ARGUMENTS variable must be initialized in every possible execution mode.

    The valid execution modes are:
    - 'script': If used as a script, use user's arguments parsed from the command line.
    - 'import': When imported into external code, working as a library.
    - 'test': Used for testing.

    :param input_path: Path to the input file to be validated. (Optional)
    :type input_path: str
    :param silent: If True, suppresses intermediate communications and log messages during execution. (Optional)
    :type silent: bool
    :param assumption: World assumption to be considered during the validation execution. (Optional)
                       Valid values are 'owa' (default) and 'cwa'.
    :type assumption: str
    :param execution_mode: Information about the execution mode. (Optional)
                           Valid values are 'import' (default), 'script', and 'test'.
    :type execution_mode: str
    """

    # Validating parameter execution_mode
    valid_execution_modes = ["script", "import", "test"]
    if execution_mode not in valid_execution_modes:
        current_function = inspect.stack()[0][3]
        report_error_invalid_parameter(execution_mode, valid_execution_modes, current_function)

    global ARGUMENTS

    # Specific according to execution_mode
    if execution_mode == "script":
        ARGUMENTS = treat_user_arguments()
    else:
        ARGUMENTS["input_path"] = input_path
        ARGUMENTS["silent"] = silent
        ARGUMENTS["assumption"] = assumption
        ARGUMENTS["execution_mode"] = execution_mode

    # General: input file details
    input_path = pathlib.Path(ARGUMENTS["input_path"])
    ARGUMENTS["input_path"] = input_path.parent
    ARGUMENTS["input_name"] = input_path.stem
    ARGUMENTS["input_extension"] = input_path.suffix[1:]