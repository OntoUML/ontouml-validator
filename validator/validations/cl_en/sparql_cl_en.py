"""Define all SPARQL queries to be used in rules of the group CL_EN."""

from validator.validations.constants import ONTOUML_SPARQL_PREFIX

QUERY_CL_EN_01 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name
WHERE {
  ?class_id rdf:type ontouml:Class .
  ?class_id ontouml:stereotype ontouml:enumeration .
  ?class_id ontouml:name ?class_name .
  ?class_id ontouml:attribute ?class_at .
}
"""
)
QUERY_CL_EN_02 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name ?class_st
WHERE {
  ?class_id rdf:type ontouml:Class .
  ?class_id ontouml:name ?class_name .
  ?class_id ontouml:literal ?class_lt .
  OPTIONAL {?class_id ontouml:stereotype ?class_st .}
}
"""
)
QUERY_CL_EN_03 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT ?class_id ?class_name (count(?class_lt) as ?num_lt)
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    OPTIONAL { ?class_id ontouml:literal ?class_lt . }
} GROUP BY ?class_id """
)
QUERY_CL_EN_04 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name
WHERE {
  ?class_id rdf:type ontouml:Class .
  ?class_id ontouml:stereotype ontouml:enumeration .
  ?class_id ontouml:name ?class_name .
  ?gen ontouml:general ?class_id .
}
"""
)
QUERY_CL_EN_05 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name ?sup_st
WHERE {
  ?class_id rdf:type ontouml:Class .
  ?class_id ontouml:stereotype ontouml:enumeration .
  ?class_id ontouml:name ?class_name .
  ?gen ontouml:specific ?class_id .
  ?gen ontouml:general ?class_sup .
  FILTER NOT EXISTS { ?class_sup ontouml:stereotype ontouml:abstract . }
  OPTIONAL { ?class_sup ontouml:stereotype ?sup_st . }
}
"""
)
