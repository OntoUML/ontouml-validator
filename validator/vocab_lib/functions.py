"""Library for manipulating ontouml-vocabulary."""
from rdflib import Graph, URIRef, RDF

from validator.vocab_lib.ontouml import ONTOUML, ONTOUML_NAMESPACE


def get_direct_superclasses(ontouml_model: Graph, ontouml_class: str, type_restr_list: list[str] = []) -> list[str]:
    """Retrieve direct superclasses of a specified OntoUML class from a given OntoUML RDF graph.

    Allows the user to specify a list of restricted types.
    Superclasses of those types will not be included in the returned list.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve superclasses.
    :type ontouml_class: str
    :param type_restr_list: A list of OntoUML stereotype URIs for type restriction. If provided, only superclasses
                            with matching stereotypes will be included. Defaults to an empty list.
    :type type_restr_list: list[str]
    :return: A list of URIs representing the direct superclasses of the specified OntoUML class.
    :rtype: list[str]
    """
    onto_class = URIRef(ontouml_class)
    superclasses = []
    specific = URIRef(ONTOUML.specific)
    general = URIRef(ONTOUML.general)

    for gen in ontouml_model.subjects(specific, onto_class):
        for superclass in ontouml_model.objects(gen, general):
            # Case restriction list: add to list of superclasses only if type fits
            if type_restr_list:
                superclass_st = get_class_stereotype(ontouml_model, superclass.toPython())
                if superclass_st not in type_restr_list:
                    superclasses.append(superclass.toPython())
            # Case there is no type to be restricted
            else:
                superclasses.append(superclass.toPython())

    return superclasses


def get_direct_subclasses(ontouml_model: Graph, ontouml_class: str, type_restr_list: list[str] = []) -> list[str]:
    """Retrieve direct subclasses of a specified OntoUML class from a given OntoUML RDF graph.

    Allows the user to specify a list of restricted types.
    subclasses of those types will not be included in the returned list.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve subclasses.
    :type ontouml_class: str
    :param type_restr_list: A list of OntoUML stereotype URIs for type restriction. If provided, only subclasses
                            with matching stereotypes will be included. Defaults to an empty list.
    :type type_restr_list: list[str]
    :return: A list of URIs representing the direct subclasses of the specified OntoUML class.
    :rtype: list[str]
    """
    onto_class = URIRef(ontouml_class)
    subclasses = []
    specific = URIRef(ONTOUML.specific)
    general = URIRef(ONTOUML.general)

    for gen in ontouml_model.subjects(general, onto_class):
        for subclass in ontouml_model.objects(gen, specific):
            # Case restriction list: add to list of subclasses only if type fits
            if type_restr_list:
                subclass_st = get_class_stereotype(ontouml_model, subclass.toPython())
                if subclass_st not in type_restr_list:
                    subclasses.append(subclass.toPython())
            # Case there is no type to be restricted
            else:
                subclasses.append(subclass.toPython())

    return subclasses


def get_all_superclasses(ontouml_model: Graph, ontouml_class: str) -> list[str]:
    """Retrieve all (direct and indirect) superclasses of a specified OntoUML class from a given OntoUML RDF graph.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve superclasses.
    :type ontouml_class: str
    :return: A list of URIs representing the direct superclasses of the specified OntoUML class.
    :rtype: list[str]
    """
    direct_super = get_direct_superclasses(ontouml_model, ontouml_class)
    all_superclasses = []
    all_superclasses.extend(direct_super)

    for superclass in direct_super:
        sub_direct = get_direct_superclasses(ontouml_model, superclass)
        all_superclasses.extend(sub_direct)

    return all_superclasses


def get_all_subclasses(ontouml_model: Graph, ontouml_class: str) -> list[str]:
    """Retrieve all (direct and indirect) subclasses of a specified OntoUML class from a given OntoUML RDF graph.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve subclasses.
    :type ontouml_class: str
    :return: A list of URIs representing the direct subclasses of the specified OntoUML class.
    :rtype: list[str]
    """
    direct_sub = get_direct_subclasses(ontouml_model, ontouml_class)
    all_subclasses = []
    all_subclasses.extend(direct_sub)

    for subclass in direct_sub:
        sub_direct = get_direct_subclasses(ontouml_model, subclass)
        all_subclasses.extend(sub_direct)

    return all_subclasses


