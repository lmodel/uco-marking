# Auto generated from uco_marking.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-04-11T23:53:38
# Schema: uco-marking
#
# id: https://w3id.org/lmodel/uco-marking
# description: Data markings represent restrictions, permissions, and other guidance for how data can be used and
#              shared.
# license: https://www.apache.org/licenses/LICENSE-2.0

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Datetime, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = "1.1.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CSO = CurieNamespace('CSO', 'https://cso.kmi.open.ac.uk/topics/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
REPR = CurieNamespace('REPR', 'https://w3id.org/reproduceme#')
SEPIO = CurieNamespace('SEPIO', 'http://purl.obolibrary.org/obo/SEPIO_')
SIO = CurieNamespace('SIO', 'http://identifiers.org/sio/')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://identifiers.org/wikidata/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/uco-core/')
CSRC = CurieNamespace('csrc', 'https://csrc.nist.gov/glossary/term/')
DCID = CurieNamespace('dcid', 'https://datacommons.org/browser/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
GR = CurieNamespace('gr', 'http://purl.org/goodrelations/v1#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LM_CORE = CurieNamespace('lm_core', 'https://w3id.org/lmodel/core/')
MARKING = CurieNamespace('marking', 'https://w3id.org/lmodel/uco-marking/')
OM = CurieNamespace('om', 'http://www.ontology-of-units-of-measure.org/resource/om-2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCHEMA_UCO_CORE = CurieNamespace('schema_uco_core', 'https://w3id.org/lmodel/uco-core/schema/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SUMO = CurieNamespace('sumo', 'https://w3id.org/sumo/kb/')
WIKIDATA = CurieNamespace('wikidata', 'http://identifiers.org/wikidata/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MARKING


# Types
class StringType(String):
    """ A string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string type"
    type_model_uri = MARKING.StringType


class LiteralType(String):
    """ Literals are used for values such as strings, numbers, and dates. """
    type_class_uri = RDF.literal
    type_class_curie = "rdf:literal"
    type_name = "literal type"
    type_model_uri = MARKING.LiteralType


class NonNegativeIntegerType(Integer):
    """ real number strictly greater than zero """
    type_class_uri = XSD.nonNegativeInteger
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "non negative integer type"
    type_model_uri = MARKING.NonNegativeIntegerType


class StatementType(StringType):
    """ "meaningful declarative sentence that is either true or false, or that which a true or false declarative sentence asserts" """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "statement type"
    type_model_uri = MARKING.StatementType


class IriType(Uriorcurie):
    """ A IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = MARKING.IriType


class BooleanType(Boolean):
    """ A boolean value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean type"
    type_model_uri = MARKING.BooleanType


class HexBinaryType(hex):
    """ "Represents arbitrary hex-encoded binary data" """
    type_class_uri = XSD.hexBinary
    type_class_curie = "xsd:hexBinary"
    type_name = "hex binary type"
    type_model_uri = MARKING.HexBinaryType


# Class references



class UcoThing(YAMLRoot):
    """
    UcoThing is the top-level class within UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoThing
    class_class_curie: ClassVar[str] = "core:UcoThing"
    class_name: ClassVar[str] = "UcoThing"
    class_model_uri: ClassVar[URIRef] = MARKING.UcoThing


class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics unique to a particular inherent aspect of a
    UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoInherentCharacterizationThing
    class_class_curie: ClassVar[str] = "core:UcoInherentCharacterizationThing"
    class_name: ClassVar[str] = "UcoInherentCharacterizationThing"
    class_model_uri: ClassVar[URIRef] = MARKING.UcoInherentCharacterizationThing


@dataclass
class GranularMarking(UcoInherentCharacterizationThing):
    """
    A granular marking is a grouping of characteristics unique to specification of MarkingDefinitions (restrictions,
    permissions, and other guidance for how data can be used and shared) that apply to particular portions of a
    particular UCO object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.GranularMarking
    class_class_curie: ClassVar[str] = "marking:GranularMarking"
    class_name: ClassVar[str] = "GranularMarking"
    class_model_uri: ClassVar[URIRef] = MARKING.GranularMarking

    marking: Optional[Union[str, List[str]]] = empty_list()
    contentSelectors: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.marking, list):
            self.marking = [self.marking] if self.marking is not None else []
        self.marking = [v if isinstance(v, str) else str(v) for v in self.marking]

        if not isinstance(self.contentSelectors, list):
            self.contentSelectors = [self.contentSelectors] if self.contentSelectors is not None else []
        self.contentSelectors = [v if isinstance(v, str) else str(v) for v in self.contentSelectors]

        super().__post_init__(**kwargs)


class MarkingModel(UcoInherentCharacterizationThing):
    """
    A MarkingModel is a grouping of characteristics unique to the expression of a particular form of data
    MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.MarkingModel
    class_class_curie: ClassVar[str] = "marking:MarkingModel"
    class_name: ClassVar[str] = "MarkingModel"
    class_model_uri: ClassVar[URIRef] = MARKING.MarkingModel


@dataclass
class LicenseMarking(MarkingModel):
    """
    A MarkingDefinition is a grouping of characteristics unique to the expression of a specific data marking conveying
    restrictions, permissions, and other guidance for how marked data can be used and shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.LicenseMarking
    class_class_curie: ClassVar[str] = "marking:LicenseMarking"
    class_name: ClassVar[str] = "LicenseMarking"
    class_model_uri: ClassVar[URIRef] = MARKING.LicenseMarking

    license: str = None
    definitionType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, str):
            self.license = str(self.license)

        if self.definitionType is not None and not isinstance(self.definitionType, str):
            self.definitionType = str(self.definitionType)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class ReleaseToMarking(MarkingModel):
    """
    A release-to marking is a grouping of characteristics unique to the expression of data MarkingDefinitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of
    authorized persons and/or organizations to which to the associated content may be released. The existence of the
    Release-To marking restricts access to ONLY those identities explicitly listed, regardless of whether another data
    marking exists that allows sharing with other members of the community.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.ReleaseToMarking
    class_class_curie: ClassVar[str] = "marking:ReleaseToMarking"
    class_name: ClassVar[str] = "ReleaseToMarking"
    class_model_uri: ClassVar[URIRef] = MARKING.ReleaseToMarking

    authorizedIdentities: Union[str, List[str]] = None
    definitionType: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.authorizedIdentities):
            self.MissingRequiredField("authorizedIdentities")
        if not isinstance(self.authorizedIdentities, list):
            self.authorizedIdentities = [self.authorizedIdentities] if self.authorizedIdentities is not None else []
        self.authorizedIdentities = [v if isinstance(v, str) else str(v) for v in self.authorizedIdentities]

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class StatementMarking(MarkingModel):
    """
    A statement marking is a grouping of characteristics unique to the expression of data MarkingDefinitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual
    marking statement, (e.g., copyright) whose semantic meaning should apply to the associated content. Statement
    markings are generally not machine-readable. An example of this would be a simple marking to apply copyright
    information, such as 'Copyright 2014 Acme Inc.'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.StatementMarking
    class_class_curie: ClassVar[str] = "marking:StatementMarking"
    class_name: ClassVar[str] = "StatementMarking"
    class_model_uri: ClassVar[URIRef] = MARKING.StatementMarking

    statement: str = None
    definitionType: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.statement):
            self.MissingRequiredField("statement")
        if not isinstance(self.statement, str):
            self.statement = str(self.statement)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class TermsOfUseMarking(MarkingModel):
    """
    A terms of use marking is a grouping of characteristics unique to the expression of data MarkingDefinitions
    (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of a textual
    statement specifying the Terms of Use (that is, the conditions under which the content may be shared, applied, or
    otherwise used) of the marked content. An example of this would be used to communicate a simple statement, such as
    'Acme Inc. is not responsible for the content of this file'.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.TermsOfUseMarking
    class_class_curie: ClassVar[str] = "marking:TermsOfUseMarking"
    class_name: ClassVar[str] = "TermsOfUseMarking"
    class_model_uri: ClassVar[URIRef] = MARKING.TermsOfUseMarking

    termsOfUse: str = None
    definitionType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.termsOfUse):
            self.MissingRequiredField("termsOfUse")
        if not isinstance(self.termsOfUse, str):
            self.termsOfUse = str(self.termsOfUse)

        if self.definitionType is not None and not isinstance(self.definitionType, str):
            self.definitionType = str(self.definitionType)

        if not isinstance(self.definitionType, list):
            self.definitionType = [self.definitionType] if self.definitionType is not None else []
        self.definitionType = [v if isinstance(v, str) else str(v) for v in self.definitionType]

        super().__post_init__(**kwargs)


@dataclass
class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ExternalReference
    class_class_curie: ClassVar[str] = "core:ExternalReference"
    class_name: ClassVar[str] = "ExternalReference"
    class_model_uri: ClassVar[URIRef] = MARKING.ExternalReference

    referenceURL: Optional[Union[str, IriType]] = None
    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.referenceURL is not None and not isinstance(self.referenceURL, IriType):
            self.referenceURL = IriType(self.referenceURL)

        if self.definingContext is not None and not isinstance(self.definingContext, str):
            self.definingContext = str(self.definingContext)

        if self.externalIdentifier is not None and not isinstance(self.externalIdentifier, str):
            self.externalIdentifier = str(self.externalIdentifier)

        super().__post_init__(**kwargs)


class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular inherent aspect of a UCO domain object.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Facet
    class_class_curie: ClassVar[str] = "core:Facet"
    class_name: ClassVar[str] = "Facet"
    class_model_uri: ClassVar[URIRef] = MARKING.Facet


@dataclass
class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of certainty in the accuracy of some
    information.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ConfidenceFacet
    class_class_curie: ClassVar[str] = "core:ConfidenceFacet"
    class_name: ClassVar[str] = "ConfidenceFacet"
    class_model_uri: ClassVar[URIRef] = MARKING.ConfidenceFacet

    confidence: Union[int, NonNegativeIntegerType] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.confidence):
            self.MissingRequiredField("confidence")
        if not isinstance(self.confidence, NonNegativeIntegerType):
            self.confidence = NonNegativeIntegerType(self.confidence)

        super().__post_init__(**kwargs)


@dataclass
class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly inherent to the cyber domain or
    indirectly related to the cyber domain and necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the base class acting as a consistent,
    unifying and interoperable foundation for all explicit and inter-relatable content objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.UcoObject
    class_class_curie: ClassVar[str] = "core:UcoObject"
    class_name: ClassVar[str] = "UcoObject"
    class_model_uri: ClassVar[URIRef] = MARKING.UcoObject

    createdBy: Optional[str] = None
    description: Optional[Union[str, List[str]]] = empty_list()
    externalReference: Optional[Union[str, List[str]]] = empty_list()
    hasFacet: Optional[Union[str, List[str]]] = empty_list()
    modifiedTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    name: Optional[str] = None
    objectMarking: Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]] = empty_list()
    objectCreatedTime: Optional[Union[str, XSDDateTime]] = None
    specVersion: Optional[str] = None
    tag: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.createdBy is not None and not isinstance(self.createdBy, str):
            self.createdBy = str(self.createdBy)

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.externalReference, list):
            self.externalReference = [self.externalReference] if self.externalReference is not None else []
        self.externalReference = [v if isinstance(v, str) else str(v) for v in self.externalReference]

        if not isinstance(self.hasFacet, list):
            self.hasFacet = [self.hasFacet] if self.hasFacet is not None else []
        self.hasFacet = [v if isinstance(v, str) else str(v) for v in self.hasFacet]

        if not isinstance(self.modifiedTime, list):
            self.modifiedTime = [self.modifiedTime] if self.modifiedTime is not None else []
        self.modifiedTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.modifiedTime]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.objectMarking, list):
            self.objectMarking = [self.objectMarking] if self.objectMarking is not None else []
        self.objectMarking = [v if isinstance(v, MarkingDefinitionAbstraction) else MarkingDefinitionAbstraction(**as_dict(v)) for v in self.objectMarking]

        if self.objectCreatedTime is not None and not isinstance(self.objectCreatedTime, XSDDateTime):
            self.objectCreatedTime = XSDDateTime(self.objectCreatedTime)

        if self.specVersion is not None and not isinstance(self.specVersion, str):
            self.specVersion = str(self.specVersion)

        if not isinstance(self.tag, list):
            self.tag = [self.tag] if self.tag is not None else []
        self.tag = [v if isinstance(v, str) else str(v) for v in self.tag]

        super().__post_init__(**kwargs)


