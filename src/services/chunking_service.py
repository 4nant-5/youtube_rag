from langchain_text_splitters import RecursiveCharacterTextSplitter


class ChunkService:
    """Service responsible for splitting LangChain documents."""

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(self, document):

        return self.text_splitter.split_documents([document])