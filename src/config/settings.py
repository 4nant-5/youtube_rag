from pathlib import Path
# Project Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
VIDEOS_DIR = DATA_DIR / "videos"
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"
FRAMES_DIR = DATA_DIR / "frames"
CHROMA_DB_PATH = DATA_DIR / "chroma_db"
COLLECTION_NAME = "youtube_rag"
# Models
EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
DEVICE = "cpu"
RERANKER_MODEL = "BAAI/bge-reranker-large"
LLM_MODEL = "Qwen/Qwen2.5-7B-Instruct"
VISION_MODEL = "Qwen/Qwen2.5-VL-7B-Instruct"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
# Video Processing
FRAME_INTERVAL = 5
# Retrieval
TOP_K = 10
FINAL_K = 5