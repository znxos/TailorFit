from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# ---------------------------------------------------------------------------
# API key schemas
# ---------------------------------------------------------------------------
# Added for GitHub Issue #40: "API Parameters - 4".
# These schemas support future API-key validation endpoints by defining:
# - APIKeyCreate: request body containing the API key string.
# - APIKeyResponse: response body showing whether the key is valid and
#   which AI provider it belongs to.
# This is a schema-only change and does not modify existing routes or logic.


class APIKeyCreate(BaseModel):
    key_string: str = Field(
        ...,
        min_length=1,
        max_length=256,
        description="The API Key string",
    )


class APIKeyResponse(BaseModel):
    is_valid: bool = Field(
        ...,
        description="Whether the API key is currently validated",
    )
    provider: str = Field(
        default="Unknown",
        description="The AI Provider",
    )

    
class CoverLetterCreate(BaseModel):
    content: str = Field(..., min_length=1, description="Cover letter content")
    status: str = Field(default="draft", description="Status: draft or finalized")
    template_version: str = Field(default="1.0", description="Template version")

class CoverLetterUpdate(BaseModel):
    content: str = Field(..., min_length=1, description="Updated content")

class CoverLetterResponse(BaseModel):
    id: str
    content: str
    status: str
    template_version: str

class JobDescriptionCreate(BaseModel):
    text: str = Field(..., min_length=1, description="Job description text")

class JobDescriptionUpdate(BaseModel):
    text: str = Field(..., min_length=1, description="Updated job description")

class JobDescriptionResponse(BaseModel):
    id: str
    text: str

class ResumeCreate(BaseModel):
    text: str = Field(..., min_length=1, max_length=6000, description="Resume content")

class ResumeUpdate(BaseModel):
    text: str = Field(..., min_length=1, max_length=6000, description="Updated resume content")

class ResumeResponse(BaseModel):
    id: str
    text: str

class SystemLogResponse(BaseModel):
    id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    status: int
    latency: float
    error_type: Optional[str] = None
