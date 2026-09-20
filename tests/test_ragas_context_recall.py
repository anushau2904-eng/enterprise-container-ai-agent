from tests.testdata.rag_dataset import evaluation_data

from app.retriever import get_retriever

from ragas import evaluate
from ragas.dataset_schema import EvaluationDataset, SingleTurnSample
from ragas.metrics import ContextRecall

from langchain_ollama import ChatOllama
from ragas.llms import LangchainLLMWrapper


def test_ragas_context_recall():

    retriever = get_retriever()

    samples = []

    for item in evaluation_data:

        question = item["question"]

        documents = retriever.invoke(question)

        context = [
            document.page_content
            for document in documents
        ]

        print("\n================================")
        print("Question:", question)
        print("Retrieved Context:", context)
        print("Ground Truth:", item["ground_truth"])

        sample = SingleTurnSample(
            user_input=question,
            retrieved_contexts=context,
            reference=item["ground_truth"]
        )

        samples.append(sample)

    dataset = EvaluationDataset(samples=samples)

    evaluator_model = ChatOllama(
        model="qwen2.5:7b",
        temperature=0
    )

    evaluator_llm = LangchainLLMWrapper(evaluator_model)

    context_recall = ContextRecall(
        llm=evaluator_llm
    )

    result = evaluate(
        dataset=dataset,
        metrics=[context_recall]
    )

    print("\n================================")
    print("RAGAS CONTEXT RECALL RESULT")
    print("================================")
    print(result)

    assert result is not None