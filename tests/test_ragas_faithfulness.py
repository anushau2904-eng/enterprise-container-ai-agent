from tests.testdata.rag_dataset import evaluation_data

from app.retriever import get_retriever
from app.llm import generate_answer

from ragas import evaluate
from ragas.dataset_schema import EvaluationDataset, SingleTurnSample
from ragas.metrics import Faithfulness
from ragas.embeddings import HuggingFaceEmbeddings

from langchain_ollama import ChatOllama
from ragas.llms import LangchainLLMWrapper


def test_ragas_evaluation():

    # Create retriever
    retriever = get_retriever()

    # Store evaluation samples
    samples = []

    # Process every evaluation question
    for item in evaluation_data:

        question = item["question"]

        # Retrieve relevant documents
        documents = retriever.invoke(question)

        # Extract retrieved context
        context = [
            document.page_content
            for document in documents
        ]

        # Generate answer using Qwen + Ollama
        answer = generate_answer(
            question,
            "\n\n".join(context)
        )

        print("\n================================")
        print("Question:", question)
        print("Retrieved Context:", context)
        print("Answer:", answer)
        print("Ground Truth:", item["ground_truth"])

        # Create RAGAS sample
        sample = SingleTurnSample(
            user_input=question,
            response=answer,
            retrieved_contexts=context,
            reference=item["ground_truth"]
        )

        samples.append(sample)

    # Create RAGAS evaluation dataset
    dataset = EvaluationDataset(
        samples=samples
    )

    # Verify all questions were processed
    assert len(samples) == len(evaluation_data)

    # Local Qwen model for RAGAS evaluation
    evaluator_model = ChatOllama(
        model="qwen2.5:7b",
        temperature=0
    )

    # Wrap Ollama model for RAGAS
    evaluator_llm = LangchainLLMWrapper(
        evaluator_model
    )

    # Local HuggingFace embeddings
    evaluator_embeddings = HuggingFaceEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Faithfulness metric
    faithfulness = Faithfulness(
        llm=evaluator_llm
    )

    # # Answer Relevancy metric
    # answer_relevancy = AnswerRelevancy(
    #     llm=evaluator_llm
    # )

    # Run RAGAS evaluation
    result = evaluate(
        dataset=dataset,
        metrics=[faithfulness
            
        ],
        embeddings=evaluator_embeddings
    )

    print("\n================================")
    print("RAGAS RESULT")
    print("================================")
    print(result)

    # Basic validation
    assert result is not None