"""Self-consistency experiment for the assignment scenario."""

from collections import Counter
import re

from config import client, MODEL


QUESTION = (
    "A student has assignments worth 20, 30, and 15 marks. "
    "She receives a 10% bonus on the total marks. "
    "What is the final total?"
)

PROMPT = """
Solve the problem step by step.
Show the calculation clearly.
End with:
Final Answer: <number>
"""


def ask(temperature):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": QUESTION},
        ],
        temperature=temperature,
    )

    return response.choices[0].message.content.strip()


def extract_answer(text):
    """Extract the numeric answer from the Final Answer line."""

    for line in reversed(text.splitlines()):
        if "final answer" in line.lower():
            numbers = re.findall(r"-?\d+(?:\.\d+)?", line)
            if numbers:
                return float(numbers[-1])

    numbers = re.findall(r"-?\d+(?:\.\d+)?", text)
    return float(numbers[-1]) if numbers else None


def run_experiment(runs, temperature):
    answers = []

    for number in range(1, runs + 1):
        response = ask(temperature)
        answer = extract_answer(response)

        print(f"\nRUN {number} (temperature={temperature})")
        print(response)
        print(f"EXTRACTED ANSWER: {answer}")

        answers.append(answer)

    return answers


if __name__ == "__main__":
    print("=" * 72)
    print("SELF-CONSISTENCY EXPERIMENT")
    print("=" * 72)
    print("\nQUESTION:", QUESTION)

    print("\n" + "=" * 72)
    print("NON-ZERO TEMPERATURE: 0.8")
    print("=" * 72)

    answers = run_experiment(5, 0.8)

    valid_answers = [answer for answer in answers if answer is not None]

    if valid_answers:
        winner, count = Counter(valid_answers).most_common(1)[0]
        print(
            f"\nMAJORITY ANSWER: {winner} "
            f"({count} of {len(valid_answers)} runs)"
        )

    print("\n" + "=" * 72)
    print("TEMPERATURE = 0")
    print("=" * 72)

    zero_answers = run_experiment(3, 0)

    print("\nTEMPERATURE 0 ANSWERS:", zero_answers)