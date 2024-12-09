from loguru import logger
from typing_extensions import Annotated
from zenml import get_step_context, step

from llm_engineering.domain.documents import RepoInfoDocument


@step
def get_or_create_repo(link: str) -> Annotated[RepoInfoDocument, "subdomains"]:
    repo_name = link.rstrip("/").split("/")[-1]

    logger.info(f"Getting or creating: {repo_name}")

    repo = RepoInfoDocument.get_or_create(link=link, title=repo_name)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="repo", metadata=_get_metadata(link, repo))

    return repo


def _get_metadata(repo: RepoInfoDocument) -> dict:
    return {
        "query": {
            "link": repo.link,
        },
        "retrieved": {"link": repo.link, "title": repo.title, "source_id": repo.id},
    }
