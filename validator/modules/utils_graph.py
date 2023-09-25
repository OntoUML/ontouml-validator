"""Util functions related to graphs."""
from loguru import logger
from rdflib import Graph

from .errors import report_error_io_read
from .utils_validations import validate_input_extension


def load_graph_safely(ontology_file: str, file_format: str = "not_provided") -> Graph:
    """Safely load graph from file to working memory using arguments provided by the user, which are the file path \
    and (optionally) the file type.

    :param ontology_file: Path to the ontology file to be loaded into the working memory.
    :type ontology_file: str
    :param file_format: Optional argument. Format of the file to be loaded.
    :type file_format: str
    :return: RDFLib graph loaded as object.
    :rtype: Graph
    """
    ontology_graph = Graph()

    print(f"{ontology_file = }")

    try:
        if file_format == "not_provided":
            ontology_graph.parse(ontology_file, encoding="utf-8")
        else:
            file_format = file_format.lower().strip()
            validate_input_extension(file_format)
            ontology_graph.parse(ontology_file, encoding="utf-8", format=file_format)
    except OSError as error:
        file_description = "input ontology file"
        report_error_io_read(ontology_file, file_description, error)

    logger.debug(f"Ontology file {ontology_file} successfully loaded to working memory.")

    return ontology_graph
