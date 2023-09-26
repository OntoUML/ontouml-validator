"""OntoUML Validation Rules - Group CL_EN.

This module provides a collection of functions for executing OntoUML validations for rules of the group CL_EN.
"""

from rdflib import Graph

from validator.validations.cl_en.sparql_cl_en import (
    QUERY_CL_EN_01,
    QUERY_CL_EN_02,
    QUERY_CL_EN_03,
    QUERY_CL_EN_04,
    QUERY_CL_EN_05,
)
from validator.validations.constants import ONTOUML_NAMESPACE
from validator.validations.result_issue import ResultIssue


def execute_rule_CL_EN_01(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_EN_01 and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_CL_EN_01)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value

        issue_description = f"The class '{class_name}' is an enumeration and has attribute(s)."
        issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
        rule_e_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_CL_EN_02(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_EN_02 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Every class having enumeration literals must be decorated with the stereotype enumeration."

    rule_w_list = []
    rule_e_list = []

    # Return classes that have literals
    query_answer = ontouml_model.query(QUERY_CL_EN_02)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value

        # Class without stereotype but with enumeration literals
        if row.class_st is None:
            issue_description = (
                f"The class '{class_name}' without stereotype has an enumeration literal and, hence, "
                f"must be stereotyped as enumerator."
            )
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_w_list.append(issue)
        # Class with stereotype different from enumeration and with enumeration literals
        else:
            class_st = row.class_st.toPython()
            if class_st != (ONTOUML_NAMESPACE + "enumeration"):
                issue_description = (
                    f"The class '{class_name}' is stereotyped as '{class_st}' but has enumeration literal(s)."
                )
                issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
                rule_e_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_CL_EN_03(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_EN_03 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Every enumeration class must have at least two literals."

    rule_w_list = []
    rule_e_list = []

    # Return classes and their respective number of literals
    query_answer = ontouml_model.query(QUERY_CL_EN_03)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value
        class_lt = row.num_lt.value

        if class_lt < 2:
            issue_description = f"The enumeration class '{class_name}' has less than two literals."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_w_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_CL_EN_04(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_EN_04 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Enumeration classes cannot be specialized by other classes."

    rule_w_list = []
    rule_e_list = []

    # Return classes and their respective number of literals
    query_answer = ontouml_model.query(QUERY_CL_EN_04)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value

        issue_description = f"The enumeration class '{class_name}' has a specialization relation."
        issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
        rule_e_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_CL_EN_05(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_EN_05 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Enumeration classes can only be generalized by classes with stereotype Abstract."

    rule_w_list = []
    rule_e_list = []

    # Return classes and their respective number of literals
    query_answer = ontouml_model.query(QUERY_CL_EN_05)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value

        if row.sup_st is None:
            issue_description = f"The enumeration class '{class_name}' has a generalization class without stereotype."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_w_list.append(issue)
        else:
            issue_description = (
                f"The enumeration class '{class_name}' has a generalization class with stereotype "
                f"different from 'Abstract'."
            )
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_e_list.append(issue)

    return rule_w_list, rule_e_list
