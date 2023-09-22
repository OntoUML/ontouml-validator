""" Main module for validating OntoUML Graphs.

This module serves as the main component for validating OntoUML Graphs, providing functions to verify and assess
the correctness of OntoUML models. The module handles input validation, model loading, and execution flow control,
supporting multiple execution modes.
"""
from validator.library import validate_ontouml_model

if __name__ == "__main__":
    """This block of code is executed when the module is run as a script. It initializes arguments for script
    execution and calls the validate_ontouml_model function in script mode.
    """

    validate_ontouml_model()
