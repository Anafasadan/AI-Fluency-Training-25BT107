# Comparing a Plain Chatbot, a Rule-Based Workflow, and an AI Agent

## 1. Scenario

The private-data scenario used in this project is student assignment tracking. The private data contains assignment names, subjects, marks, and remaining days. The three assignments used in the scenario are Python Lab, AI Report, and Math Quiz.

The Python Lab has 20 marks and 2 days remaining. The AI Report has 30 marks and 4 days remaining. The Math Quiz has 15 marks and 1 day remaining. This data is stored locally in the project and is treated as private student information.

The same type of student-assignment questions were tested using three different approaches: a plain chatbot, a rule-based workflow, and an AI agent.

## 2. Plain Chatbot

The plain chatbot mainly uses an LLM to generate responses. It does not have a tool for accessing the private assignment data. Therefore, when asked questions that require exact private information, it cannot reliably retrieve the assignment details. In the test, the chatbot could generate a general response, such as a reminder or message, but it could not directly access the private assignment records.

The chatbot does not use external tools or a predefined decision-making workflow. The LLM receives the system prompt and the user's question and generates an answer.

The main limitation is that the chatbot does not have direct access to the private assignment data. Therefore, it is not suitable for questions that require exact private information unless that information is explicitly provided to the model.

## 3. Rule-Based Workflow

The rule-based workflow uses predefined Python rules and conditions. It does not use an LLM. The workflow checks the user's question and applies programmed rules to determine the answer.

For example, the workflow can calculate the total marks for the Python Lab and AI Report and can compare the marks of the AI Report and Math Quiz. These answers are produced using normal Python logic and the private assignment data.

The main advantage of this approach is that its behaviour is predictable because the programmer defines the rules. However, it is less flexible. If a user asks a question for which a rule has not been programmed, the workflow cannot handle it. In the test, the workflow could answer the predefined calculation and comparison questions, but it could not generate a new two-line reminder because there was no rule for that type of request.

## 4. AI Agent

The AI agent combines an LLM, tools, and a loop. The LLM receives the user's question and decides whether a tool is needed. The available tool can retrieve private assignment details, while the safe calculator can perform arithmetic operations.

For example, when asked about the AI Report and Math Quiz, the agent used the `get_assignment_details` tool to retrieve the private records and then generated an answer. When asked for a reminder about an upcoming assignment, it retrieved the Python Lab details and used those details to generate a two-line reminder.

The important difference is that the LLM decides which tool to use, while the Python program actually executes the tool. The result is then returned to the LLM, which can continue the loop and produce the final answer.

In these tests, the agent handled a wider variety of requests than the fixed workflow because it could interpret the request and decide when private data was required. However, it still depends on the quality of the LLM and the correctness of the tools and private data.

## 5. Challenge Test

An additional challenge question was used to test a request that was not directly covered by the predefined workflow rules: "Which two assignments together have exactly 45 marks?"

The rule-based workflow could not answer because no rule was written for this type of question. The AI agent retrieved the details of all three assignments using the `get_assignment_details` tool and correctly identified that the AI Report and Math Quiz together have exactly 45 marks.

This demonstrates how the agent can combine private-data retrieval with reasoning over multiple pieces of information.

## 6. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High for general language responses, but limited for private-data questions | Low to medium because behaviour depends on predefined rules | High because the LLM can interpret different requests and select tools |
| Decision-making | LLM generates the response but has no private-data tool | Python rules make the decisions | LLM decides which tool or action is needed |
| Tool usage | No tools | No LLM tools; uses programmed Python logic | Uses tools such as `get_assignment_details` and `safe_calculator` |
| Private-data access | No direct access | Yes, through Python code and stored data | Yes, through the assignment-details tool |
| Multi-step task handling | Limited | Possible only when explicitly programmed | Can perform multiple tool calls through the agent loop |
| Automation | Suitable for simple response generation | Suitable for fixed, repeatable tasks | Suitable for tasks requiring flexible decisions and multiple actions |
| Reliability | General responses can be useful, but private facts cannot be verified without data access | Predictable for programmed cases | Can handle more cases, but depends on the LLM and tool execution |

## 7. Suitability Analysis

For this student assignment tracking scenario, the AI agent was able to handle a wider range of requests because it could combine natural-language understanding with access to the private assignment data. It could retrieve the required assignment information and then use that information to answer questions or generate useful reminders.

The rule-based workflow is useful when the questions and required operations are known in advance. It gives predictable results for the rules that have been programmed, but new types of questions require additional programming.

The plain chatbot is useful for general conversations and text generation, but it does not have direct access to the private assignment records in this project. Therefore, it cannot reliably answer questions that require exact private information.

## 8. Conclusion

A plain chatbot is appropriate for general conversation, text generation, and questions that do not require access to private or external data. A rule-based workflow is appropriate for fixed, predictable tasks where the required rules and conditions are known in advance.

An AI agent is appropriate when a task requires natural-language understanding, access to tools or private data, and multiple steps to complete the request. The agent can interpret the request, select an appropriate tool, observe the tool result, and continue the process until it can produce a final response.

This comparison demonstrates the main idea of Agentic AI: an agent combines an LLM with tools and a loop so that it can take actions rather than only generate a response.