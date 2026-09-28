from app.retrieval.retriever import Retriever
from app.generation.prompt_builder import PromptBuilder


retriever = Retriever()
prompt_builder = PromptBuilder()


question = "What are the hostel rules?"


# retrieve relevant chunks
results = retriever.retrieve(
    question=question,
    college_id="mnnit",
    top_k=3
)

results = retriever.retrieve(
    question=question,
    college_id="mnnit",
    top_k=3
)

print("Retrieved chunks:", len(results))

for result in results:
    print("Page:", result.payload["page_number"])


prompt = prompt_builder.build_prompt(
    question=question,
    results=results
)

print(prompt)


# build the LLM prompt
prompt = prompt_builder.build_prompt(
    question=question,
    results=results
)


print(prompt)