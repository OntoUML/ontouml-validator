""" Main module for validating OntoUML Graphs.

This module serves as the main component for validating OntoUML Graphs, providing functions to verify and assess
the correctness of OntoUML models. The module handles input validation, model loading, and execution flow control,
supporting multiple execution modes.
"""

import time

import json2graph.library

import modules.arguments as args
from modules.utils_graph import load_graph_safely
from validator.modules.globals import METADATA
from validator.modules.logger import initialize_logger
from validator.modules.utils_general import get_date_time
from validator.modules.utils_validations import validate_input_extension, validate_execution_mode


def validate_ontouml_model(input_path: str,
                           silent: bool = True,
                           assumption: str = "owa",
                           execution_mode: str = "import") -> tuple[list[str], list[str]]:
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

    :return: Tuple containing two lists, both potentially containing codes OntoUML rules' codes. The lists are:
            [0] codes of rules that the model do not comply with and that generated an ERROR.
            [1] codes of rules that the model do not comply with and that generated a WARNING.
    :rtype: tuple[list[str],list[str]]
    """

    logger = initialize_logger(execution_mode)

    # Validating input file extension and parameter execution_mode
    validate_input_extension(args.ARGUMENTS['input_path'])
    validate_execution_mode(execution_mode)

    # Initializing arguments if not initialized yet (in the cases when execution mode is 'import' or 'test')
    if execution_mode != "script":
        args.initialize_arguments(input_path=input_path,
                                  silent=silent,
                                  assumption=assumption,
                                  execution_mode=execution_mode)

    # From now on the ARGUMENTS is initialized and only the dictionary is used (not the received parameters)

    if execution_mode == "script" and not args.ARGUMENTS["silent"]:
        # Initial time information
        time_screen_format = "%d-%m-%Y %H:%M:%S"
        start_date_time = get_date_time(time_screen_format)
        st = time.perf_counter()

        logger.info(f"{METADATA['name']} v{METADATA['version']} started on {start_date_time}!")
        logger.debug(f"Selected arguments are: {args.ARGUMENTS}")
        logger.info(f"Starting the validation of the file {args.ARGUMENTS['input_path']} "
                    f"considering {args.ARGUMENTS['assumption']}.\n")

    # Loading model to be validated
    if args.ARGUMENTS['input_extension'] == "json":
        model_graph = json2graph.library.decode_json_model(args.ARGUMENTS['input_path'])
    else:
        model_graph = load_graph_safely(ontology_file=args.ARGUMENTS['input_path'],
                                        format=args.ARGUMENTS['input_extension'])

    list_errors, list_warnings = run_validation(model_graph)

    if execution_mode == "script" and not args.ARGUMENTS["silent"]:
        # Get software's execution conclusion time
        end_date_time = get_date_time(time_screen_format)
        et = time.perf_counter()
        elapsed_time = round((et - st), 3)
        logger.info(f"Validation concluded on {end_date_time}. Total execution time: {elapsed_time} seconds.")

    return list_errors, list_warnings


if __name__ == '__main__':
    """ This block of code is executed when the module is run as a script. It initializes arguments for script 
    execution and calls the validate_ontouml_model function in script mode.
    """

    args.initialize_arguments(execution_mode="script")
    list_problems = validate_ontouml_model(execution_mode="script")
