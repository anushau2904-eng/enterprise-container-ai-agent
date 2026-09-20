from app.retriever import get_retriever
from app.llm import generate_answer


def ask_question(question):
    retriever = get_retriever()

    documents = retriever.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    answer = generate_answer(question, context)

    return answer