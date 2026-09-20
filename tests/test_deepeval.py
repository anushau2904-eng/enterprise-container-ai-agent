from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval.models import OllamaModel

from tests.testdata.rag_dataset import evaluation_data
from app.rag_pipeline import ask_question


def test_deepeval_answer_relevancy():

    test_cases = []

    for item in evaluation_data:

        question = item["question"]

        actual_answer = ask_question(question)

        test_case = LLMTestCase(
            input=question,
            actual_output=actual_answer,
            expected_output=item["ground_truth"]
        )

        test_cases.append(test_case)

    evaluator_model = OllamaModel(
        model="qwen2.5:7b",
        base_url="http://localhost:11434"
    )

    metric = AnswerRelevancyMetric(
        threshold=0.7,
        model=evaluator_model
    )

    evaluate(
        test_cases=test_cases,
        metrics=[metric]
    )