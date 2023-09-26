"""Main module for validating OntoUML Graphs.

This module serves as the main component for validating OntoUML Graphs, providing functions to verify and assess
the correctness of OntoUML models. The module handles input validation, model loading, and execution flow control,
supporting multiple execution modes.
"""
import sys

from loguru import logger

from validator.lib import validate_ontouml_file

if __name__ == "__main__":
    """This block of code is executed when the module is run as a script. It initializes arguments for script
    execution and calls the validate_ontouml_model function in script mode.
    """

    logger.configure(handlers=[{"sink": sys.stderr, "level": "DEBUG"}])

    ontouml_file = "./validator/tests/test_files/CL_ST_01F.ttl"
    validate_ontouml_file(ontouml_file, "owa")
