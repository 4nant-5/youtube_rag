from pathlib import Path
from langchain_core.documents import Document
from whoosh.qparser import QueryParser
from whoosh.query import Term
from whoosh.fields import (
    Schema,
    ID,
    TEXT,
    NUMERIC,
)

from whoosh.index import (
    create_in,
    open_dir,
    exists_in,
)


class WhooshService:

    schema = Schema(

        chunk_id=ID(stored=True, unique=True),

        video_id=ID(stored=True),

        content=TEXT(stored=True),

        start_time=NUMERIC(stored=True),

        end_time=NUMERIC(stored=True),

    )

    def add_documents(self,documents: list[Document],):

        writer = self.index.writer()

        for i, document in enumerate(documents):

            metadata = document.metadata

            chunk_id = metadata["chunk_id"]

            writer.add_document(

                chunk_id=metadata["chunk_id"],

                video_id=metadata["video_id"],

                content=document.page_content,

                start_time=metadata["start_time"],

                end_time=metadata["end_time"],
            )

        writer.commit()

    def search(
        self,
        query: str,
        video_id: str | None = None,
        limit: int = 5,
    ):

        parser = QueryParser(
            "content",
            schema=self.index.schema,
        )

        parsed_query = parser.parse(query)

        if video_id:

            parsed_query = parsed_query & Term(
                "video_id",
                video_id,
            )

        documents = []

        with self.index.searcher() as searcher:

            results = searcher.search(
                parsed_query,
                limit=limit,
            )

            for result in results:

                documents.append(

                    Document(

                        page_content=result["content"],

                        metadata={

                            "chunk_id": result["chunk_id"],

                            "video_id": result["video_id"],

                            "start_time": result["start_time"],

                            "end_time": result["end_time"],

                        },

                    )

                )

        return documents

    def __init__(self):

        self.index_path = Path("data/whoosh")

        self.index_path.mkdir(
            parents=True,
            exist_ok=True,
        )

        if exists_in(self.index_path):

            self.index = open_dir(self.index_path)

        else:

            self.index = create_in(
                self.index_path,
                self.schema,
            )