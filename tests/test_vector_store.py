from app.document_loader import load_document
from app.text_splitter import split_document
from app.vector_store import create_vector_store


def test_create_vector_store():
    content = load_document("container_manual.txt")

    chunks = split_document(content)

    vector_store = create_vector_store(chunks)

    assert vector_store is not None

    print("\nChunks stored in ChromaDB:", len(chunks))