from loguru import logger
from typing_extensions import Annotated
from zenml import get_step_context, step

from llm_engineering.domain.documents import RepoInfoDocument


@step
def get_or_create_subdomain(title: str) -> Annotated[RepoInfoDocument, "subdomains"]:
    logger.info(f"Getting or creating: {title}")

    repo = RepoInfoDocument.get_or_create(title=title)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="subdomains", metadata=_get_metadata(repo))

    return repo


def _get_metadata(repo: RepoInfoDocument) -> dict:
    return {
        "query": {
            "title": repo.title,
        },
        "retrieved": {"title": repo.title, "source_id": str(repo.id)},
    }
