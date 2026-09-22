# Comparing Direct Prompting, Chain-of-Thought, and ReAct

## Scenario

I chose a Student Assignment Tracking scenario. The private assignment records contain three assignments: Python Lab worth 20 marks, AI Report worth 30 marks, and Math Quiz worth 15 marks. The scenario contains questions that require private assignment information as well as questions that require arithmetic reasoning.

## Direct Prompting

Direct prompting asks the language model to answer the question directly without giving it a structured reasoning instruction or access to external tools. In my experiment, the question "How many marks is the AI Report worth?" could not be answered because the private assignment information was not available to the model. The model correctly stated that it did not have that information.

For reasoning questions, direct prompting was able to produce correct answers. For example, for a 30-mark assignment with a 10% late penalty, it returned 27 marks. For the question involving assignments worth 20, 30, and 15 marks, it returned a total of 65 marks and an average of approximately 21.67 marks.

## Chain-of-Thought

Chain-of-Thought prompting asks the model to solve a problem step by step and show the calculations. In my experiment, CoT also could not answer the private AI Report marks question because it did not have access to the private assignment records.

For calculation-based questions, CoT showed intermediate steps. For example, it calculated the 10% penalty on 30 marks as 3 marks and then calculated 30 - 3 = 27. For the three-assignment question, it showed the addition of 20 + 30 + 15 = 65 and then calculated 65 / 3 ≈ 21.67.

Therefore, CoT provided more visible reasoning steps than direct prompting, but it did not provide access to private information.

## ReAct

ReAct combines reasoning with actions and observations. The model can decide when it needs a tool, use the tool, observe the result, and then produce a final answer.

For the question "How many marks is the AI Report worth?", the ReAct agent called the `get_assignment_info` tool with the assignment name "AI REPORT". The tool returned that the AI Report is worth 30 marks and has 4 days remaining. The agent then produced the final answer that the AI Report is worth 30 marks.

This demonstrates the difference between a language model answering from the prompt alone and an agent that can access external or private information through tools.

## Comparison

| Aspect | Direct Prompting | Chain-of-Thought | ReAct |
|---|---|---|---|
| Reasoning depth | Short/direct answer | Step-by-step calculation | Reasoning combined with actions |
| Tool usage | No | No | Yes |
| Private information | Cannot access it | Cannot access it | Can access it through tools |
| Multi-step problems | Can solve simple calculations | Shows calculation steps | Can combine tools and calculations |
| Transparency | Shows final answer | Shows intermediate steps | Shows actions and observations |
| Speed and cost | Usually lower | Usually higher because of longer output | Can be higher because of tool calls |
| Consistency | Depends on model response | Can vary with temperature | Depends on both model and tool execution |

## Self-Consistency Observation

I used the reasoning question: "A student has assignments worth 20, 30, and 15 marks. She receives a 10% bonus on the total marks. What is the final total?"

The correct calculation is 20 + 30 + 15 = 65 marks. A 10% bonus is 6.5 marks, so the final total is 71.5 marks.

At temperature 0.8, I ran the CoT prompt five times. All five runs produced the final answer 71.5. Therefore, the majority answer was 71.5 in 5 out of 5 runs.

I also tested temperature 0 with three runs. All three runs produced 71.5. In this experiment, temperature 0 produced identical answers across all three runs.

The experiment shows that repeated reasoning can be compared to check consistency. However, consistency alone does not guarantee correctness; the answer still needs to be checked against the actual calculation.

## Suitability for This Scenario

For this Student Assignment Tracking scenario, ReAct is useful when a question requires private assignment information because the agent can call a tool to retrieve that information. Direct prompting is suitable for simple questions when all required information is already present in the prompt. CoT is useful when a calculation or multi-step reasoning process needs to be made explicit.

The choice therefore depends on the question. A simple calculation can be handled with direct prompting, a calculation where intermediate reasoning is useful can use CoT, and a question requiring private assignment data can use ReAct with an appropriate tool.

## Conclusion

Direct prompting, Chain-of-Thought, and ReAct serve different purposes. Direct prompting is simple and usually requires fewer steps. CoT adds explicit step-by-step reasoning for calculation and multi-step problems. ReAct extends the process by allowing the model to interact with tools and use observations before producing an answer.

The experiments showed that the main advantage of ReAct in this scenario was access to private assignment information through a tool. The CoT experiment showed more detailed calculation steps, while direct prompting produced shorter answers. Self-consistency showed that the selected reasoning problem produced the same correct numerical answer across the tested runs at both temperature 0.8 and temperature 0.
