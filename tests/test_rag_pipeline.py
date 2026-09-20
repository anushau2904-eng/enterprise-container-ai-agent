from app.rag_pipeline import ask_question


def test_rag_pipeline():

    question = "What is the recommended temperature for frozen cargo?"

    answer = ask_question(question)

    print("\nRAG Answer:")
    print(answer)

    assert answer is not None
    assert answer.strip() != ""
    assert "-18°C" in answer