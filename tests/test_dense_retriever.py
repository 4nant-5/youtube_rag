import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.youtube_service import YouTubeService
from src.services.transcript_service import TranscriptService
from src.services.document_service import DocumentService
from src.services.chunking_service import ChunkService
from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService
from src.retrievers.dense_retriever import DenseRetriever


def main():

    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    video_id = YouTubeService.extract_video_id(url)

    transcript_data = TranscriptService.get_transcript(video_id)

    transcript = transcript_data["transcript"]

    document = DocumentService.transcript_to_document(
        transcript,
        video_id,
    )

    chunk_service = ChunkService()

    chunks = chunk_service.split_documents(document)

    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )

    # Prevent duplicate inserts later—we'll improve this soon
    chroma_service.add_documents(chunks)

    retriever = DenseRetriever(chroma_service)

    results = retriever.retrieve(
    query="What is this video about?",
    video_id=video_id,
    )

    print("=" * 80)

    print(f"Retrieved {len(results)} chunks")

    print("=" * 80)

    for i, doc in enumerate(results, start=1):

        print(f"\nChunk {i}")

        print("-" * 40)

        print(doc.page_content[:500])

        print()

if __name__ == "__main__":
    main()