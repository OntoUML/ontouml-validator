"""OntoUML Validation Rules: Group CL.

This module provides a collection of functions for executing OntoUML validations for rules of the group CL.
"""
from rdflib import Graph

from validator.validations.result_issue import ResultIssue
from validator.validations.rules_cl.sparql_cl import (
    QUERY_R_CL_XJZ,
    QUERY_R_CL_JOJ,
    QUERY_R_CL_UMC,
    QUERY_R_CL_AIB,
    QUERY_R_CL_EDA,
    QUERY_R_CL_GJU,
    QUERY_R_CL_BWZ,
    QUERY_R_CL_YOK,
)
from validator.vocab_lib.globals import (
    ONTOUML_NAMESPACE,
    ONTOUML_CLASS_STEREOTYPES,
    ONTOUML_BASE_SORTALS,
    ONTOUML_ULTIMATE_SORTALS,
)
from validator.vocab_lib.vocab_lib import (
    get_classes_of_types,
    get_class_name,
    get_all_superclasses,
)


def execute_rule_R_CL_XJZ(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_XJZ and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_R_CL_XJZ)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value

        issue_description = f"The class '{class_name}' is an enumeration and has attribute(s)."
        issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
        rule_e_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_R_CL_JOJ(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_JOJ and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_R_CL_JOJ)

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


def execute_rule_R_CL_UMC(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_UMC and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_R_CL_UMC)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value
        class_lt = row.num_lt.value

        if class_lt < 2:
            issue_description = f"The enumeration class '{class_name}' has less than two literals."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
            rule_w_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_R_CL_AIB(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_AIB and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_R_CL_AIB)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.value

        issue_description = f"The enumeration class '{class_name}' has a specialization relation."
        issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
        rule_e_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_R_CL_EDA(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_EDA and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_R_CL_EDA)

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


def execute_rule_R_CL_ZGT(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_ZGT and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = (
        "Every class decorated with a base sortal stereotype must specialize a unique class decorated "
        "with a ultimate sortal stereotype."
    )

    rule_w_list = []
    rule_e_list = []

    # Creating a list of all base_sortals and of all ultimate_sortals in the ontology
    base_sortals = get_classes_of_types(ontouml_model, ONTOUML_BASE_SORTALS)
    ultimate_sortals = get_classes_of_types(ontouml_model, ONTOUML_ULTIMATE_SORTALS)

    for base_sortal in base_sortals:
        base_sortal_sup = get_all_superclasses(ontouml_model, base_sortal)
        sup_count = 0

        for sup in base_sortal_sup:
            if sup in ultimate_sortals:
                sup_count += 1

        if sup_count == 0:
            class_name = get_class_name(ontouml_model, base_sortal)
            issue_description = f"The class '{class_name}' is a base sortal without an ultimate sortal as supertype."
            issue = ResultIssue(rule_code, rule_definition, issue_description, [base_sortal])
            rule_w_list.append(issue)
        elif sup_count > 1:
            class_name = get_class_name(ontouml_model, base_sortal)
            issue_description = (
                f"The class '{class_name}' is a base sortal with {sup_count} ultimate sortals supertypes."
            )
            issue = ResultIssue(rule_code, rule_definition, issue_description, [base_sortal])
            rule_e_list.append(issue)

    return rule_w_list, rule_e_list


def execute_rule_R_CL_GJU(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_GJU and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_R_CL_GJU)

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


def execute_rule_R_CL_BWZ(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_BWZ and return its description and results.

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
    query_answer = ontouml_model.query(QUERY_R_CL_BWZ)

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


def execute_rule_R_CL_YOK(ontouml_model: Graph, rule_code: str) -> tuple[list[ResultIssue], list[ResultIssue]]:
    """Execute rule R_CL_YOK and return its description and results.

    :param ontouml_model: The OntoUML model in graph format (using the ontouml-vocabulary) to be validated by the rule.
    :type ontouml_model: Graph
    :param rule_code: Code of this rule.
    :type rule_code: str
    :return: A tuple with two components:
        - A list of all warnings (as a ResultIssue object) found during the specific rule's validation process.
        - A list of all errors (as a ResultIssue object) found during the specific rule's validation process.
    :rtype: tuple[list[ResultIssue], list[ResultIssue]]
    """
    rule_definition = "Every class decorated with a non-sortal stereotype must be abstract."

    rule_w_list = []
    rule_e_list = []

    # Returns every non-sortal class that has its attribute isAbstract set to false
    query_answer = ontouml_model.query(QUERY_R_CL_YOK)

    for row in query_answer:
        class_id = row.class_id.toPython()
        class_name = row.class_name.toPython()
        class_st = row.class_st.toPython()

        issue_description = (
            f"The non-sortal ('{class_st}') class '{class_name}' " f"has isAbstract attribute set to 'false'."
        )
        issue = ResultIssue(rule_code, rule_definition, issue_description, [class_id])
        rule_e_list.append(issue)

    return rule_w_list, rule_e_list
