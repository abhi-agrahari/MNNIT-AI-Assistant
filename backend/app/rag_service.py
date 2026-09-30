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
        college_id: str,
        history: list[dict] = []
    ):

        # rewrite question to be standalone
        search_question = self.llm.rewrite_question(
            question,
            history
        )

        #print("Original question:", question)
        #print("Search question:", search_question)

        # retrieve relevant chunks from Qdrant
        results = self.retriever.retrieve(
            question=search_question,
            college_id=college_id,
            top_k=5
        )

        if not results:
            return {
                "answer": "I could not find this information in the provided documents.",
                "sources": []
            }

        # build prompt using retrieved context
        prompt = self.prompt_builder.build_prompt(
            question=question,
            results=results
        )

        # generate answer using LLM
        answer = self.llm.generate(prompt)

        # extract source information
        sources = []
        seen_sources = set()

        for result in results:

            payload = result.payload

            source_key = (
                payload["document_id"],
                payload["page_number"]
            )

            # skip duplicate document/page sources
            if source_key in seen_sources:
                continue

            seen_sources.add(source_key)

            sources.append({
                "document_id": payload["document_id"],
                "page_number": payload["page_number"]
            })

        return {
            "answer": answer,
            "sources": sources
        }