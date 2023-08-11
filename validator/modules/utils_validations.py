import inspect

from validator.modules.errors import report_error_invalid_parameter, report_error_requirement_not_met


def validate_input_extension(input_extension: str):
    """ Validate the input file format for RDFLib-compatible graph or JSON serialization.

    This function validates the file extension of the input OntoUML model to ensure it is compatible with supported
    formats. It checks against a predefined list of RDFLib's allowed graph and JSON formats and raises an error if the
    provided input extension is invalid.

    :param input_extension: Path to the input file to be validated.
    :type input_extension: str
    """
    # Formats for saving graphs supported by RDFLib
    # https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html#saving-rdf
    allowed_graph_formats = ["turtle", "ttl", "turtle2", "xml", "pretty-xml", "json-ld", "ntriples", "nt", "nt11", "n3",
                             "trig", "trix", "nquads"]

    # Checking if provided input file type is valid
    if (input_extension != "json") and (input_extension not in allowed_graph_formats):
        report_error_requirement_not_met("Provided input file must be of a valid type. Execution finished.")


def validate_execution_mode(execution_mode):
    """ Validate the provided execution mode against a list of valid modes.

    This function validates the given execution mode against a predefined list of valid modes: ["script", "import",
    "test"]. It ensures that the provided mode is one of the accepted values, and if not, raises an error indicating
    the invalid parameter.

    :param execution_mode: The execution mode to be validated.
    :type execution_mode: str
    """
    
    valid_execution_modes = ["script", "import", "test"]
    if execution_mode not in valid_execution_modes:
        current_function = inspect.stack()[0][3]
        report_error_invalid_parameter(execution_mode, valid_execution_modes, current_function)