@dataclass
class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Assertion
    class_class_curie: ClassVar[str] = "core:Assertion"
    class_name: ClassVar[str] = "Assertion"
    class_model_uri: ClassVar[URIRef] = MARKING.Assertion

    statement: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.statement, list):
            self.statement = [self.statement] if self.statement is not None else []
        self.statement = [v if isinstance(v, str) else str(v) for v in self.statement]

        super().__post_init__(**kwargs)


@dataclass
class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Annotation
    class_class_curie: ClassVar[str] = "core:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = MARKING.Annotation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming authority.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AttributedName
    class_class_curie: ClassVar[str] = "core:AttributedName"
    class_name: ClassVar[str] = "AttributedName"
    class_model_uri: ClassVar[URIRef] = MARKING.AttributedName

    namingAuthority: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.namingAuthority is not None and not isinstance(self.namingAuthority, str):
            self.namingAuthority = str(self.namingAuthority)

        super().__post_init__(**kwargs)


class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Compilation
    class_class_curie: ClassVar[str] = "core:Compilation"
    class_name: ClassVar[str] = "Compilation"
    class_model_uri: ClassVar[URIRef] = MARKING.Compilation


@dataclass
class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed
    on a given day, all accounts associated with a given person).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ContextualCompilation
    class_class_curie: ClassVar[str] = "core:ContextualCompilation"
    class_name: ClassVar[str] = "ContextualCompilation"
    class_model_uri: ClassVar[URIRef] = MARKING.ContextualCompilation

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


