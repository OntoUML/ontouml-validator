"""Constants to be used globally in the code."""
from validator.vocab_lib.ONTOUML import ONTOUML

ONTOUML_SPARQL_PREFIX = "PREFIX ontouml: <https://w3id.org/ontouml#> "

ONTOUML_CLASS_STEREOTYPES = [
    ONTOUML.abstract,
    ONTOUML.category,
    ONTOUML.collective,
    ONTOUML.datatype,
    ONTOUML.enumeration,
    ONTOUML.event,
    ONTOUML.historicalRole,
    ONTOUML.historicalRoleMixin,
    ONTOUML.kind,
    ONTOUML.mixin,
    ONTOUML.mode,
    ONTOUML.phase,
    ONTOUML.phaseMixin,
    ONTOUML.quality,
    ONTOUML.quantity,
    ONTOUML.relator,
    ONTOUML.role,
    ONTOUML.roleMixin,
    ONTOUML.situation,
    ONTOUML.subkind,
    ONTOUML.type,
]

ONTOUML_ST_BASE_SORTALS = [
    ONTOUML.historicalRole,
    ONTOUML.phase,
    ONTOUML.role,
    ONTOUML.subkind,
]

ONTOUML_ST_ULTIMATE_SORTALS = [
    ONTOUML.collective,
    ONTOUML.kind,
    ONTOUML.mode,
    ONTOUML.quality,
    ONTOUML.quantity,
    ONTOUML.relator,
    ONTOUML.type,
]

ONTOUML_ST_SORTALS = ONTOUML_ST_BASE_SORTALS + ONTOUML_ST_ULTIMATE_SORTALS

ONTOUML_ST_NON_SORTALS = [
    ONTOUML.category,
    ONTOUML.historicalRoleMixin,
    ONTOUML.mixin,
    ONTOUML.phaseMixin,
    ONTOUML.roleMixin,
]

ONTOUML_ST_ABSTRACTS = [
    ONTOUML.abstract,
    ONTOUML.datatype,
    ONTOUML.enumeration,
]

ONTOUML_ST_RIGIDS = [
    ONTOUML.category,
    ONTOUML.collective,
    ONTOUML.kind,
    ONTOUML.mode,
    ONTOUML.quality,
    ONTOUML.quantity,
    ONTOUML.relator,
    ONTOUML.subkind,
]

ST_ANTI_RIGIDS = [
    ONTOUML.historicalRole,
    ONTOUML.historicalRoleMixin,
    ONTOUML.phase,
    ONTOUML.phaseMixin,
    ONTOUML.role,
    ONTOUML.roleMixin,
]

ONTOUML_ST_SEMI_RIGIDS = [
    ONTOUML.mixin,
]
