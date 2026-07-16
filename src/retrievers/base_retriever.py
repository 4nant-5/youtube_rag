from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseRetriever(ABC):
    """
    Base class for all retrievers in the project.
    Every retriever must implement the retrieve() method.
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
        video_id: str,
        k: int = 5,
    ) -> list[Document]:
        """
        Retrieve the top-k relevant documents.

        Parameters
        ----------
        query : str
            User's question.

        video_id : str
            Restrict retrieval to a specific YouTube video.

        k : int
            Number of documents to retrieve.

        Returns
        -------
        list[Document]
            Retrieved LangChain documents.
        """

        raise NotImplementedError(
            "Subclasses must implement retrieve()."
        )