"""Define all SPARQL queries to be used in rules of the group CL_SO."""

from validator.validations.constants import ONTOUML_SPARQL_PREFIX

QUERY_CL_SO_01 = (
    ONTOUML_SPARQL_PREFIX
    + """
SELECT ?class_id ?class_name (COUNT(DISTINCT ?sup_id) AS ?count)
WHERE {
    ?class_id rdfs:subClassOf* ?sup_id .
    ?sup_id ontouml:stereotype ?class_st .
    ?sup_id ontouml:stereotype ?sup_st .
    FILTER (?class_st IN (ontouml:subkind, ontouml:phase, ontouml:role, ontouml:historicalRole))
    FILTER (?sup_st IN (ontouml:kind, ontouml:collective, ontouml:quantity,
                        ontouml:relator, ontouml:mode, ontouml:quality, ontouml:type))
} GROUP BY ?class_id
"""
)
