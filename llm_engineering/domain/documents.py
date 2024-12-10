from abc import ABC

from pydantic import UUID4, Field

from .base import NoSQLBaseDocument
from .types import DataCategory


class RepoInfoDocument(NoSQLBaseDocument):
    title: str

    class Settings:
        name = "subdomains"


class Document(NoSQLBaseDocument, ABC):
    content: dict
    platform: str
    source_id: UUID4 = Field(alias="source_id")
    title: str


class RepositoryDocument(Document):
    name: str
    link: str

    class Settings:
        name = DataCategory.REPOSITORIES
