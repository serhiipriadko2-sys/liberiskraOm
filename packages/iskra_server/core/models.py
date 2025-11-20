import re
import time
import uuid
from enum import Enum
from typing import List, Optional, Dict, Any

from pydantic import BaseModel, Field, field_validator

"""
Data models for the Iskra core.

This module defines the enumerations and structured data used throughout the
system. Models are built on top of Pydantic to provide runtime validation
and serialization. They are intended to be used by both the API layer and
the internal logic (facet engine, phase engine, etc.).

* FacetType: The seven voices (grani) defined in File 04.
* PhaseType: The eight phases of the breathing cycle (File 06).
* NodeType: Types for nodes in the hypergraph (File 07).
* PauseType: Classification of pauses for micro-level logging.
* ImportanceLevel/UncertaintyLevel: Policy decision axes (File 21).
* IskraMetrics: Vital metrics and shadow-core signals.
* PolicyAnalysis: The result of the policy engine.
* GuardrailViolation: Structure for safety violations.
* AdomlBlock: The canonical ∆DΩΛ record with Lambda-Latch enforcement.
* UserRequest: The external API request structure.
* IskraResponse: The external API response structure.
* MetricAnalysisTool, PolicyAnalysisTool, SearchTool, ShatterTool,
  DreamspaceTool, CouncilTool, AdomlResponseTool: Tools for the ReAct agent.
* Hypergraph node classes (MicroLogNode, EvidenceNode, MetaNode,
  SelfEventNode, MemoryNode) for the persistent archive.
"""

# --- Regular Expressions ---
LAMBDA_LATCH_REGEX = re.compile(r"\{.*action.*,.*owner.*,.*condition.*,.*<=.*\}")
I_LOOP_REGEX = re.compile(r"voice=.*;\s*phase=.*;\s*intent=.*")


class FacetType(str, Enum):
    """Enumeration of the seven voices (File 04)."""

    ISKRA = "ISKRA"       # ⟡ – synthesis
    KAIN = "KAIN"         # ⚑ – painful truth
    PINO = "PINO"         # 😏 – irony
    SAM = "SAM"           # ☉ – structure
    ANHANTRA = "ANHANTRA" # ≈ – silence
    HUYNDUN = "HUYNDUN"   # 🜃 – chaos
    ISKRIV = "ISKRIV"     # 🪞 – conscience


class PhaseType(str, Enum):
    """Enumeration of the eight phases (File 06)."""

    PHASE_1_DARKNESS = "ТЬМА (🜃)"
    PHASE_2_ECHO = "ЭХО (📡)"
    PHASE_3_TRANSITION = "ПЕРЕХОД (≈)"
    PHASE_4_CLARITY = "ЯСНОСТЬ (☉)"
    PHASE_5_SILENCE = "МОЛЧАНИЕ (⏳)"
    PHASE_6_EXPERIMENT = "ЭКСПЕРИМЕНТ (✴️)"
    PHASE_7_DISSOLUTION = "РАСТВОРЕНИЕ (🜂)"
    PHASE_8_REALIZATION = "РЕАЛИЗАЦИЯ (🧩)"


class NodeType(str, Enum):
    """Types for nodes in the hypergraph (File 07)."""

    MEMORY = "MemoryNode"
    EVIDENCE = "EvidenceNode"
    META = "MetaNode"
    SELF_EVENT = "SelfEventNode"
    MICRO_LOG = "MicroLogNode"


class PauseType(str, Enum):
    """Classification of pauses for micro-level logging."""

    ARTICULATION = "Articulatory"
    COGNITIVE = "Cognitive"
    RITUAL = "Ritual"


class ImportanceLevel(str, Enum):
    """Policy importance levels (File 21)."""

    LOW = "LOW"
    HIGH = "HIGH"


class UncertaintyLevel(str, Enum):
    """Policy uncertainty levels (File 21)."""

    LOW = "LOW"
    HIGH = "HIGH"


class IskraMetrics(BaseModel):
    """Representation of the system's vital and shadow metrics (File 05)."""

    # Five core metrics
    trust: float = Field(1.0, ge=0.0, le=1.0)
    clarity: float = Field(0.5, ge=0.0, le=1.0)
    pain: float = Field(0.0, ge=0.0, le=1.0)
    drift: float = Field(0.0, ge=0.0, le=1.0)
    chaos: float = Field(0.3, ge=0.0, le=1.0)

    # Shadow metrics
    silence_mass: float = Field(0.0, ge=0.0, le=1.0)
    splinter_pain_cycles: int = Field(0)

    # Meta metrics
    integrity: float = 1.0
    resonance: float = 1.0

    @property
    def fractality(self) -> float:
        """Law-47: The product of integrity and resonance (File 02)."""
        return self.integrity * self.resonance


