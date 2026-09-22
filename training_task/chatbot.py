"""System 1: a plain LLM chatbot.
No tools and no access to the private college data.
"""

from config import client, MODEL, QUESTIONS, banner


SYSTEM_PROMPT = """
You are a helpful college assistant.

You do NOT have access to the college's private course fee database.

If a question asks for private course fee information,
say that you do not have access to the fee list.

Do not guess or invent private course fee data.

You can answer general questions that do not require the private fee data.
"""


def chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    banner("SYSTEM 1: CHATBOT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", chatbot(question))
        print("-" * 70)
        