"""Constants to be used globally in the code."""
from validator.vocab_lib.ontouml import ONTOUML

ONTOUML_SPARQL_PREFIX = "PREFIX ontouml: <https://w3id.org/ontouml#> "

ONTOUML_CLASS_STEREOTYPES = [
    str(ONTOUML.abstract),
    str(ONTOUML.category),
    str(ONTOUML.collective),
    str(ONTOUML.datatype),
    str(ONTOUML.enumeration),
    str(ONTOUML.event),
    str(ONTOUML.historicalRole),
    str(ONTOUML.historicalRoleMixin),
    str(ONTOUML.kind),
    str(ONTOUML.mixin),
    str(ONTOUML.mode),
    str(ONTOUML.phase),
    str(ONTOUML.phaseMixin),
    str(ONTOUML.quality),
    str(ONTOUML.quantity),
    str(ONTOUML.relator),
    str(ONTOUML.role),
    str(ONTOUML.roleMixin),
    str(ONTOUML.situation),
    str(ONTOUML.subkind),
    str(ONTOUML.type),
]

ONTOUML_ST_BASE_SORTALS = [
    str(ONTOUML.historicalRole),
    str(ONTOUML.phase),
    str(ONTOUML.role),
    str(ONTOUML.subkind),
]

ONTOUML_ST_ULTIMATE_SORTALS = [
    str(ONTOUML.collective),
    str(ONTOUML.kind),
    str(ONTOUML.mode),
    str(ONTOUML.quality),
    str(ONTOUML.quantity),
    str(ONTOUML.relator),
    str(ONTOUML.type),
]

ONTOUML_ST_SORTALS = ONTOUML_ST_BASE_SORTALS + ONTOUML_ST_ULTIMATE_SORTALS

ONTOUML_ST_NON_SORTALS = [
    str(ONTOUML.category),
    str(ONTOUML.historicalRoleMixin),
    str(ONTOUML.mixin),
    str(ONTOUML.phaseMixin),
    str(ONTOUML.roleMixin),
]

ONTOUML_ST_ABSTRACTS = [
    str(ONTOUML.abstract),
    str(ONTOUML.datatype),
    str(ONTOUML.enumeration),
]

ONTOUML_ST_RIGIDS = [
    str(ONTOUML.category),
    str(ONTOUML.collective),
    str(ONTOUML.kind),
    str(ONTOUML.mode),
    str(ONTOUML.quality),
    str(ONTOUML.quantity),
    str(ONTOUML.relator),
    str(ONTOUML.subkind),
]

ST_ANTI_RIGIDS = [
    str(ONTOUML.historicalRole),
    str(ONTOUML.historicalRoleMixin),
    str(ONTOUML.phase),
    str(ONTOUML.phaseMixin),
    str(ONTOUML.role),
    str(ONTOUML.roleMixin),
]

ONTOUML_ST_SEMI_RIGIDS = [
    str(ONTOUML.mixin),
]

ONTOUML_ONTOLOGICAL_NATURES = [
    str(ONTOUML.abstractNature),
    str(ONTOUML.collectiveNature),
    str(ONTOUML.eventNature),
    str(ONTOUML.extrinsicModeNature),
    str(ONTOUML.functionalComplexNature),
    str(ONTOUML.intrinsicModeNature),
    str(ONTOUML.qualityNature),
    str(ONTOUML.quantityNature),
    str(ONTOUML.relatorNature),
    str(ONTOUML.situationNature),
    str(ONTOUML.typeNature),
]
