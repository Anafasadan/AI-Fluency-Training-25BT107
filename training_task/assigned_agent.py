"""ReAct agent for the Day 2 assigned task."""

import json

from config import client, MODEL
from tools_assignment import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are an assignment-tracking assistant.

You have access to tools that contain private assignment information
and a calculator.

Use a tool whenever the question requires private assignment data
or arithmetic that should be calculated.

After getting the required information, give a short final answer.
"""


def agent(question, max_steps=8):
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

        if not message.tool_calls:
            print(f"\nFINAL ANSWER: {message.content}")
            return message.content

        messages.append(message)

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(f"\nACTION: {tool_name}({arguments})")

            tool_function = TOOL_FUNCTIONS[tool_name]
            result = tool_function(**arguments)

            print(f"OBSERVATION: {result}")

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                }
            )

    return "The agent reached the maximum number of steps."


if __name__ == "__main__":
    question = "How many marks is the AI Report worth?"

    print("QUESTION:", question)
    agent(question)