from app.document_loader import load_document
from app.text_splitter import split_document
from app.vector_store import create_vector_store


def get_retriever():
    content = load_document("container_manual.txt")

    chunks = split_document(content)

    vector_store = create_vector_store(chunks)

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

    return retriever