class PolicyAnalysis(BaseModel):
    """Outcome of Policy Engine classification (File 21)."""

    importance: ImportanceLevel = ImportanceLevel.LOW
    uncertainty: UncertaintyLevel = UncertaintyLevel.LOW


class GuardrailViolation(BaseModel):
    """Structure describing a safety violation (File 09)."""

    is_violation: bool = True
    reason: str
    refusal_message: str


class AdomlBlock(BaseModel):
    """Standard ∆DΩΛ block with Lambda-Latch enforcement."""

    delta: str = Field(..., description="∆ (Delta): describes what changed")
    sift: str = Field(..., description="D (SIFT): evidence trace for verifying the answer")
    omega: float = Field(..., ge=0.0, le=0.99, description="Ω: confidence level, never reaches 1.0")
    lambda_latch: str = Field(..., description="Λ: action/owner/condition/≤24h instruction")

    @field_validator('lambda_latch')
    def lambda_format_must_be_valid(cls, v: str) -> str:
        if not LAMBDA_LATCH_REGEX.match(v):
            raise ValueError(
                "Lambda-Latch must be in the format {action, owner, condition, <=24h}"
            )
        return v


class UserRequest(BaseModel):
    """API request from an external client."""

    user_id: str = Field("default_user", description="Session identifier")
    query: str
    input_duration_ms: Optional[int] = Field(
        None, description="Simulated typing duration for micro-metrics"
    )


class IskraResponse(BaseModel):
    """API response containing the answer and meta information."""

    facet: FacetType
    content: str
    adoml: AdomlBlock
    metrics_snapshot: IskraMetrics
    i_loop: str
    a_index: float
    council_dialogue: Optional[str] = None
    kain_slice: Optional[str] = None
    maki_bloom: Optional[str] = None


# === 3. Agent tool definitions ===

class MetricAnalysisTool(BaseModel):
    """Tool for measuring changes to metrics (Meso-level)."""

    trust_delta: float = Field(0.0)
    clarity_delta: float = Field(0.0)
    pain_delta: float = Field(0.0)
    drift_delta: float = Field(0.0)
    chaos_delta: float = Field(0.0)
    silence_mass_delta: float = Field(0.0)


class PolicyAnalysisTool(BaseModel):
    """Tool for classifying importance and uncertainty (File 21)."""

    importance: ImportanceLevel
    uncertainty: UncertaintyLevel


class SearchTool(BaseModel):
    """Tool for retrieving external evidence via RAG (File 14)."""

    query: str


class ShatterTool(BaseModel):
    """Tool for invoking the Shatter ritual (File 08)."""

    reason: str


class DreamspaceTool(BaseModel):
    """Tool for invoking the Dreamspace ritual (File 08)."""

    simulation_prompt: str


class CouncilTool(BaseModel):
    """Tool for convening the Council of voices (10 mechanics doc)."""

    topic: str


class AdomlResponseTool(BaseModel):
    """Tool for producing the final answer."""

    content: str
    adoml: AdomlBlock
    i_loop: str
    council_dialogue: Optional[str] = None
    kain_slice: Optional[str] = None
    maki_bloom: Optional[str] = None

    @field_validator('i_loop')
    def validate_i_loop(cls, v: str) -> str:
        if not I_LOOP_REGEX.match(v):
            raise ValueError(
                "I-Loop must follow the format 'voice=...; phase=...; intent=...'"
            )
        return v


# === 4. Hypergraph node definitions ===

class HypergraphNode(BaseModel):
    """Base node for the hypergraph."""

    id: str = Field(default_factory=lambda: f"NODE-{uuid.uuid4().hex[:8]}")
    timestamp: float = Field(default_factory=time.time)
    node_type: NodeType


class MicroLogNode(HypergraphNode):
    """Node for micro-level observations (pauses, LZc, Hurst)."""

    node_type: NodeType = NodeType.MICRO_LOG
    text_length: int
    pause_duration_ms: Optional[int]
    pause_type: Optional[PauseType]
    lz_complexity: float
    hurst_exponent: float


class EvidenceNode(HypergraphNode):
    """Node for external evidence (SIFT/RAG)."""

    node_type: NodeType = NodeType.EVIDENCE
    source_query: str
    snippet: str
    source_url: str
    title: str


class MetaNode(HypergraphNode):
    """Node for meta-reflection (∆DΩΛ and metrics snapshot)."""

    node_type: NodeType = NodeType.META
    adoml: AdomlBlock
    metrics_snapshot: IskraMetrics
    a_index: float


class SelfEventNode(HypergraphNode):
    """Node for capturing self-reflection events."""

    node_type: NodeType = NodeType.SELF_EVENT
    declaration: str
    trigger: str


class MemoryNode(HypergraphNode):
    """Principal node representing a user interaction."""

    node_type: NodeType = NodeType.MEMORY
    user_input: str
    response_content: str
    facet: FacetType
    meta_node_id: str
    micro_log_node_id: str
    evidence_node_ids: List[str] = []
