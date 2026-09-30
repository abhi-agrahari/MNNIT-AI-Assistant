import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

class LLMService:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not set"
            )

        self.client = Groq(
            api_key=api_key
        )

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    def rewrite_question(
        self,
        question: str,
        history: list[dict]
    ) -> str:

        # if there is no previous conversation then question is already standalone
        if not history:
           return question

        conversation = ""

        for message in history:

            conversation += (
                f"User: {message['question']}\n"
                f"Assistant: {message['answer']}\n\n"
            )

        prompt = f"""
            You are a question rewriting assistant.

            Convert the user's latest question into a standalone question
            using the previous conversation when necessary.

            Do not answer the question.
            Only return the rewritten question.

            Previous conversation:
            {conversation}

            Latest question:
            {question}

            Standalone question:
            """

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()