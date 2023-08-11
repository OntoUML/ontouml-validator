""" Main module for validating OntoUML Graphs. """
import inspect

from modules.arguments import treat_user_arguments
from validator.modules.errors import report_error_invalid_parameter


def validate_ontouml_model(execution_mode: str) -> tuple[list[str], bool]:

    # Validating parameter execution_mode
    valid_execution_modes = ["script", "import", "test"]
    if execution_mode not in valid_execution_modes:
        current_function = inspect.stack()[0][3]
        report_error_invalid_parameter(execution_mode, valid_execution_modes, current_function)

    # Load model from json
    # load model from graph

    # perform validation

    # results on screen
    # results on screen

    return_bool = True
    return_list = ["a","b"]

    return return_bool, return_list


if __name__ == '__main__':
    treat_user_arguments()
    validate_ontouml_model(execution_mode="script")
