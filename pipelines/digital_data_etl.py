from zenml import pipeline

from steps.etl import crawl_links, get_or_create_subdomain


@pipeline
def digital_data_etl(title: str, links: list[str]) -> str:
    subdomain = get_or_create_subdomain(title)
    last_step = crawl_links(repo=subdomain, links=links)

    return last_step.invocation_id