@dataclass
class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ControlledVocabulary
    class_class_curie: ClassVar[str] = "core:ControlledVocabulary"
    class_name: ClassVar[str] = "ControlledVocabulary"
    class_model_uri: ClassVar[URIRef] = MARKING.ControlledVocabulary

    value: str = None
    constrainingVocabularyReference: Optional[Union[str, IriType]] = None
    constrainingVocabularyName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.constrainingVocabularyReference is not None and not isinstance(self.constrainingVocabularyReference, IriType):
            self.constrainingVocabularyReference = IriType(self.constrainingVocabularyReference)

        if self.constrainingVocabularyName is not None and not isinstance(self.constrainingVocabularyName, str):
            self.constrainingVocabularyName = str(self.constrainingVocabularyName)

        super().__post_init__(**kwargs)


@dataclass
class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.EnclosingCompilation
    class_class_curie: ClassVar[str] = "core:EnclosingCompilation"
    class_name: ClassVar[str] = "EnclosingCompilation"
    class_model_uri: ClassVar[URIRef] = MARKING.EnclosingCompilation

    object: Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.object]

        super().__post_init__(**kwargs)


class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Bundle
    class_class_curie: ClassVar[str] = "core:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = MARKING.Bundle


@dataclass
class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Grouping
    class_class_curie: ClassVar[str] = "core:Grouping"
    class_name: ClassVar[str] = "Grouping"
    class_model_uri: ClassVar[URIRef] = MARKING.Grouping

    object: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    context: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.context, list):
            self.context = [self.context] if self.context is not None else []
        self.context = [v if isinstance(v, str) else str(v) for v in self.context]

        super().__post_init__(**kwargs)


