import inspect

from icecream import ic
from loguru import logger
from rdflib import Graph

from .sparql_queries import QUERY_CL001
from ..modules.errors import report_error_end_of_switch


def execute_rule_CL001(ontouml_model: Graph) -> tuple[list[str], list[str]]:
    """Execute rule CL001 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :return: A tuple with two components:
        - A list of all warnings found during the specific rule's validation process.
        - A list of all errors found during the specific rule's validation process.
    :rtype: tuple[list[str], list[str]]
    """

    rule_description = "Every class must be decorated with exactly one stereotype."

    query_answer = ontouml_model.query(QUERY_CL001)

    for row in query_answer:
        class_name = row.class_name.value
        class_sts = row.num_sts.value
        ic(class_name, class_sts)

    rule_w_list = []
    rule_e_list = []

    return rule_description, rule_w_list, rule_e_list


def execute_rule_switch(ontouml_model: Graph, rule_code: str) -> tuple[list[str], list[str]]:
    """Select a specific validation rule function based on the given 'rule_code' to be executed on the provided \
    OntoUML model.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of the specific rule to be executed.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings found during the specific rule's validation process.
        - A list of all errors found during the specific rule's validation process.
    :rtype: tuple[list[str], list[str]]
    """
    if rule_code == "CL001":
        rule_description, rule_w_list, rule_e_list = execute_rule_CL001(ontouml_model)
    # elif rule_code == "CL002":
    #     rule_w_list, rule_e_list = execute_rule_CL002(ontouml_model)
    # elif rule_code == "CL003":
    #     rule_w_list, rule_e_list = execute_rule_CL003(ontouml_model)
    # This situation must never be reached
    else:
        current_function = inspect.stack()[0][3]
        report_error_end_of_switch("rule_code", current_function)

    if rule_w_list:
        logger.info(f"WARNING identified by rule {rule_code}: {rule_description}.")
    if rule_e_list:
        logger.info(f"ERROR identified by rule {rule_code}: {rule_description}.")

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

    validation_rules_list = ["CL001"]

    for rule_code in validation_rules_list:
        rule_w_list, rule_e_list = execute_rule_switch(ontouml_model, rule_code)
        w_list.append(rule_w_list)
        e_list.append(rule_e_list)

    return w_list, e_list
