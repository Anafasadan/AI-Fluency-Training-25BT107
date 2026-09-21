"""System 2: a rule-based workflow.
No LLM is used. The answers come from fixed Python rules.
"""

from config import COURSE_FEES, QUESTIONS


def workflow(question):
    text = question.lower()

    if (
        "total" in text
        and "cs101" in text
        and "ai202" in text
        and "10%" in text
    ):
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        scholarship_total = total * 0.90
        return f"Total fee after a 10% scholarship: Rs. {scholarship_total:,.0f}"

    if "fee" in text and "ai202" in text:
        return f"AI202 fee: Rs. {COURSE_FEES['AI202']:,}"

    if "more expensive" in text and "ds303" in text and "cs101" in text:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]

        if difference > 0:
            return (
                f"Yes. DS303 costs Rs. {difference:,} more than CS101."
            )
        else:
            return (
                f"No. DS303 does not cost more than CS101. "
                f"The difference is Rs. {abs(difference):,}."
            )

    if "welcome" in text and "ai students" in text:
        return (
            "Welcome to the AI programme!\n"
            "Enjoy learning, building, and experimenting with AI."
        )

    return "Sorry, I do not have a rule for this type of question."


if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW ===\n")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)