"""This module defines a global dictionary `RULES_DEFINITIONS` that maps rule codes to their corresponding rule \
descriptions. These rule descriptions are used in the rules' execution functions to generate identified issues.

The structure of `RULES_DEFINITIONS` is as follows:
{
    "Rule Code": "Rule Description",
    ...
}

Each rule code is a unique identifier for a specific modeling rule, and its corresponding rule description provides
a human-readable explanation of that rule.

Usage Example:
    To retrieve the description of a rule with code "R_CL_EDA," you can use `RULES_DEFINITIONS["R_CL_EDA"]`,
    which will return "Enumeration classes can only be generalized by classes with stereotype Abstract."
"""

RULES_DEFINITIONS = {
    "R_CL_AIB": "Enumeration classes cannot be specialized by other classes.",  # noqa: E501
    "R_CL_ALX": "Every class decorated with a ULTIMATE SORTAL or a NON-SORTAL stereotype cannot specialize classes decorated with a SORTAL or an ABSTRACT stereotype.",  # noqa: E501
    "R_CL_ANY": "No class representing a powertype (i.e., whose tagged value 'isPowertype' is set to 'true') can be the target of more than one non-derived instantiation relation.",  # noqa: E501
    "R_CL_ASZ": "Every class decorated with a non-sortal stereotype and the tagged value 'order' set to '1' must have the tagged value 'restrictedTo' set to an array containing one or more of the values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality' ].",  # noqa: E501
    "R_CL_BFO": "Every class whose tagged value 'restrictedTo' is [ 'collective' ] must have the tagged value 'isExtensional' set to either 'true' or 'false'.",  # noqa: E501
    "R_CL_BLE": "Every class decorated with a RIGID or SEMI-RIGID stereotype cannot specialize classes decorated with an ANTI-RIGID stereotype.",  # noqa: E501
    "R_CL_BQI": "Every class with the tagged value 'restrictedTo' set to [ 'type' ] must have the have the tagged 'order' set to a number greater than '1'.",  # noqa: E501
    "R_CL_BWZ": "Every class must be decorated with stereotypes of the OntoUML profile.",  # noqa: E501
    "R_CL_CMS": "Every class decorated with a «phase» must be part of a disjoint and complete generalization set including only classes decorated with «phase» as the generalizations' specific classes.",  # noqa: E501
    "R_CL_EDA": "Enumeration classes can only be generalized by classes with stereotype Abstract.",  # noqa: E501
    "R_CL_EGT": "No class can have one of its subclasses as its superclasses.",  # noqa: E501
    "R_CL_EMV": "Every class must have the tagged value 'restrictedTo' set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'event', 'situation', 'abstract', 'type' ].",  # noqa: E501
    "R_CL_GAZ": "Every class with the tagged value 'restrictedTo' set to [ 'type' ] and some other value must have the have the tagged 'order' set to '*'.",  # noqa: E501
    "R_CL_GJU": "Every class must be decorated with exactly one stereotype.",  # noqa: E501
    "R_CL_JFW": "Every class representing a powertype (i.e., whose tagged value 'isPowertype' is set to 'true') must only have types as instances (i.e., its tagged value 'restrictedTo' must be set to [ 'type' ]).",  # noqa: E501
    "R_CL_JMQ": "Every class must have the tagged value 'order' set to a number greater than '0' or set to '*'.",  # noqa: E501
    "R_CL_JOJ": "Every class having enumeration literals must be decorated with the stereotype enumeration.",  # noqa: E501
    "R_CL_LAX": "Every class decorated with a base sortal stereotype and the tagged value 'order' set to '1' must have the tagged value 'restrictedTo' set to an array containing one of the values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality' ].",  # noqa: E501
    "R_CL_NBG": "Every class decorated with a «phaseMixin» must be part of a disjoint and complete generalization set including only classes decorated with «phaseMixin» as the generalizations' specific classes.",  # noqa: E501
    "R_CL_OEV": "Every non-derived class decorated with a «role» must be connected directly or indirectly to some relation decorated with the stereotype «mediation» where the opposited end has a cardinality with lower bound '1'.",  # noqa: E501
    "R_CL_PPZ": "Every abstract class should be specialized by some concrete class or have a super class that is specialized by a concrete class.",  # noqa: E501
    "R_CL_PSQ": "Every class decorated with a stereotype «type» must have the have the tagged 'order' set to a number greater than '1' or set to '*'.",  # noqa: E501
    "R_CL_QJC": "Each class with one of the following stereotypes must exclusively map to the corresponding 'restrictedTo' value: collective to collective, event to event, kind to functional-complex, quality to quality, quantity to quantity, relator to relator, situation to situation, abstract to abstract, enumeration to abstract, and datatype to abstract.",  # noqa: E501
    "R_CL_QOV": "Every class representing a powertype (i.e., whose tagged value 'isPowertype' is set to 'true') must be decorated with a RIGID stereotype (i.e., either «category», «type», or «subkind»).",  # noqa: E501
    "R_CL_SQU": "Every class decorated with a stereotype from the set «kind», «collective», «quantity», «relator», «mode», «quality», «event», «situation», «abstract», «datatype», or «enumeration», must have the have the tagged 'order' set to '1'.",  # noqa: E501
    "R_CL_UMC": "Every enumeration class must have at least two literals.",  # noqa: E501
    "R_CL_UTL": "Every class whose tagged value 'restrictedTo' does includes the value [ 'type' ] must have the tagged value 'isPowertype' set to either 'true' or 'false'.",  # noqa: E501
    "R_CL_VOQ": "Every class whose tagged value 'restrictedTo' is not [ 'collective' ] must have the tagged value 'isExtensional' set to 'null'.",  # noqa: E501
    "R_CL_VPE": "Every class whose tagged value 'restrictedTo' does not include the value [ 'type' ] must have the tagged value 'isPowertype' set to 'null'.",  # noqa: E501
    "R_CL_XJZ": "Every class decorated with the stereotype «enumeration» must not have attributes.",  # noqa: E501
    "R_CL_YOK": "Every class decorated with a non-sortal stereotype must be abstract.",  # noqa: E501
    "R_CL_ZEF": "Every class decorated with a stereotype «mode» must have the tagged value 'restrictedTo' set to an array containing one of or both the values [ 'intrinsic-mode', 'extrinsic-mode' ].",  # noqa: E501
    "R_CL_ZGT": "Every class decorated with a base sortal stereotype must specialize a unique class decorated with a ULTIMATE SORTAL stereotype .",  # noqa: E501
    "R_GE_BAK": "No generalization can connect a general class decorated with «abstract» to a specific class that is not decorated with some abstract stereotype (i.e., «abstract», «datatype», or «enumeration»).",  # noqa: E501
    "R_GE_EPG": "No generalization can connect a general class decorated with a ULTIMATE SORTAL stereotype to a specific class decorated with a ULTIMATE SORTAL stereotype.",  # noqa: E501
    "R_GE_HGQ": "No generalization can connect a general class decorated with a sortal stereotype to a specific class decorated with a non-sortal stereotype.",  # noqa: E501
    "R_GE_HPZ": "No generalization can connect a general class to an specific class where the specific class has in its tagged value 'restrictedTo' values that are not present in the same tagged value of the general class.",  # noqa: E501
    "R_GE_IJM": "No generalization can connect a general class decorated with «event» to a specific class decorated with a different stereotype.",  # noqa: E501
    "R_GE_JLW": "No generalization can connect a general class decorated with «datatype» to a specific class decorated with a different stereotype.",  # noqa: E501
    "R_GE_MDR": "Every generalization connected to a general class with its tagged value 'order' set to a number can only connect a specific class whose tagged value 'order' is set to the same number.",  # noqa: E501
    "R_GE_MXI": "No generalization can connect a general class decorated with an ANTI-RIGID stereotype to a specific class decorated with a RIGID or SEMI-RIGID stereotype.",  # noqa: E501
    "R_GE_UXR": "No generalization can connect a general class decorated with «situation» to a specific class decorated with a different stereotype.",  # noqa: E501
    "R_GE_VEZ": "No generalization can connect a general class decorated with «enumeration» to a specific class decorated with a different stereotype.",  # noqa: E501
    "R_GE_XRS": "Every generalization connected to a general class with its tagged value 'isExtensional' set to 'true' can only connect a specific class whose tagged value 'isExtensional' is set to 'true' as well.",  # noqa: E501
    "R_GS_LHD": "Every categorizer in a generalization set must be a high-order type whose instances are types (i.e., whose tagged value 'restrictedTo' is set to [ 'type' ]).",  # noqa: E501
    "R_GS_PQP": "Every categorizer in a generalization set must be the target of an instantiation relation (i.e., a relation decorated with a stereotype «instantiation») whose source is the generalization set's general class.",  # noqa: E501
    "R_GS_UTW": "Every categorizer in a generalization set must have the tagged value 'isPowertype' set to 'false'.",  # noqa: E501
    "R_GS_XXB": "The target's cardinality of the instantiation relation between the general class and the categorizer must not have a lower bound '0' if the generalization set is complete.",  # noqa: E501
    "R_GS_YKW": "Every generalization in a generalization set must share the same general class.",  # noqa: E501
    "R_GS_ZMQ": "The target's cardinality of the instantiation relation between the general class and the categorizer must not have an upper bound '1' if the generalization set is overlapping (or covering).",  # noqa: E501
    "R_PR_BWY": "Every property decorated with a stereotype «begin» must be defined within a class representing an event (i.e., whose tagged value is set to [ 'event' ]).",  # noqa: E501
    "R_PR_LCI": "Every property decorated with a stereotype «end» must be defined within a class representing an event (i.e., whose tagged value is set to [ 'event' ]).",  # noqa: E501
    "R_RE_ALR": "Every relation decorated with a stereotype «historicalDepedence» must connect source class and target class where either both represent endurants (i.e., whose tagged value is set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'type' ]) or both represent events (i.e., whose tagged value 'restrictedTo' is set to [ 'event' ]).",  # noqa: E501
    "R_RE_AZO": "Every relation decorated with a stereotype «bringsAbout» must connect a source class representing an event (i.e., whose tagged value is set to [ 'event' ]) to a target class representing a situation (i.e., whose tagged value 'restrictedTo' is set to [ 'situation' ]).",  # noqa: E501
    "R_RE_CDJ": "Every relation decorated with a stereotype «mediation» must connect a source class representing a relator (i.e., whose tagged value 'restrictedTo' set to [ 'relator' ]) to a target class representing an endurant (i.e., whose tagged value is set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'type' ]).",  # noqa: E501
    "R_RE_EAQ": "Every relation decorated with a stereotype «manifestation» must connect a source class representing a moment (i.e., whose tagged value is set to one or more values in the list [ 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality' ]) to a target class representing an event (i.e., whose tagged value 'restrictedTo' is set to [ 'event' ]).",  # noqa: E501
    "R_RE_ECP": "Every relation decorated with a stereotype «characterization» must connect a source class representing mode or quality (i.e., whose tagged value 'restrictedTo' set to one or more values in the list [ 'intrinsic-mode', 'extrinsic-mode', 'quality' ]) to a target class representing an endurant (i.e., whose tagged value is set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'type' ]).",  # noqa: E501
    "R_RE_FIX": "Every relation decorated with a stereotype «componentOf» must connect a source class and a target class representing functional-complexes (i.e., whose tagged value 'restrictedTo' is set to [ 'functional-complex' ]).",  # noqa: E501
    "R_RE_GZF": "No relation decorated with a stereotype «instantiation» can connect an ordered source class (i.e., whose tagged value 'order' is set to a number 'x') to a target class that is not an orderless (i.e., whose tagged value 'order' is set to '*') or in the order immediately above (i.e., whose tagged value 'order' is set to a number 'x+1').",  # noqa: E501
    "R_RE_GZN": "Every relation decorated with a stereotype «triggers» must connect a source class representing a situation (i.e., whose tagged value is set to [ 'situation' ]) to a target class representing an event (i.e., whose tagged value 'restrictedTo' is set to [ 'event' ]).",  # noqa: E501
    "R_RE_HGG": "Every relation decorated with a stereotype «creation» must connect a source class representing an endurant (i.e., whose tagged value is set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'type' ]) to a target class representing an event (i.e., whose tagged value 'restrictedTo' is set to [ 'event' ]).",  # noqa: E501
    "R_RE_JND": "No relation decorated with a stereotype «instantiation» can connect an orderless source class (i.e., whose tagged value 'order' is set to '*') to a target class that is not an orderless as well.",  # noqa: E501
    "R_RE_KPG": "Every relation must be decorated with at most one stereotype.",  # noqa: E501
    "R_RE_KZC": "Every relation decorated with a stereotype «participation» must connect a source class representing an endurant (i.e., whose tagged value is set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'type' ]) to a target class representing an event (i.e., whose tagged value 'restrictedTo' is set to [ 'event' ]).",  # noqa: E501
    "R_RE_LQF": "Every relation decorated with a stereotype «termination» must connect a source class representing an endurant (i.e., whose tagged value is set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'type' ]) to a target class representing an event (i.e., whose tagged value 'restrictedTo' is set to [ 'event' ]).",  # noqa: E501
    "R_RE_NTY": "Every relation decorated with a stereotype «participational» must connect a source class and a target class representing events (i.e., whose tagged value 'restrictedTo' is set to [ 'event' ]).",  # noqa: E501
    "R_RE_RON": "Every relation decorated with a stereotype «memberOf» must connect a source class representing a functional-complex (i.e., whose tagged value 'restrictedTo' is set to [ 'functional-complex' ]) to a target class representing a collective (i.e., whose tagged value 'restrictedTo' is set to [ 'collective' ]).",  # noqa: E501
    "R_RE_SEI": "Every relation decorated with a stereotype «instantiation» must connect a target class representing a high-order type whose instances are types (i.e., whose tagged value 'restrictedTo' is set to [ 'type' ]).",  # noqa: E501
    "R_RE_UCH": "Every relation decorated with a stereotype «subCollectionOf» must connect a source class and a target class representing collectives (i.e., whose tagged value 'restrictedTo' is set to [ 'collective' ]).",  # noqa: E501
    "R_RE_VDQ": "Every relation decorated with a stereotype «derivation» must connect a source relation to a target class.",  # noqa: E501
    "R_RE_VMI": "Every relation decorated with a stereotype «externalDependence» must connect a source class representing extrinsic mode (i.e., whose tagged value 'restrictedTo' set to [ 'extrinsic-mode' ]) to a target class representing an endurant (i.e., whose tagged value is set to one or more values in the list [ 'functional-complex', 'collective', 'quantity', 'relator', 'intrinsic-mode', 'extrinsic-mode', 'quality', 'type' ]).",  # noqa: E501
}
