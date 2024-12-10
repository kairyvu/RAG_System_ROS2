from concurrent.futures import ThreadPoolExecutor, as_completed

from loguru import logger
from typing_extensions import Annotated
from zenml import get_step_context, step

from llm_engineering.domain.base.nosql import NoSQLBaseDocument
from llm_engineering.domain.documents import Document, RepoInfoDocument, RepositoryDocument


@step
def query_data_warehouse(
    titles: list[str],
) -> Annotated[list, "raw_documents"]:
    documents = []
    for title in titles:
        logger.info(f"Querying data warehouse for {title} subdomain")

        profile = RepoInfoDocument.get_or_create(title=title)

        results = fetch_all_data(profile)
        repo_documents = [doc for query_result in results.values() for doc in query_result]

        documents.extend(repo_documents)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="raw_documents", metadata=_get_metadata(documents))

    return documents


def fetch_all_data(doc: RepoInfoDocument) -> dict[str, list[NoSQLBaseDocument]]:
    source_id = str(doc.id)
    with ThreadPoolExecutor() as executor:
        future_to_query = {
            executor.submit(__fetch_repositories, source_id): "repositories",
        }

        results = {}
        for future in as_completed(future_to_query):
            query_name = future_to_query[future]
            try:
                results[query_name] = future.result()
            except Exception:
                logger.exception(f"'{query_name}' request failed.")

                results[query_name] = []

    return results


def __fetch_repositories(source_id) -> list[NoSQLBaseDocument]:
    return RepositoryDocument.bulk_find(source_id=source_id)


def _get_metadata(documents: list[Document]) -> dict:
    metadata = {
        "num_documents": len(documents),
    }
    for document in documents:
        collection = document.get_collection_name()
        if collection not in metadata:
            metadata[collection] = {}
        if "titles" not in metadata[collection]:
            metadata[collection]["titles"] = list()

        metadata[collection]["num_documents"] = metadata[collection].get("num_documents", 0) + 1
        metadata[collection]["titles"].append(document.title)

    for value in metadata.values():
        if isinstance(value, dict) and "titles" in value:
            value["titles"] = list(set(value["titles"]))

    return metadata
