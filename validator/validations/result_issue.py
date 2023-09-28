"""Define the ResultIssue class, which represents issues (warnings or errors) identified by validation rules."""


class ResultIssue:
    """A class to represent an issue (warning or error) identified by a validation rule."""

    # TODO: Check if it is really necessary to have a list of ids or if just a single id is enought
    def __init__(self, rule_code: str, rule_definition: str, issue_description: str, ids_list: list[str]):
        """Initialize a ResultIssue object.

        :param rule_code: The code of the rule that identified the issue.
        :type rule_code: str
        :param rule_definition: The textual definition of the rule that identified the issue.
        :type rule_definition: str
        :param issue_description: The textual description of the issue identified.
        :type issue_description: str
        :param ids_list: A list of IDs (URIs) of the elements affected by/related to the issue.
        :type ids_list: list[str]
        """
        self.rule_code = rule_code
        self.rule_definition = rule_definition
        self.issue_description = issue_description
        self.ids_list = ids_list
