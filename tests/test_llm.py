from app.llm import generate_answer


def test_generate_answer():

    question = "What is the recommended temperature for frozen cargo?"

    context = """
    Reefer containers are temperature-controlled containers.

    For frozen cargo, the recommended operating temperature is -18°C.
    """

    answer = generate_answer(question, context)

    print("\nLLM Answer:")
    print(answer)

    assert answer is not None
    assert len(answer) > 0