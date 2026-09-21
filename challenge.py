"""A question none of the three systems was designed for."""

from workflow import workflow
from agent import agent

QUESTION = "Which two assignments together have exactly 45 marks?"

print("Q:", QUESTION)

print("\nWorkflow :", workflow(QUESTION))
print("\nAgent   :", agent(QUESTION))