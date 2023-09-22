import inspect

from validator.modules.errors import report_error_invalid_parameter, report_error_requirement_not_met


def validate_input_extension(input_extension: str):
    """Validate the input file format provided by a user for ensuring RDFLib-compatible graph.

    This function validates the file extension of the input OntoUML model to ensure it is compatible with supported
    formats. It checks against a predefined list of RDFLib's allowed graph and JSON formats and raises an error if the
    provided input extension is invalid.

    :param input_extension: Path to the input file to be validated.
    :type input_extension: str
    """
    # Formats for saving graphs supported by RDFLib
    # https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html#saving-rdf
    allowed_graph_formats = [
        "turtle",
        "ttl",
        "turtle2",
        "xml",
        "pretty-xml",
        "json-ld",
        "ntriples",
        "nt",
        "nt11",
        "n3",
        "trig",
        "trix",
        "nquads",
    ]

    # Checking if provided input file type is valid
    if (input_extension != "json") and (input_extension not in allowed_graph_formats):
        report_error_requirement_not_met("Provided input file must be of a valid type. Execution finished.")


def validate_assumption(world_assumption: str) -> str:
    """Validate and normalize a world-assumption parameter.

    This function takes a `world_assumption` parameter, converts it to lowercase, and removes leading and trailing
    whitespace. It then checks if the normalized assumption is either "owa" (Open World Assumption) or "cwa"
    (Closed World Assumption). If it is, the value is returned. If not, an error is raised by a specific function.

    :param world_assumption: The world assumption to be validated and normalized.
    :type world_assumption: str

    :return: The validated and normalized world assumption ("owa" or "cwa").
    :rtype: str
    """
    assumption = world_assumption.lower().strip()

    if (assumption != "owa") or (assumption != "cwa"):
        current_function = inspect.stack()[0][3]
        report_error_invalid_parameter("world_assumption", ["cwa", "owa"], current_function)

    return assumption
