from app.retriever import get_retriever


def test_retrieve_relevant_chunks():
    retriever = get_retriever()

    question = "What is the recommended temperature for frozen cargo?"

    documents = retriever.invoke(question)

    print("\nRetrieved documents:")

    for document in documents:
        print("\n---")
        print(document.page_content)

    assert len(documents) > 0