# Day 1 Training Task – Observations

## 1. Observations

| Criterion | Chatbot | Workflow | Agent |
|---|---|---|---|
| Q1 correct? (Y/N) | N | Y | Y |
| Q2 correct? (Y/N) | N | Y | Y |
| Q3 correct? (Y/N) | N | Y | Y |
| Q4 handled well? (Y/N) | Y | Y | Y |
| Challenge question handled? (Y/N) | N | N | Y |
| Same output on a repeat run? (Y/N) | Not tested | Yes | Not tested |
| Approximate response time | Not measured | Very short | Short |
| Number of LLM calls per question | 1 | 0 | Varies depending on tool use |
| One strength | Natural-language responses | Predictable fixed rules | Flexible tool use |
| One weakness | No private-data access | Rigid for new questions | Depends on LLM and tools |
| Best suited for | General conversation | Fixed repeatable tasks | Multi-step tasks using tools |

## 2. Agent Trace – Question 2

Question 2:

> What is the total fee for CS101 and AI202 after a 10% scholarship?

The agent uses the course-fee lookup tool to retrieve the private fees and then uses the calculator to perform the arithmetic.

Expected calculation:

- CS101 = Rs. 12,000
- AI202 = Rs. 18,000
- Total = Rs. 30,000
- After 10% scholarship = Rs. 27,000

The agent therefore produces:

> Rs. 27,000

The exact order and number of tool calls can vary between runs.

## 3. Discussion Questions

### 1. The chatbot gave a confident but wrong fee. Why is that more dangerous than replying "I don't know"?

A confident but wrong answer can make the user believe incorrect information is reliable. Saying "I don't know" makes the limitation clear.

### 2. The workflow was always correct for questions 1 and 2. Why might a finance office still prefer it over the agent?

A finance office may prefer a rule-based workflow for common, fixed questions because the programmed rules provide predictable behaviour.

### 3. The agent's steps can change between runs. What problems would that cause in a real product?

Changing steps can make the system harder to test, debug, and predict. A real product may therefore need limits and monitoring.

### 4. Design a system that uses a workflow for common questions and an agent for the rest. Where would you draw the line?

Common and predictable questions can first be handled by predefined workflow rules. Questions that do not match those rules or require flexible multi-step tool use can be passed to the agent.

### 5. Which parts of `agent.py` are the LLM, the tools, and the loop?

The LLM is the model/API call. The tools are `get_course_fee` and `calculator`. The loop repeatedly sends information to the model, executes requested tools, adds the results, and continues until a final answer is produced.

## 4. Challenge Result

The challenge question was:

> I can pay Rs. 30,000. Which two courses can I take together within this budget?

The workflow did not have a predefined rule for this type of question.

The AI agent successfully found two combinations within the budget:

- CS101 + AI202 = Rs. 30,000
- CS101 + DS303 = Rs. 27,000

The result shows that the agent can use the private course-fee data and reason over multiple courses.

## 5. Viva Questions

### 1. What is the difference between a chatbot, a rule-based workflow, and an AI agent?

A chatbot mainly uses an LLM to generate responses. A workflow follows predefined rules and steps. An AI agent combines an LLM with tools and a loop.

### 2. In `agent.py`, which parts are the LLM, tools, and loop?

The model/API call is the LLM. The functions in `tools.py` are the tools. The repeated processing in `agent()` is the loop.

### 3. Who actually executes a tool?

The Python program executes the tool. The LLM decides which tool to request.

### 4. Why does the agent need a `max_steps` limit?

It limits the number of iterations and prevents the agent from continuing indefinitely.

### 5. Why does the calculator avoid Python's `eval()`?

The calculator uses restricted operations instead of allowing arbitrary Python code execution.

### 6. What is the purpose of the JSON Schema tool descriptions?

They describe the tool names, purposes, parameters, and required inputs so the LLM knows how to request the tools.

### 7. Why do we use a virtual environment for each project?

A virtual environment keeps the project's Python packages isolated from other projects.

### 8. Why is the API key kept in a `.env` file instead of inside `config.py`?

The API key is sensitive information. Keeping it in `.env` and excluding `.env` with `.gitignore` helps prevent the key from being uploaded to GitHub.

### 9. What does it mean that Ollama, Groq, and Hugging Face provide an OpenAI-compatible API?

It means they can provide an API interface that can be used with the OpenAI Python client structure.