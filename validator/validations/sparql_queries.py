"""This model contains all SPARQL queries used for validating an OntoUML Model."""

ONTOUML_PREFIX = "PREFIX ontouml: <https://w3id.org/ontouml#> "

QUERY_CL001 = (
    ONTOUML_PREFIX
    + """
SELECT ?class_id ?class_name (count(?class_st) as ?num_sts)
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    OPTIONAL {?class_id ontouml:stereotype ?class_st .}
} GROUP BY ?class_id """
)

QUERY_CL002 = (
    ONTOUML_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name ?class_st
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    OPTIONAL {?class_id ontouml:stereotype ?class_st .}
} """
)

QUERY_CL003 = (
    ONTOUML_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name
WHERE {
  ?class_id rdf:type ontouml:Class .
  ?class_id ontouml:stereotype ontouml:enumeration .
  ?class_id ontouml:name ?class_name .
}
"""
)
