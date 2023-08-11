""" Main module for validating OntoUML Graphs.

This module serves as the main component for validating OntoUML Graphs, providing functions to verify and assess
the correctness of OntoUML models. The module handles input validation, model loading, and execution flow control,
supporting multiple execution modes.
"""

import inspect

import json2graph.library

import modules.arguments as args
from modules.errors import report_error_invalid_parameter, report_error_requirement_not_met
from modules.utils_graph import load_graph_safely


def validate_input_extension(input_extension: str):
    """ Validate the input file format for RDFLib-compatible graph or JSON serialization.

    This function validates the file extension of the input OntoUML model to ensure it is compatible with supported
    formats. It checks against a predefined list of RDFLib's allowed graph and JSON formats and raises an error if the
    provided input extension is invalid.

    :param input_extension: Path to the input file to be validated.
    :type input_extension: str
    """
    # Formats for saving graphs supported by RDFLib
    # https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html#saving-rdf
    allowed_graph_formats = ["turtle", "ttl", "turtle2", "xml", "pretty-xml", "json-ld", "ntriples", "nt", "nt11", "n3",
                             "trig", "trix", "nquads"]

    # Checking if provided input file type is valid
    if (input_extension != "json") and (input_extension not in allowed_graph_formats):
        report_error_requirement_not_met("Provided input file must be of a valid type. Execution finished.")


def validate_ontouml_model(input_path: str,
                           silent: bool = True,
                           assumption: str = "owa",
                           execution_mode: str = "import") -> list[str]:
    """ This function performs validation of an OntoUML model. It validates the input parameters, initializes arguments
    based on the execution mode, loads the model graph, and runs the validation process. The function returns a list of
    problems identified in the validated model.

    This function ensures that the OntoUML model is properly loaded, validated, and any issues are reported for
    further analysis.

    :param input_path: Path to the input file to be validated.
    :type input_path: str
    :param silent: If True, suppresses intermediate communications and log messages during execution. (Optional)
    :type silent: bool
    :param assumption: World assumption to be considered during the validation execution. (Optional)
                       Valid values are 'owa' (default) and 'cwa'.
    :type assumption: str
    :param execution_mode: Information about the execution mode. (Optional)
                           Valid values are 'import' (default), 'script', and 'test'.
    :type execution_mode: str

    :return: List of strings representing all validations in which the model failed.
             I.e., it is list of problems the validated model has.
    :rtype: list[str]
    """

    # Validating input file extension and parameter execution_mode
    validate_input_extension(args.ARGUMENTS['input_path'])
    valid_execution_modes = ["script", "import", "test"]
    if execution_mode not in valid_execution_modes:
        current_function = inspect.stack()[0][3]
        report_error_invalid_parameter(execution_mode, valid_execution_modes, current_function)

    # Initializing arguments if not initialized yet (in the cases when execution mode is 'import' or 'test')
    if execution_mode != "script":
        args.initialize_arguments(input_path=input_path,
                                  silent=silent,
                                  assumption=assumption,
                                  execution_mode=execution_mode)

    # From now on the ARGUMENTS is initialized and only the dictionary is used (not the received parameters)

    # Loading model to be validated
    if args.ARGUMENTS['input_extension'] == "json":
        model_graph = json2graph.library.decode_json_model(args.ARGUMENTS['input_path'])
    else:
        model_graph = load_graph_safely(ontology_file=args.ARGUMENTS['input_path'],
                                        format=args.ARGUMENTS['input_extension'])

    list_problems = run_validation(model_graph)

    return list_problems


if __name__ == '__main__':
    """ This block of code is executed when the module is run as a script. It initializes arguments for script 
    execution and calls the validate_ontouml_model function in script mode.
    """

    args.initialize_arguments(execution_mode="script")
    validate_ontouml_model(execution_mode="script")
