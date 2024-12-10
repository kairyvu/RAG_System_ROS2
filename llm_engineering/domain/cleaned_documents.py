from abc import ABC

from pydantic import UUID4

from llm_engineering.domain.types import DataCategory

from .base import VectorBaseDocument


class CleanedDocument(VectorBaseDocument, ABC):
    content: str
    platform: str
    source_id: UUID4
    title: str


class CleanedRepositoryDocument(CleanedDocument):
    name: str
    link: str

    class Config:
        name = "cleaned_repositories"
        category = DataCategory.REPOSITORIES
        use_vector_index = False
