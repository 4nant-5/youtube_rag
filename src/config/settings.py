from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
# Project Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
VIDEOS_DIR = DATA_DIR / "videos"
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"
FRAMES_DIR = DATA_DIR / "frames"

CHROMA_DB_PATH = Path(
    os.getenv("CHROMA_DB_PATH", str(DATA_DIR / "chroma_db"))
)

WHOOSH_INDEX_PATH = Path(
    os.getenv("WHOOSH_INDEX_PATH", str(DATA_DIR / "whoosh_index"))
)

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "youtube_rag")

# Models
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "BAAI/bge-large-en-v1.5"
)

DEVICE = os.getenv("DEVICE", "cpu")

RERANKER_MODEL = os.getenv(
    "RERANKER_MODEL",
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen3:8b"
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)

VISION_MODEL = os.getenv(
    "VISION_MODEL",
    "Qwen/Qwen2.5-VL-7B-Instruct"
)

# Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

# Video Processing
FRAME_INTERVAL = int(os.getenv("FRAME_INTERVAL", 5))

# Retrieval
TOP_K = int(os.getenv("TOP_K", 10))
FINAL_K = int(os.getenv("FINAL_K", 5))