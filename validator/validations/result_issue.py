"""Define the ResultIssue class, which represents issues (warnings or errors) identified by validation rules."""


class ResultIssue:
    """A class to represent an issue (warning or error) identified by a validation rule."""

    def __init__(self, rule_code: str, description: str, ids_list: list[str]):
        """Initialize a ResultIssue object.

        :param rule_code: The code of the rule that identified the issue.
        :type rule_code: str
        :param description: The textual description of the rule that identified the issue.
        :type description: str
        :param ids_list: A list of IDs (URIs) of the elements affected by/related to the issue.
        :type ids_list: list[str]
        """
        self.rule_code = rule_code
        self.description = description
        self.ids_list = ids_list
