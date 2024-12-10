from pydantic import UUID4, Field

from llm_engineering.domain.base import VectorBaseDocument
from llm_engineering.domain.types import DataCategory


class Query(VectorBaseDocument):
    content: str
    source_id: UUID4 | None = None
    title: str | None = None
    metadata: dict = Field(default_factory=dict)

    class Config:
        category = DataCategory.QUERIES

    @classmethod
    def from_str(cls, query: str) -> "Query":
        return Query(content=query.strip("\n "))

    def replace_content(self, new_content: str) -> "Query":
        return Query(
            id=self.id,
            content=new_content,
            source_id=self.source_id,
            title=self.title,
            metadata=self.metadata,
        )


class EmbeddedQuery(Query):
    embedding: list[float]

    class Config:
        category = DataCategory.QUERIES
