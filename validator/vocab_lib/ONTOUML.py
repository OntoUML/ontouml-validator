"""
Module for the ONTOUML namespace mapping to the OntoUML vocabulary.

This module defines the ONTOUML class, which serves as a convenient way to access OntoUML terms and concepts in Python
code. It complies with the OntoUML vocabulary version 1.1.0 available at https://w3id.org/ontouml/vocabulary/v1.1.0.

Usage:
    - Import the ONTOUML class from this module to access OntoUML terms with their associated URIs.
    - Use ONTOUML.term_name to access specific OntoUML terms.

Example:
    ```
    from ontouml_namespace import ONTOUML

    my_ontouml_term = ONTOUML.term_name
    ```

For more information about the OntoUML vocabulary,
refer to the official documentation at: https://w3id.org/ontouml/vocabulary
"""

from rdflib import URIRef
from rdflib.namespace import DefinedNamespace, Namespace


class ONTOUML(DefinedNamespace):
    """Class to provide terms from the OntoUML vocabulary in an easy way.

    All vocabulary concepts and their return values (as comments).
    Complies with https://w3id.org/ontouml/vocabulary/v1.1.0.
    """

    abstract: URIRef  # https://w3id.org/ontouml#abstract
    abstractNature: URIRef  # https://w3id.org/ontouml#abstractNature
    aggregationKind: URIRef  # https://w3id.org/ontouml#aggregationKind
    AggregationKind: URIRef  # https://w3id.org/ontouml#AggregationKind
    attribute: URIRef  # https://w3id.org/ontouml#attribute
    begin: URIRef  # https://w3id.org/ontouml#begin
    bringsAbout: URIRef  # https://w3id.org/ontouml#bringsAbout
    cardinality: URIRef  # https://w3id.org/ontouml#cardinality
    Cardinality: URIRef  # https://w3id.org/ontouml#Cardinality
    cardinalityValue: URIRef  # https://w3id.org/ontouml#cardinalityValue
    categorizer: URIRef  # https://w3id.org/ontouml#categorizer
    category: URIRef  # https://w3id.org/ontouml#category
    characterization: URIRef  # https://w3id.org/ontouml#characterization
    Class: URIRef  # https://w3id.org/ontouml#Class
    Classifier: URIRef  # https://w3id.org/ontouml#Classifier
    ClassStereotype: URIRef  # https://w3id.org/ontouml#ClassStereotype
    ClassView: URIRef  # https://w3id.org/ontouml#ClassView
    collective: URIRef  # https://w3id.org/ontouml#collective
    collectiveNature: URIRef  # https://w3id.org/ontouml#collectiveNature
    comparative: URIRef  # https://w3id.org/ontouml#comparative
    componentOf: URIRef  # https://w3id.org/ontouml#componentOf
    composite: URIRef  # https://w3id.org/ontouml#composite
    ConnectorView: URIRef  # https://w3id.org/ontouml#ConnectorView
    containsModelElement: URIRef  # https://w3id.org/ontouml#containsModelElement
    containsView: URIRef  # https://w3id.org/ontouml#containsView
    creation: URIRef  # https://w3id.org/ontouml#creation
    datatype: URIRef  # https://w3id.org/ontouml#datatype
    DecoratableElement: URIRef  # https://w3id.org/ontouml#DecoratableElement
    derivation: URIRef  # https://w3id.org/ontouml#derivation
    description: URIRef  # https://w3id.org/ontouml#description
    diagram: URIRef  # https://w3id.org/ontouml#diagram
    Diagram: URIRef  # https://w3id.org/ontouml#Diagram
    DiagramElement: URIRef  # https://w3id.org/ontouml#DiagramElement
    ElementView: URIRef  # https://w3id.org/ontouml#ElementView
    end: URIRef  # https://w3id.org/ontouml#end
    enumeration: URIRef  # https://w3id.org/ontouml#enumeration
    event: URIRef  # https://w3id.org/ontouml#event
    eventNature: URIRef  # https://w3id.org/ontouml#eventNature
    externalDependence: URIRef  # https://w3id.org/ontouml#externalDependence
    extrinsicModeNature: URIRef  # https://w3id.org/ontouml#extrinsicModeNature
    functionalComplexNature: URIRef  # https://w3id.org/ontouml#functionalComplexNature
    general: URIRef  # https://w3id.org/ontouml#general
    generalization: URIRef  # https://w3id.org/ontouml#generalization
    Generalization: URIRef  # https://w3id.org/ontouml#Generalization
    GeneralizationSet: URIRef  # https://w3id.org/ontouml#GeneralizationSet
    GeneralizationSetView: URIRef  # https://w3id.org/ontouml#GeneralizationSetView
    GeneralizationView: URIRef  # https://w3id.org/ontouml#GeneralizationView
    height: URIRef  # https://w3id.org/ontouml#height
    historicalDependence: URIRef  # https://w3id.org/ontouml#historicalDependence
    historicalRole: URIRef  # https://w3id.org/ontouml#historicalRole
    historicalRoleMixin: URIRef  # https://w3id.org/ontouml#historicalRoleMixin
    instantiation: URIRef  # https://w3id.org/ontouml#instantiation
    intrinsicModeNature: URIRef  # https://w3id.org/ontouml#intrinsicModeNature
    isAbstract: URIRef  # https://w3id.org/ontouml#isAbstract
    isComplete: URIRef  # https://w3id.org/ontouml#isComplete
    isDerived: URIRef  # https://w3id.org/ontouml#isDerived
    isDisjoint: URIRef  # https://w3id.org/ontouml#isDisjoint
    isExtensional: URIRef  # https://w3id.org/ontouml#isExtensional
    isOrdered: URIRef  # https://w3id.org/ontouml#isOrdered
    isPowertype: URIRef  # https://w3id.org/ontouml#isPowertype
    isReadOnly: URIRef  # https://w3id.org/ontouml#isReadOnly
    isViewOf: URIRef  # https://w3id.org/ontouml#isViewOf
    kind: URIRef  # https://w3id.org/ontouml#kind
    literal: URIRef  # https://w3id.org/ontouml#literal
    Literal: URIRef  # https://w3id.org/ontouml#Literal
    lowerBound: URIRef  # https://w3id.org/ontouml#lowerBound
    manifestation: URIRef  # https://w3id.org/ontouml#manifestation
    material: URIRef  # https://w3id.org/ontouml#material
    mediation: URIRef  # https://w3id.org/ontouml#mediation
    memberOf: URIRef  # https://w3id.org/ontouml#memberOf
    mixin: URIRef  # https://w3id.org/ontouml#mixin
    mode: URIRef  # https://w3id.org/ontouml#mode
    model: URIRef  # https://w3id.org/ontouml#model
    ModelElement: URIRef  # https://w3id.org/ontouml#ModelElement
    name: URIRef  # https://w3id.org/ontouml#name
    NodeView: URIRef  # https://w3id.org/ontouml#NodeView
    none: URIRef  # https://w3id.org/ontouml#none
    Note: URIRef  # https://w3id.org/ontouml#Note
    NoteView: URIRef  # https://w3id.org/ontouml#NoteView
    OntologicalNature: URIRef  # https://w3id.org/ontouml#OntologicalNature
    OntoumlElement: URIRef  # https://w3id.org/ontouml#OntoumlElement
    order: URIRef  # https://w3id.org/ontouml#order
    owner: URIRef  # https://w3id.org/ontouml#owner
    Package: URIRef  # https://w3id.org/ontouml#Package
    PackageView: URIRef  # https://w3id.org/ontouml#PackageView
    participation: URIRef  # https://w3id.org/ontouml#participation
    participational: URIRef  # https://w3id.org/ontouml#participational
    Path: URIRef  # https://w3id.org/ontouml#Path
    phase: URIRef  # https://w3id.org/ontouml#phase
    phaseMixin: URIRef  # https://w3id.org/ontouml#phaseMixin
    point: URIRef  # https://w3id.org/ontouml#point
    Point: URIRef  # https://w3id.org/ontouml#Point
    project: URIRef  # https://w3id.org/ontouml#project
    Project: URIRef  # https://w3id.org/ontouml#Project
    property: URIRef  # https://w3id.org/ontouml#property
    Property: URIRef  # https://w3id.org/ontouml#Property
    PropertyStereotype: URIRef  # https://w3id.org/ontouml#PropertyStereotype
    propertyType: URIRef  # https://w3id.org/ontouml#propertyType
    quality: URIRef  # https://w3id.org/ontouml#quality
    qualityNature: URIRef  # https://w3id.org/ontouml#qualityNature
    quantity: URIRef  # https://w3id.org/ontouml#quantity
    quantityNature: URIRef  # https://w3id.org/ontouml#quantityNature
    Rectangle: URIRef  # https://w3id.org/ontouml#Rectangle
    RectangularShape: URIRef  # https://w3id.org/ontouml#RectangularShape
    redefinesProperty: URIRef  # https://w3id.org/ontouml#redefinesProperty
    Relation: URIRef  # https://w3id.org/ontouml#Relation
    relationEnd: URIRef  # https://w3id.org/ontouml#relationEnd
    RelationStereotype: URIRef  # https://w3id.org/ontouml#RelationStereotype
    RelationView: URIRef  # https://w3id.org/ontouml#RelationView
    relator: URIRef  # https://w3id.org/ontouml#relator
    relatorNature: URIRef  # https://w3id.org/ontouml#relatorNature
    restrictedTo: URIRef  # https://w3id.org/ontouml#restrictedTo
    role: URIRef  # https://w3id.org/ontouml#role
    roleMixin: URIRef  # https://w3id.org/ontouml#roleMixin
    shape: URIRef  # https://w3id.org/ontouml#shape
    Shape: URIRef  # https://w3id.org/ontouml#Shape
    shared: URIRef  # https://w3id.org/ontouml#shared
    situation: URIRef  # https://w3id.org/ontouml#situation
    situationNature: URIRef  # https://w3id.org/ontouml#situationNature
    sourceEnd: URIRef  # https://w3id.org/ontouml#sourceEnd
    sourceView: URIRef  # https://w3id.org/ontouml#sourceView
    specific: URIRef  # https://w3id.org/ontouml#specific
    stereotype: URIRef  # https://w3id.org/ontouml#stereotype
    Stereotype: URIRef  # https://w3id.org/ontouml#Stereotype
    subCollectionOf: URIRef  # https://w3id.org/ontouml#subCollectionOf
    subkind: URIRef  # https://w3id.org/ontouml#subkind
    subQuantityOf: URIRef  # https://w3id.org/ontouml#subQuantityOf
    subsetsProperty: URIRef  # https://w3id.org/ontouml#subsetsProperty
    targetEnd: URIRef  # https://w3id.org/ontouml#targetEnd
    targetView: URIRef  # https://w3id.org/ontouml#targetView
    termination: URIRef  # https://w3id.org/ontouml#termination
    text: URIRef  # https://w3id.org/ontouml#text
    Text: URIRef  # https://w3id.org/ontouml#Text
    topLeftPosition: URIRef  # https://w3id.org/ontouml#topLeftPosition
    triggers: URIRef  # https://w3id.org/ontouml#triggers
    type: URIRef  # https://w3id.org/ontouml#type
    typeNature: URIRef  # https://w3id.org/ontouml#typeNature
    upperBound: URIRef  # https://w3id.org/ontouml#upperBound
    width: URIRef  # https://w3id.org/ontouml#width
    xCoordinate: URIRef  # https://w3id.org/ontouml#xCoordinate
    yCoordinate: URIRef  # https://w3id.org/ontouml#yCoordinate

    _fail = True
    _underscore_num = True

    _NS = Namespace("https://w3id.org/ontouml#")
