from app.retrieval.retriever import Retriever
from app.generation.prompt_builder import PromptBuilder
from app.generation.llm import LLMService


class RAGService:

    def __init__(self):

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = LLMService()

    def answer(
        self,
        question: str,
        college_id: str
    ):

        # retrieve relevant chunks from Qdrant
        results = self.retriever.retrieve(
            question=question,
            college_id=college_id,
            top_k=5
        )

        # build prompt using retrieved context
        prompt = self.prompt_builder.build_prompt(
            question=question,
            results=results
        )

        # generate answer using the LLM
        answer = self.llm.generate(prompt)

        return answer