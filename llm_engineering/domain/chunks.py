from abc import ABC

from pydantic import UUID4, Field

from llm_engineering.domain.types import DataCategory

from .base import VectorBaseDocument


class Chunk(VectorBaseDocument, ABC):
    content: str
    platform: str
    document_id: UUID4
    source_id: UUID4
    metadata: dict = Field(default_factory=dict)
    title: str


class RepositoryChunk(Chunk):
    name: str
    link: str

    class Config:
        category = DataCategory.REPOSITORIES
