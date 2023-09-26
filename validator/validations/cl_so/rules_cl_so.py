"""OntoUML Validation Rules - Group CL_SO.

This module provides a collection of functions for executing OntoUML validations for rules of the group CL_SO.
"""
from rdflib import Graph

from validator.validations.cl_so.sparql_cl_so import QUERY_CL_SO_01
from validator.validations.result_issue import ResultIssue


def execute_rule_CL_SO_01(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_SO_01 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Every class decorated with the stereotype 'enumeration' must not have attributes."

    rule_w_list = []
    rule_e_list = []

    # Return enumeration classes that have attributes
    query_answer = ontouml_model.query(QUERY_CL_SO_01)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value
        sup_count = row.count.value

        if sup_count == 0:
            issue_description = f"The class '{class_name}' is a base sortal without an ultimate sortal as supertype."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_w_list.append(issue)
        elif sup_count > 1:
            issue_description = (
                f"The class '{class_name}' is a base sortal with " f"{sup_count} ultimate sortals supertypes."
            )
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_e_list.append(issue)

    return rule_w_list, rule_e_list
