"""Compare direct prompting and Chain-of-Thought for the assignment scenario."""

from config import client, MODEL


QUESTIONS = [
    "How many marks is the AI Report worth?",
    "An assignment is worth 30 marks and has a 10% late penalty. How many marks remain?",
    "A student has assignments worth 20, 30, and 15 marks. What is the total, and what is the average per assignment?",
]


DIRECT_PROMPT = """
You are a helpful assignment assistant.
Answer the question directly and give only the final answer.
You do not have access to private assignment records or external tools.
"""


COT_PROMPT = """
You are a helpful assignment assistant.
Solve the question step by step.
Number each step and show calculations when needed.
You do not have access to private assignment records or external tools.
After the steps, write:
Final Answer: <answer>
"""


def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("=" * 72)
    print("DIRECT PROMPTING vs CHAIN-OF-THOUGHT")
    print("=" * 72)

    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\nQUESTION {number}: {question}")

        print("\n--- WITHOUT CoT ---")
        print(ask(DIRECT_PROMPT, question))

        print("\n--- WITH CoT ---")
        print(ask(COT_PROMPT, question))

        print("\n" + "-" * 72)