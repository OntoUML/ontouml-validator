""" Main file to perform tests on the ontouml-validator.

The input file does not have a header.
"""
import csv
import os

import pytest

from validator.modules.utils_graph import load_graph_safely
from validator.validate import validate_ontouml_model


def get_test_list() -> list[tuple[str,str,str]]:
    """ Loads information about test test_files from csv and creates a list of tuples with tests' information.

    :return: The returned tuples' content is:
                [0] (str) input file name: name of the input file to be tested.
                [2] (str) world-assumption to be used in the test. Valid values are "cwa" and "owa".
                [3] (str) expected result: indicates if the result is expected to be:
                    - 'valid': valid
                    - 'warning': invalid and generate a warning
                    - 'error': invalid and generate an error
    :rtype: list[tuple[str,str,str]]
    """

    # Guarantees that the file will be found as it searches using this file as basis
    package_dir = os.path.dirname(os.path.dirname(__file__))
    test_files_dir = "tests" + os.path.sep + "test_files" + os.path.sep
    file_path = os.path.join(package_dir, test_files_dir, "tests_list.csv")

    print(f"{file_path = }")

    # Read file with all tests information to generate fixture
    with open(file_path, mode='r') as csv_file:
        tests_information = []
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            single_test = tuple(row.values())
            tests_information.append(single_test)

    return tests_information

# Execute list generation
LIST_OF_TESTS = get_test_list()


@pytest.mark.parametrize("input_file, assumption, expected_result", LIST_OF_TESTS)
def test_scior(input_file: str, assumption: str, expected_result: int):
    """ Executes Scior in a received input file and checks if the execution result matches the expected value.

    :param input_file: Path to an input file that is going to be validated as a test.
    :type input_file: str
    :param assumption: Indicates the world-assumption to be used test execution. Valid values: 'cwa' and 'owa')
    :type assumption: str
    :param expected_result: Indicates if the result is expected to be: valid ('valid'), invalid and generate a warning
                            ('warning'), or invalid and generate an error ('error').
    :type expected_result: int
    """

    package_dir = os.path.dirname(os.path.dirname(__file__))
    test_files_dir = "tests" + os.path.sep + "test_files" + os.path.sep
    file_path = os.path.join(package_dir, test_files_dir, input_file)

    errors, warnings = validate_ontouml_model(input_path=input_file, assumption=assumption, execution_mode="test")

    # check if resulting lists are empty or not
    # compare with expected result

    # assert no_error, f"EXECUTION ERROR! Error not associated with file consistency or Scior's results."
    # assert is_consistent == is_consistent, f"CONSISTENCY NOT MATCHED! Expected {exp_consist_msg}, got {got_consist_msg}."
    # assert is_correct, f"RESULT NOT MATCHED! Expected {exp_result_msg}, got {got_result_msg}."
