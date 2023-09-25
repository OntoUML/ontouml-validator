""" This script is used to perform tests on the ontouml-validator using pytest.

A list of tests is read from the file tests_list.csv and each test is individually performed.
"""
import csv
import inspect
import os

import pytest
from icecream import ic

from validator.modules.errors import report_error_end_of_switch
from validator.modules.utils_graph import load_graph_safely
from validator.validations.rules_general import execute_rule_switch

# Guarantees that the file will be found as it searches using this file as basis
package_dir = os.path.dirname(os.path.dirname(__file__))
test_files_dir = "tests" + os.path.sep + "test_files" + os.path.sep
file_path = os.path.join(package_dir, test_files_dir, "tests_list.csv")


def get_test_list() -> list[tuple[str, str, str]]:
    """Loads information about test test_files from csv and creates a list of tuples with tests' information.
    Note: the input file does not have a header.

    :return: The returned tuples' content is:
                [0] (str) world-assumption to be used in the test. Valid values are "cwa" and "owa".
                [1] (str) input file name: name of the input file to be tested.
                [2] (str) expected result: indicates if the result is expected to be:
                    - 'valid': valid
                    - 'warning': invalid and generate a warning
                    - 'error': invalid and generate an error
    :rtype: list[tuple[str,str,str]]
    """

    # Read file with all tests information to generate fixture
    with open(file_path, mode="r") as csv_file:
        tests_information = []
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            single_test = tuple(row.values())
            tests_information.append(single_test)

    return tests_information


# Execute list generation
LIST_OF_TESTS = get_test_list()
ic(LIST_OF_TESTS)


@pytest.mark.parametrize("assumption, rule_code, input_file, expected_result", LIST_OF_TESTS)
def test_all(assumption: str, rule_code: str, input_file: str, expected_result: int):
    """Executes the validator in a received input file and checks if the execution result matches the expected value.

    :param assumption: Indicates the world-assumption to be used in test execution. Valid values are: 'cwa' and 'owa'.
    :type assumption: str
    :param rule_code: The code of the validation rule to be tested.
    :type rule_code: str
    :param input_file: Path to an input file that is going to be validated as a test.
    :type input_file: str
    :param expected_result: Indicates the test's expected result, which can be one of the following:
        - 'valid': The evaluation result is expected to be valid.
        - 'warning': The evaluation result is expected to generate a warning.
        - 'error': The evaluation result is expected to generate an error.
    :type expected_result: int
    """

    # Load test file
    input_file_path = os.path.join(package_dir, test_files_dir, input_file)
    ontouml_model = load_graph_safely(input_file_path, "ttl")

    # Execute and get results
    rule_w_list, rule_e_list = execute_rule_switch(ontouml_model, rule_code)

    # In CWA, all warnings are errors
    if assumption == "cwa":
        rule_e_list.extend(rule_w_list)
        rule_w_list.clear()

    # Generate boolean result according to execution
    is_valid = True if (not (rule_w_list) and not (rule_e_list)) else False
    is_warning = True if (rule_w_list and not (rule_e_list)) else False
    is_error = True if rule_e_list else False

    # Creating fail message to be used if necessary
    if is_valid:
        result = "valid"
    elif is_warning:
        result = "warning"
    elif is_error:
        result = "error"
    else:
        current_function = inspect.stack()[0][3]
        report_error_end_of_switch("result", current_function)

    test_fail_message = f"Expected {expected_result}, got {result}."

    # Assertions
    if expected_result == "valid":
        assert is_valid, test_fail_message
    elif expected_result == "warning":
        assert is_warning, test_fail_message
    elif expected_result == "error":
        assert is_error, test_fail_message
    else:
        current_function = inspect.stack()[0][3]
        report_error_end_of_switch("is_valid", current_function)
