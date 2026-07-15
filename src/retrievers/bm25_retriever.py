from langchain_core.documents import Document

from src.services.whoosh_service import WhooshService


class BM25Retriever:
    """
    Lexical retriever backed by Whoosh.
    """

    def __init__(self, whoosh_service: WhooshService):

        self.whoosh_service = whoosh_service

    def retrieve(
    self,
    query: str,
    video_id: str,
    k: int = 5,
):

        return self.whoosh_service.search(
    query=query,
    video_id=video_id,
    limit=k,
)