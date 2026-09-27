from app.generation.llm import LLMService


llm = LLMService()


prompt = """
You are an assistant for MNNIT Allahabad.

Answer the following question in one short sentence.

Question:
What is MNNIT?
"""


answer = llm.generate(prompt)

print("Answer:")
print(answer)