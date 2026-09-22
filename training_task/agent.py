"""System 3: a tool-using AI agent."""

import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a helpful college fee assistant.

Never guess private course fees.
Always use get_course_fee when an exact course fee is required.

Use the calculator tool for arithmetic.

Available courses:
CS101, AI202, DS303.

If no tool is needed, answer directly.
"""


def clean_tool_name(name):
    """Remove accidental extra channel text from a tool name."""
    return name.split("<|channel|>")[0].strip()


def agent(question, max_steps=6):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    for step in range(1, max_steps + 1):

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
           tool_choice="required" if step == 1 else "auto",
            temperature=0,
        )

        message = response.choices[0].message

        # If the model answers directly, finish.
        if not message.tool_calls:
            return message.content.strip()

        assistant_tool_calls = []

        for tool_call in message.tool_calls:
            tool_name = clean_tool_name(tool_call.function.name)

            assistant_tool_calls.append(
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_name,
                        "arguments": tool_call.function.arguments,
                    },
                }
            )

        messages.append(
            {
                "role": "assistant",
                "content": message.content or "",
                "tool_calls": assistant_tool_calls,
            }
        )

        # Execute each requested tool using Python.
        for tool_call in message.tool_calls:

            tool_name = clean_tool_name(tool_call.function.name)
            arguments = json.loads(tool_call.function.arguments)

            if tool_name not in TOOL_FUNCTIONS:
                result = f"Unknown tool: {tool_name}"
            else:
                result = TOOL_FUNCTIONS[tool_name](**arguments)

            print(
                f"   step {step}: {tool_name}({arguments}) -> {result}"
            )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": str(result),
                }
            )

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":
    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", agent(question))
        print("-" * 70)