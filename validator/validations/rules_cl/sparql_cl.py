"""Define all SPARQL queries to be used in rules of the group CL."""
from validator.vocab_lib.variables import ONTOUML_SPARQL_PREFIX

QUERY_R_CL_XJZ = (
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

QUERY_R_CL_JOJ = (
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

QUERY_R_CL_UMC = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT ?class_id ?class_name ?class_st (count(?class_lt) as ?num_lt)
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    ?class_id ontouml:stereotype ontouml:enumeration .
    OPTIONAL { ?class_id ontouml:literal ?class_lt . }
} GROUP BY ?class_id """
)

QUERY_R_CL_AIB = (
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

QUERY_R_CL_EDA = (
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

QUERY_R_CL_GJU = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT ?class_id ?class_name (count(?class_st) as ?num_sts)
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    OPTIONAL {?class_id ontouml:stereotype ?class_st .}
} GROUP BY ?class_id """
)

QUERY_R_CL_BWZ = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT DISTINCT ?class_id ?class_name ?class_st
WHERE {
    ?class_id rdf:type ontouml:Class .
    ?class_id ontouml:name ?class_name .
    OPTIONAL {?class_id ontouml:stereotype ?class_st .}
} """
)

QUERY_R_CL_YOK = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT ?class_id ?class_name ?class_st
WHERE {
  ?class_id a ontouml:Class ;
         ontouml:name ?class_name ;
         ontouml:stereotype ?class_st ;
         ontouml:isAbstract false .
  FILTER (?class_st IN (ontouml:category, ontouml:historicalRoleMixin, ontouml:mixin,
                        ontouml:phaseMixin, ontouml:roleMixin))
}
"""
)

QUERY_TAGGED_VALUE = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT ?class_id ?class_name ?class_st ?tagged
WHERE {
  ?class_id a ontouml:Class ;
            ontouml:name ?class_name ;
            ontouml:stereotype ?class_st .
  OPTIONAL {?class_id ontouml:restrictedTo ?tagged . }
}
"""
)