def get_all_classes(ontouml_model: Graph) -> list[str]:
    """Retrieve all OntoUML classes from a given OntoUML RDF graph.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :return: A list of URIs representing OntoUML classes.
    :rtype: list[str]
    """
    list_classes = []

    for model_class in ontouml_model.subjects(RDF.type, ONTOUML.Class):
        list_classes.append(model_class)

    return list_classes


def get_classes_of_types(ontouml_model: Graph, type_restr_list: list[str]) -> list[str]:
    """Retrieve OntoUML classes that match a list of stereotype URIs from a given OntoUML RDF graph.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :param type_restr_list: A list of OntoUML stereotype URIs for filtering classes.
    :type type_restr_list: list[str]
    :return: A list of URIs representing OntoUML classes that match the provided stereotype URIs.
    :rtype: list[str]
    """
    list_classes = []

    for onto_class in ontouml_model.subjects(RDF.type, ONTOUML.Class):
        for type_restr in type_restr_list:
            uri_type_restr = URIRef(type_restr)
            if uri_type_restr in ontouml_model.objects(onto_class, ONTOUML.stereotype):
                list_classes.append(onto_class.toPython())

    return list_classes


def get_class_name(ontouml_model: Graph, ontouml_class: str) -> str:
    """
    Retrieve the name of a specified OntoUML class from a given OntoUML RDF graph.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve the name.
    :type ontouml_class: str
    :return: The name of the specified OntoUML class.
    :rtype: str
    """
    uri_class_name = ontouml_model.value(URIRef(ontouml_class), ONTOUML.name)
    class_name = uri_class_name.toPython()

    return class_name


def get_class_stereotype(ontouml_model: Graph, ontouml_class: str) -> str | None:
    """Retrieve the stereotype (if any) of a specified OntoUML class from a given OntoUML RDF graph.

    :param ontouml_model: The RDF graph containing OntoUML model data.
    :type ontouml_model: rdflib.Graph
    :param ontouml_class: The URI of the OntoUML class for which to retrieve the stereotype.
    :type ontouml_class: str
    :return: The stereotype of the specified OntoUML class, or None if not found.
    :rtype: str | None
    """
    try:
        uri_class_st = ontouml_model.value(ONTOUML.Class, ONTOUML.stereotype)
        class_stereotype = uri_class_st.toPython()
    except AttributeError:
        class_stereotype = None

    return class_stereotype


def get_ontouml_term(term_name: str) -> (URIRef, str):
    """
    Retrieve the URIRef and string representation for a specified term.

    This method provides a convenient way to access both the URIRef and the string representation of a term in
    the OntoUML vocabulary.

    Example:
        # Access the URIRef and string representation for 'abstract'
        abstract_uri, abstract_str = ONTOUML.get_term('abstract')

    :param term_name: The name of the term for which to retrieve information.
    :type term_name: str
    :return: A tuple containing the URIRef representing the term and its string representation.
    :rtype: (URIRef,str)

    """
    str_term = ONTOUML_NAMESPACE + term_name
    uri_term = URIRef(term_name)

    return uri_term, str_term


def get_ontouml_uri(term_name: str) -> URIRef:
    """
    Retrieve the URIRef for a specified OntoUML term.

    This function provides a convenient way to access the URIRef representation of a term in the OntoUML vocabulary.

    Example:
        # Access the URIRef for 'abstract'
        abstract_uri = get_ontouml_uri('abstract')

    :param term_name: The name of the term for which to retrieve the URIRef.
    :type term_name: str
    :return: The URIRef representing the term.
    :rtype: URIRef
    """
    uri_term, _ = get_ontouml_term(term_name)
    return uri_term


def get_ontouml_str(term_name: str) -> str:
    """
    Retrieve the string representation for a specified OntoUML term.

    This function provides a convenient way to access the string representation of a term in the OntoUML vocabulary.

    Example:
        # Access the string representation for 'abstract'
        abstract_str = get_ontouml_str('abstract')

    :param term_name: The name of the term for which to retrieve the string representation.
    :type term_name: str
    :return: The string representation of the term.
    :rtype: str
    """
    _, str_term = get_ontouml_term(term_name)
    return str_term
