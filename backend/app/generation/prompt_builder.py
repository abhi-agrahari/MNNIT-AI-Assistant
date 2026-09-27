class PromptBuilder:

    def build_prompt(
        self,
        question: str,
        results
    ) -> str:

        context_parts = []

        for result in results:

            payload = result.payload

            context_parts.append(
                f"""
                    Source:
                    Document: {payload["document_id"]}
                    Page: {payload["page_number"]}

                    Content:
                    {payload["text"]}
                    """
            )

        # create context
        context = "\n".join(context_parts)

        # create prompt
        prompt = f"""
            You are an assistant for MNNIT Allahabad.

            Answer the user's question using only the information
            provided in the context below.

            If the answer is not present in the context, say:
            "I could not find this information in the provided documents."

            Do not make up information.

            Context:
            {context}

            Question:
            {question}

            Answer:
            """

        return prompt