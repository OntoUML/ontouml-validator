"""OntoUML Rule Execution Module.

This module provides a collection of functions for executing various OntoUML validation rules.
It is designed to validate OntoUML models loaded as RDF graphs using a set of predefined rules.
The module currently contains implementations for multiple rules. Additional rules can be easily added in the future.
"""

from rdflib import Graph

from validator.validations.constants import ONTOUML_CLASS_STEREOTYPES, ONTOUML_NAMESPACE
from validator.validations.result_issue import ResultIssue
from validator.validations.sparql_queries import QUERY_CL_ST_01, QUERY_CL_ST_02, QUERY_CL_EN_01, QUERY_CL_EN_02


def execute_rule_CL_ST_01(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_ST_01 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Every class must be decorated with exactly one stereotype."

    rule_w_list = []
    rule_e_list = []

    # Returns every class and the amount of stereotypes they have
    query_answer = ontouml_model.query(QUERY_CL_ST_01)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value
        class_sts = row.num_sts.value

        if class_sts == 0:
            issue_description = f"The class '{class_name}' has no stereotype."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_w_list.append(issue)
        elif class_sts > 1:
            issue_description = f"The class '{class_name}' has more than one stereotype."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_e_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_CL_ST_02(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule CL_ST_02 and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Every class must be decorated with stereotypes of the OntoUML profile."

    rule_w_list = []
    rule_e_list = []

    # Returns every class and their respective stereotype
    query_answer = ontouml_model.query(QUERY_CL_ST_02)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value

        if row.class_st is None:
            issue_description = f"The class '{class_name}' has no stereotype."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_w_list.append(issue)
        else:
            class_st = row.class_st.toPython()
            if class_st not in ONTOUML_CLASS_STEREOTYPES:
                issue_description = (
                    f"The class '{class_name}' has stereotype '{class_st}', which is not part of the OntoUML profile."
                )
                issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
                rule_e_list.append(issue)

    return rule_w_list, rule_e_list


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
