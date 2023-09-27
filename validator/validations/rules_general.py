"""OntoUML Validation Utilities.

This module provides utility functions for validating input parameters and assumptions related to the OntoUML
validation process. It includes functions for validating input file extensions to ensure compatibility
with RDFLib's supported formats and for normalizing and validating world assumptions.
"""
import inspect

from rdflib import Graph

from .result_issue import ResultIssue
from .rules_cl.rules_cl import (
    execute_rule_R_CL_XJZ,
    execute_rule_R_CL_JOJ,
    execute_rule_R_CL_UMC,
    execute_rule_R_CL_AIB,
    execute_rule_R_CL_EDA,
    execute_rule_R_CL_ZGT,
    execute_rule_R_CL_GJU,
    execute_rule_R_CL_BWZ,
    execute_rule_R_CL_YOK,
)
from ..modules.errors import report_error_end_of_switch


def execute_rule_switch(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Select a specific validation rule function based on the given 'rule_code' to be executed on the provided \
    OntoUML model.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of the specific rule to be executed.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings found during the specific rule's validation process.
        - A list of all errors found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    if rule_code == "R_CL_GJU":
        rule_w_list, rule_e_list = execute_rule_R_CL_GJU(ontouml_model, rule_code)
    elif rule_code == "R_CL_BWZ":
        rule_w_list, rule_e_list = execute_rule_R_CL_BWZ(ontouml_model, rule_code)
    elif rule_code == "R_CL_XJZ":
        rule_w_list, rule_e_list = execute_rule_R_CL_XJZ(ontouml_model, rule_code)
    elif rule_code == "R_CL_JOJ":
        rule_w_list, rule_e_list = execute_rule_R_CL_JOJ(ontouml_model, rule_code)
    elif rule_code == "R_CL_UMC":
        rule_w_list, rule_e_list = execute_rule_R_CL_UMC(ontouml_model, rule_code)
    elif rule_code == "R_CL_AIB":
        rule_w_list, rule_e_list = execute_rule_R_CL_AIB(ontouml_model, rule_code)
    elif rule_code == "R_CL_EDA":
        rule_w_list, rule_e_list = execute_rule_R_CL_EDA(ontouml_model, rule_code)
    elif rule_code == "R_CL_ZGT":
        rule_w_list, rule_e_list = execute_rule_R_CL_ZGT(ontouml_model, rule_code)
    elif rule_code == "R_CL_YOK":
        rule_w_list, rule_e_list = execute_rule_R_CL_YOK(ontouml_model, rule_code)
    # This situation must never be reached
    else:
        current_function = inspect.stack()[0][3]
        report_error_end_of_switch("rule_code", current_function)

    return rule_w_list, rule_e_list


def execute_all_validation_rules(ontouml_model: Graph) -> tuple[list[str], list[str]]:
    """Execute all validation rules and collect their results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated.
    :type ontouml_model: Graph
    :return: A tuple with two components:
        - A list of all warnings found during the validation process.
        - A list of all errors found during the validation process.
    :rtype: tuple[list[str], list[str]]
    """
    # Create empty lists to be filled in by the individual rules
    w_list = []
    e_list = []

    validation_rules_list = ["R_CL_GJU"]

    for rule_code in validation_rules_list:
        rule_w_list, rule_e_list = execute_rule_switch(ontouml_model, rule_code)
        w_list.append(rule_w_list)
        e_list.append(rule_e_list)

    return w_list, e_list
