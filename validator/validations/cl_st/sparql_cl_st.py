"""Define all SPARQL queries to be used in rules of the group CL_ST."""

from validator.validations.constants import ONTOUML_SPARQL_PREFIX

QUERY_CL_ST_01 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT ?class_id ?class_name (count(?class_st) as ?num_sts)
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    OPTIONAL {?class_id ontouml:stereotype ?class_st .}
} GROUP BY ?class_id """
)

QUERY_CL_ST_02 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name ?class_st
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    OPTIONAL {?class_id ontouml:stereotype ?class_st .}
} """
)
