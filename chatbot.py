from config import client, MODEL, QUESTIONS, banner

banner("PLAIN CHATBOT")

SYSTEM_PROMPT = """
You are a helpful college assistant.
Answer the user's question clearly.
You do not have access to the college's private fee database.
If you do not know a fee, say that you do not have the private fee data.
"""

for question in QUESTIONS:
    print(f"Q: {question}")

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )

    answer = response.choices[0].message.content.strip()

    print(f"A: {answer}\n")