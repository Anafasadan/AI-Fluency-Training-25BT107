"""Tools for the Day 2 assigned task."""

import ast
import operator as op


ASSIGNMENTS = {
    "PYTHON LAB": {
        "subject": "Python",
        "marks": 20,
        "days_remaining": 2,
    },
    "AI REPORT": {
        "subject": "Artificial Intelligence",
        "marks": 30,
        "days_remaining": 4,
    },
    "MATH QUIZ": {
        "subject": "Mathematics",
        "marks": 15,
        "days_remaining": 1,
    },
}


def get_assignment_info(assignment_name):
    """Return private information about an assignment."""
    name = assignment_name.upper().strip()

    if name not in ASSIGNMENTS:
        return f"Unknown assignment: {assignment_name}"

    return ASSIGNMENTS[name]


_ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}


def calculator(expression):
    """Safely calculate a basic arithmetic expression."""

    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return _ALLOWED_OPERATORS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
            return _ALLOWED_OPERATORS[type(node.op)](evaluate(node.operand))

        raise ValueError("Unsupported expression")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


TOOL_FUNCTIONS = {
    "get_assignment_info": get_assignment_info,
    "calculator": calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_assignment_info",
            "description": "Get private information about a student's assignment.",
            "parameters": {
                "type": "object",
                "properties": {
                    "assignment_name": {
                        "type": "string",
                        "description": "Assignment name such as AI REPORT or PYTHON LAB",
                    }
                },
                "required": ["assignment_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a basic arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression to calculate",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]