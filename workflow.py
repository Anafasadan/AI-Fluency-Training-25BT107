"""System 2: a rule-based workflow for the student assignment tracker."""

import re
from config import ASSIGNMENTS, QUESTIONS


def workflow(question):
    text = question.lower()

    if "total" in text and "python lab" in text and "ai report" in text:
        total = (
            ASSIGNMENTS["PYTHON LAB"]["marks"]
            + ASSIGNMENTS["AI REPORT"]["marks"]
        )
        return f"Total marks: {total}"

    if "how many marks" in text and "ai report" in text:
        return f"AI Report is worth {ASSIGNMENTS['AI REPORT']['marks']} marks."

    if "more" in text and "ai report" in text and "math quiz" in text:
        difference = (
            ASSIGNMENTS["AI REPORT"]["marks"]
            - ASSIGNMENTS["MATH QUIZ"]["marks"]
        )
        return (
            f"Yes. AI Report is worth {ASSIGNMENTS['AI REPORT']['marks']} "
            f"marks, which is {difference} more than Math Quiz."
        )

    return "Sorry, I do not have a rule for this type of question."


if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW (no LLM) ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)