"""Define the ResultIssue class, which represents issues (warnings or errors) identified by validation rules."""
from validator.validations.rueles_definitions import RULES_DEFINITIONS


class ResultIssue:
    """A class to represent an issue (warning or error) identified by a validation rule."""

    def __init__(self, rule_code: str, issue_description: str, related_id: str):
        """Initialize a ResultIssue object.

        :param rule_code: The code of the rule that identified the issue.
        :type rule_code: str
        :param issue_description: The textual description of the issue identified.
        :type issue_description: str
        :param related_id: The ID (URI) of the element affected by/related to the issue.
        :type related_id: str
        """
        self.rule_code = rule_code
        self.rule_definition = RULES_DEFINITIONS[rule_code]  # noqa: F841
        self.issue_description = issue_description
        self.related_id = related_id
