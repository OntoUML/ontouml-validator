"""Library for the OntoUML Validation.

This module provides a set of functions for validating OntoUML models stored in graph format using specified world
assumptions ('owa' or 'cwa'). OntoUML is a modeling language for ontology-based conceptual modeling.

These functions utilize the OntoUML vocabulary and a set of validation rules to determine the validity of the provided
models. They return a tuple with information about the validation results, including whether the model is valid,
any warnings encountered, and any errors identified.

The module also contains auxiliary functions for loading OntoUML models and handling world assumptions.

Usage:
1. Import the module: `from ontouml_validator import validate_ontouml_file, validate_ontouml_model`
2. Use the provided functions to validate OntoUML models.
"""
from loguru import logger
from rdflib import Graph

from .modules.utils_graph import load_graph_safely
from .modules.utils_validations import validate_assumption
from .validations.rules_general import execute_all_validation_rules


def validate_ontouml_file(ontouml_file_path: str, world_assumption: str) -> tuple[bool, list[str], list[str]]:
    """Validate an OntoUML model stored in a graph file using a specified world assumption ('owa' or 'cwa').

    This function takes the path to an OntoUML model stored in graph format (using the ontouml-vocabulary) and
    validates it with a specified world assumption using the validate_ontouml_model function.

    :param ontouml_file_path: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated.
    :type ontouml_file_path: str
    :param world_assumption: the world-assumption to be used during the validation. Allowed values are:'owa' and 'cwa'.
    :type world_assumption: str
    :return: A tuple with three components:
        - A boolean indicating whether the validated model is valid or not.
        - A list of warnings found during the validation process.
        - A list of errors found during the validation process.
    :rtype: tuple[bool,list[str],list[str]]
    """
    ontouml_model = load_graph_safely(ontouml_file_path)
    is_valid, w_list, e_list = validate_ontouml_model(ontouml_model, world_assumption)
    return is_valid, w_list, e_list


def validate_ontouml_model(ontouml_model: Graph, world_assumption: str) -> tuple[bool, list[str], list[str]]:
    """Validate an ontouml model loaded as a graph checking its compliance to all OntoUML rules.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated.
    :type ontouml_model: Graph
    :param world_assumption: the world-assumption to be used during the validation. Allowed values are:'owa' and 'cwa'.
    :type world_assumption: str
    :return: A tuple with three components:
        - A boolean indicating whether the validated model is valid or not.
        - A list of warnings found during the validation process.
        - A list of errors found during the validation process.
    :rtype: tuple[bool,list[str],list[str]]
    """
    # Assures that the world_assumption received as argument is valid
    assumption = validate_assumption(world_assumption)

    w_list, e_list = execute_all_validation_rules(ontouml_model)

    # In OWA, a model is considered valid if no errors were found, independently of the warnings.
    # In CWA, warnings also represent errors
    if assumption == "cwa":
        e_list.append(w_list)
        w_list = []

    logger.info(f"Final w_list: {w_list}")
    logger.info(f"Final e_list: {e_list}")

    is_valid = True if not e_list else False

    return is_valid, w_list, e_list
