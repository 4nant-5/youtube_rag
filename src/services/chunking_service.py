from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:
    """Service responsible for splitting LangChain Documents."""

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(self, documents):

        chunks = self.text_splitter.split_documents(documents)

        for index, chunk in enumerate(chunks):

            video_id = chunk.metadata["video_id"]

            chunk.metadata["chunk_id"] = f"{video_id}_{index}"

        return chunks