class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique to an individual or organization. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.IdentityAbstraction
    class_class_curie: ClassVar[str] = "core:IdentityAbstraction"
    class_name: ClassVar[str] = "IdentityAbstraction"
    class_model_uri: ClassVar[URIRef] = MARKING.IdentityAbstraction


class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Item
    class_class_curie: ClassVar[str] = "core:Item"
    class_name: ClassVar[str] = "Item"
    class_model_uri: ClassVar[URIRef] = MARKING.Item


class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to the expression of a specific data
    marking conveying restrictions, permissions, and other guidance for how marked data can be used and shared. This
    class is an ontological structural abstraction for this concept. Implementations of this concept should utilize
    the marking MarkingDefinition class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.MarkingDefinitionAbstraction
    class_class_curie: ClassVar[str] = "core:MarkingDefinitionAbstraction"
    class_name: ClassVar[str] = "MarkingDefinitionAbstraction"
    class_model_uri: ClassVar[URIRef] = MARKING.MarkingDefinitionAbstraction


@dataclass
class MarkingDefinition(MarkingDefinitionAbstraction):
    """
    A MarkingDefinition is a grouping of characteristics unique to the expression of a specific data marking conveying
    restrictions, permissions, and other guidance for how marked data can be used and shared.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MARKING.MarkingDefinition
    class_class_curie: ClassVar[str] = "marking:MarkingDefinition"
    class_name: ClassVar[str] = "MarkingDefinition"
    class_model_uri: ClassVar[URIRef] = MARKING.MarkingDefinition

    definitionType: str = None
    definition: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.definitionType):
            self.MissingRequiredField("definitionType")
        if not isinstance(self.definitionType, str):
            self.definitionType = str(self.definitionType)

        if not isinstance(self.definition, list):
            self.definition = [self.definition] if self.definition is not None else []
        self.definition = [v if isinstance(v, str) else str(v) for v in self.definition]

        super().__post_init__(**kwargs)


class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular entity behaves or the resources they use).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ModusOperandi
    class_class_curie: ClassVar[str] = "core:ModusOperandi"
    class_name: ClassVar[str] = "ModusOperandi"
    class_model_uri: ClassVar[URIRef] = MARKING.ModusOperandi


@dataclass
class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that one or more objects are related to
    another object in some way.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Relationship
    class_class_curie: ClassVar[str] = "core:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = MARKING.Relationship

    isDirectional: Union[bool, BooleanType] = None
    source: Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]] = None
    target: Union[dict, "UcoObject"] = None
    endTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()
    kindOfRelationship: Optional[str] = None
    startTime: Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.isDirectional):
            self.MissingRequiredField("isDirectional")
        if not isinstance(self.isDirectional, BooleanType):
            self.isDirectional = BooleanType(self.isDirectional)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, UcoObject) else UcoObject(**as_dict(v)) for v in self.source]

        if self._is_empty(self.target):
            self.MissingRequiredField("target")
        if not isinstance(self.target, UcoObject):
            self.target = UcoObject(**as_dict(self.target))

        if not isinstance(self.endTime, list):
            self.endTime = [self.endTime] if self.endTime is not None else []
        self.endTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.endTime]

        if self.kindOfRelationship is not None and not isinstance(self.kindOfRelationship, str):
            self.kindOfRelationship = str(self.kindOfRelationship)

        if not isinstance(self.startTime, list):
            self.startTime = [self.startTime] if self.startTime is not None else []
        self.startTime = [v if isinstance(v, XSDDateTime) else XSDDateTime(v) for v in self.startTime]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.authorizedIdentities = Slot(uri=MARKING.authorizedIdentities, name="authorizedIdentities", curie=MARKING.curie('authorizedIdentities'),
                   model_uri=MARKING.authorizedIdentities, domain=None, range=Optional[str])

slots.contentSelectors = Slot(uri=MARKING.contentSelectors, name="contentSelectors", curie=MARKING.curie('contentSelectors'),
                   model_uri=MARKING.contentSelectors, domain=None, range=Optional[str])

slots.definition = Slot(uri=MARKING.definition, name="definition", curie=MARKING.curie('definition'),
                   model_uri=MARKING.definition, domain=MarkingModel, range=Optional[str])

slots.definitionType = Slot(uri=MARKING.definitionType, name="definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MARKING.definitionType, domain=None, range=Optional[str])

slots.license = Slot(uri=MARKING.license, name="license", curie=MARKING.curie('license'),
                   model_uri=MARKING.license, domain=None, range=Optional[str])

slots.marking = Slot(uri=MARKING.marking, name="marking", curie=MARKING.curie('marking'),
                   model_uri=MARKING.marking, domain=MarkingDefinition, range=Optional[str])

slots.termsOfUse = Slot(uri=MARKING.termsOfUse, name="termsOfUse", curie=MARKING.curie('termsOfUse'),
                   model_uri=MARKING.termsOfUse, domain=None, range=Optional[str])

slots.confidence = Slot(uri=CORE.confidence, name="confidence", curie=CORE.curie('confidence'),
                   model_uri=MARKING.confidence, domain=None, range=Optional[Union[int, NonNegativeIntegerType]])

slots.constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=MARKING.constrainingVocabularyName, domain=None, range=Optional[str])

slots.constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=MARKING.constrainingVocabularyReference, domain=None, range=Optional[Union[str, IriType]])

slots.context = Slot(uri=CORE.context, name="context", curie=CORE.curie('context'),
                   model_uri=MARKING.context, domain=None, range=Optional[str])

slots.createdBy = Slot(uri=CORE.createdBy, name="createdBy", curie=CORE.curie('createdBy'),
                   model_uri=MARKING.createdBy, domain=IdentityAbstraction, range=Optional[str])

slots.definingContext = Slot(uri=CORE.definingContext, name="definingContext", curie=CORE.curie('definingContext'),
                   model_uri=MARKING.definingContext, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=MARKING.description, domain=None, range=Optional[str])

slots.endTime = Slot(uri=CORE.endTime, name="endTime", curie=CORE.curie('endTime'),
                   model_uri=MARKING.endTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.externalIdentifier = Slot(uri=CORE.externalIdentifier, name="externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=MARKING.externalIdentifier, domain=None, range=Optional[str])

slots.externalReference = Slot(uri=CORE.externalReference, name="externalReference", curie=CORE.curie('externalReference'),
                   model_uri=MARKING.externalReference, domain=ExternalReference, range=Optional[str])

slots.hasFacet = Slot(uri=CORE.hasFacet, name="hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=MARKING.hasFacet, domain=None, range=Optional[str])

slots.isDirectional = Slot(uri=CORE.isDirectional, name="isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=MARKING.isDirectional, domain=None, range=Optional[Union[bool, BooleanType]])

slots.kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=MARKING.kindOfRelationship, domain=None, range=Optional[str])

slots.modifiedTime = Slot(uri=CORE.modifiedTime, name="modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=MARKING.modifiedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=MARKING.name, domain=None, range=Optional[str])

slots.namingAuthority = Slot(uri=CORE.namingAuthority, name="namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=MARKING.namingAuthority, domain=None, range=Optional[str])

slots.object = Slot(uri=CORE.object, name="object", curie=CORE.curie('object'),
                   model_uri=MARKING.object, domain=None, range=Optional[Union[dict, UcoObject]])

slots.objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=MARKING.objectCreatedTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.objectMarking = Slot(uri=CORE.objectMarking, name="objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=MARKING.objectMarking, domain=None, range=Optional[Union[dict, MarkingDefinitionAbstraction]])

slots.referenceURL = Slot(uri=CORE.referenceURL, name="referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=MARKING.referenceURL, domain=None, range=Optional[Union[str, IriType]])

slots.source = Slot(uri=CORE.source, name="source", curie=CORE.curie('source'),
                   model_uri=MARKING.source, domain=None, range=Optional[Union[dict, UcoObject]])

slots.specVersion = Slot(uri=CORE.specVersion, name="specVersion", curie=CORE.curie('specVersion'),
                   model_uri=MARKING.specVersion, domain=None, range=Optional[str])

slots.startTime = Slot(uri=CORE.startTime, name="startTime", curie=CORE.curie('startTime'),
                   model_uri=MARKING.startTime, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.statement = Slot(uri=CORE.statement, name="statement", curie=CORE.curie('statement'),
                   model_uri=MARKING.statement, domain=None, range=Optional[str])

slots.tag = Slot(uri=CORE.tag, name="tag", curie=CORE.curie('tag'),
                   model_uri=MARKING.tag, domain=None, range=Optional[str])

slots.target = Slot(uri=CORE.target, name="target", curie=CORE.curie('target'),
                   model_uri=MARKING.target, domain=None, range=Optional[Union[dict, UcoObject]])

slots.value = Slot(uri=CORE.value, name="value", curie=CORE.curie('value'),
                   model_uri=MARKING.value, domain=None, range=Optional[str])

slots.GranularMarking_marking = Slot(uri=MARKING.marking, name="GranularMarking_marking", curie=MARKING.curie('marking'),
                   model_uri=MARKING.GranularMarking_marking, domain=GranularMarking, range=Optional[Union[str, List[str]]])

slots.GranularMarking_contentSelectors = Slot(uri=MARKING.contentSelectors, name="GranularMarking_contentSelectors", curie=MARKING.curie('contentSelectors'),
                   model_uri=MARKING.GranularMarking_contentSelectors, domain=GranularMarking, range=Optional[Union[str, List[str]]])

slots.LicenseMarking_definitionType = Slot(uri=MARKING.definitionType, name="LicenseMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MARKING.LicenseMarking_definitionType, domain=LicenseMarking, range=Optional[Union[str, List[str]]])

slots.LicenseMarking_license = Slot(uri=MARKING.license, name="LicenseMarking_license", curie=MARKING.curie('license'),
                   model_uri=MARKING.LicenseMarking_license, domain=LicenseMarking, range=str)

slots.MarkingDefinition_definition = Slot(uri=MARKING.definition, name="MarkingDefinition_definition", curie=MARKING.curie('definition'),
                   model_uri=MARKING.MarkingDefinition_definition, domain=MarkingDefinition, range=Optional[Union[str, List[str]]])

slots.MarkingDefinition_definitionType = Slot(uri=MARKING.definitionType, name="MarkingDefinition_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MARKING.MarkingDefinition_definitionType, domain=MarkingDefinition, range=str)

slots.ReleaseToMarking_definitionType = Slot(uri=MARKING.definitionType, name="ReleaseToMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MARKING.ReleaseToMarking_definitionType, domain=ReleaseToMarking, range=Optional[Union[str, List[str]]])

slots.ReleaseToMarking_authorizedIdentities = Slot(uri=MARKING.authorizedIdentities, name="ReleaseToMarking_authorizedIdentities", curie=MARKING.curie('authorizedIdentities'),
                   model_uri=MARKING.ReleaseToMarking_authorizedIdentities, domain=ReleaseToMarking, range=Union[str, List[str]])

slots.StatementMarking_definitionType = Slot(uri=MARKING.definitionType, name="StatementMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MARKING.StatementMarking_definitionType, domain=StatementMarking, range=Optional[Union[str, List[str]]])

slots.StatementMarking_statement = Slot(uri=CORE.statement, name="StatementMarking_statement", curie=CORE.curie('statement'),
                   model_uri=MARKING.StatementMarking_statement, domain=StatementMarking, range=str)

slots.TermsOfUseMarking_definitionType = Slot(uri=MARKING.definitionType, name="TermsOfUseMarking_definitionType", curie=MARKING.curie('definitionType'),
                   model_uri=MARKING.TermsOfUseMarking_definitionType, domain=TermsOfUseMarking, range=Optional[Union[str, List[str]]])

slots.TermsOfUseMarking_termsOfUse = Slot(uri=MARKING.termsOfUse, name="TermsOfUseMarking_termsOfUse", curie=MARKING.curie('termsOfUse'),
                   model_uri=MARKING.TermsOfUseMarking_termsOfUse, domain=TermsOfUseMarking, range=str)

slots.Annotation_object = Slot(uri=CORE.object, name="Annotation_object", curie=CORE.curie('object'),
                   model_uri=MARKING.Annotation_object, domain=Annotation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Assertion_statement = Slot(uri=CORE.statement, name="Assertion_statement", curie=CORE.curie('statement'),
                   model_uri=MARKING.Assertion_statement, domain=Assertion, range=Optional[Union[str, List[str]]])

slots.AttributedName_namingAuthority = Slot(uri=CORE.namingAuthority, name="AttributedName_namingAuthority", curie=CORE.curie('namingAuthority'),
                   model_uri=MARKING.AttributedName_namingAuthority, domain=AttributedName, range=Optional[str])

slots.ConfidenceFacet_confidence = Slot(uri=CORE.confidence, name="ConfidenceFacet_confidence", curie=CORE.curie('confidence'),
                   model_uri=MARKING.ConfidenceFacet_confidence, domain=ConfidenceFacet, range=Union[int, NonNegativeIntegerType])

slots.ContextualCompilation_object = Slot(uri=CORE.object, name="ContextualCompilation_object", curie=CORE.curie('object'),
                   model_uri=MARKING.ContextualCompilation_object, domain=ContextualCompilation, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.ControlledVocabulary_constrainingVocabularyReference = Slot(uri=CORE.constrainingVocabularyReference, name="ControlledVocabulary_constrainingVocabularyReference", curie=CORE.curie('constrainingVocabularyReference'),
                   model_uri=MARKING.ControlledVocabulary_constrainingVocabularyReference, domain=ControlledVocabulary, range=Optional[Union[str, IriType]])

slots.ControlledVocabulary_constrainingVocabularyName = Slot(uri=CORE.constrainingVocabularyName, name="ControlledVocabulary_constrainingVocabularyName", curie=CORE.curie('constrainingVocabularyName'),
                   model_uri=MARKING.ControlledVocabulary_constrainingVocabularyName, domain=ControlledVocabulary, range=Optional[str])

slots.ControlledVocabulary_value = Slot(uri=CORE.value, name="ControlledVocabulary_value", curie=CORE.curie('value'),
                   model_uri=MARKING.ControlledVocabulary_value, domain=ControlledVocabulary, range=str)

slots.EnclosingCompilation_object = Slot(uri=CORE.object, name="EnclosingCompilation_object", curie=CORE.curie('object'),
                   model_uri=MARKING.EnclosingCompilation_object, domain=EnclosingCompilation, range=Optional[Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]]])

slots.ExternalReference_referenceURL = Slot(uri=CORE.referenceURL, name="ExternalReference_referenceURL", curie=CORE.curie('referenceURL'),
                   model_uri=MARKING.ExternalReference_referenceURL, domain=ExternalReference, range=Optional[Union[str, IriType]])

slots.ExternalReference_definingContext = Slot(uri=CORE.definingContext, name="ExternalReference_definingContext", curie=CORE.curie('definingContext'),
                   model_uri=MARKING.ExternalReference_definingContext, domain=ExternalReference, range=Optional[str])

slots.ExternalReference_externalIdentifier = Slot(uri=CORE.externalIdentifier, name="ExternalReference_externalIdentifier", curie=CORE.curie('externalIdentifier'),
                   model_uri=MARKING.ExternalReference_externalIdentifier, domain=ExternalReference, range=Optional[str])

slots.Grouping_context = Slot(uri=CORE.context, name="Grouping_context", curie=CORE.curie('context'),
                   model_uri=MARKING.Grouping_context, domain=Grouping, range=Optional[Union[str, List[str]]])

slots.Relationship_endTime = Slot(uri=CORE.endTime, name="Relationship_endTime", curie=CORE.curie('endTime'),
                   model_uri=MARKING.Relationship_endTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.Relationship_isDirectional = Slot(uri=CORE.isDirectional, name="Relationship_isDirectional", curie=CORE.curie('isDirectional'),
                   model_uri=MARKING.Relationship_isDirectional, domain=Relationship, range=Union[bool, BooleanType])

slots.Relationship_kindOfRelationship = Slot(uri=CORE.kindOfRelationship, name="Relationship_kindOfRelationship", curie=CORE.curie('kindOfRelationship'),
                   model_uri=MARKING.Relationship_kindOfRelationship, domain=Relationship, range=Optional[str])

slots.Relationship_target = Slot(uri=CORE.target, name="Relationship_target", curie=CORE.curie('target'),
                   model_uri=MARKING.Relationship_target, domain=Relationship, range=Union[dict, "UcoObject"])

slots.Relationship_source = Slot(uri=CORE.source, name="Relationship_source", curie=CORE.curie('source'),
                   model_uri=MARKING.Relationship_source, domain=Relationship, range=Union[Union[dict, "UcoObject"], List[Union[dict, "UcoObject"]]])

slots.Relationship_startTime = Slot(uri=CORE.startTime, name="Relationship_startTime", curie=CORE.curie('startTime'),
                   model_uri=MARKING.Relationship_startTime, domain=Relationship, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_description = Slot(uri=DCTERMS.description, name="UcoObject_description", curie=DCTERMS.curie('description'),
                   model_uri=MARKING.UcoObject_description, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_createdBy = Slot(uri=CORE.createdBy, name="UcoObject_createdBy", curie=CORE.curie('createdBy'),
                   model_uri=MARKING.UcoObject_createdBy, domain=UcoObject, range=Optional[str])

slots.UcoObject_externalReference = Slot(uri=CORE.externalReference, name="UcoObject_externalReference", curie=CORE.curie('externalReference'),
                   model_uri=MARKING.UcoObject_externalReference, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_hasFacet = Slot(uri=CORE.hasFacet, name="UcoObject_hasFacet", curie=CORE.curie('hasFacet'),
                   model_uri=MARKING.UcoObject_hasFacet, domain=UcoObject, range=Optional[Union[str, List[str]]])

slots.UcoObject_modifiedTime = Slot(uri=CORE.modifiedTime, name="UcoObject_modifiedTime", curie=CORE.curie('modifiedTime'),
                   model_uri=MARKING.UcoObject_modifiedTime, domain=UcoObject, range=Optional[Union[Union[str, XSDDateTime], List[Union[str, XSDDateTime]]]])

slots.UcoObject_name = Slot(uri=RDFS.label, name="UcoObject_name", curie=RDFS.curie('label'),
                   model_uri=MARKING.UcoObject_name, domain=UcoObject, range=Optional[str])

slots.UcoObject_objectCreatedTime = Slot(uri=CORE.objectCreatedTime, name="UcoObject_objectCreatedTime", curie=CORE.curie('objectCreatedTime'),
                   model_uri=MARKING.UcoObject_objectCreatedTime, domain=UcoObject, range=Optional[Union[str, XSDDateTime]])

slots.UcoObject_objectMarking = Slot(uri=CORE.objectMarking, name="UcoObject_objectMarking", curie=CORE.curie('objectMarking'),
                   model_uri=MARKING.UcoObject_objectMarking, domain=UcoObject, range=Optional[Union[Union[dict, MarkingDefinitionAbstraction], List[Union[dict, MarkingDefinitionAbstraction]]]])

slots.UcoObject_specVersion = Slot(uri=CORE.specVersion, name="UcoObject_specVersion", curie=CORE.curie('specVersion'),
                   model_uri=MARKING.UcoObject_specVersion, domain=UcoObject, range=Optional[str])

slots.UcoObject_tag = Slot(uri=CORE.tag, name="UcoObject_tag", curie=CORE.curie('tag'),
                   model_uri=MARKING.UcoObject_tag, domain=UcoObject, range=Optional[Union[str, List[str]]])