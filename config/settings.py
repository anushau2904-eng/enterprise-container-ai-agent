from pathlib import Path

# Project Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DATABASE_PATH = BASE_DIR / "database" / "container_management.db"

# Knowledge Base
KNOWLEDGE_BASE_PATH = BASE_DIR / "knowledge_base"

# ChromaDB
CHROMA_DB_PATH = BASE_DIR / "chroma_db"

# Ollama
OLLAMA_MODEL = "llama3.2:3b"

# Application
APP_NAME = "Enterprise Container Management AI Agent"
APP_VERSION = "1.0.0"