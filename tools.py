"""Tools used by the student assignment agent."""

import ast
import operator as op

from config import ASSIGNMENTS


def get_assignment_details(assignment_name):
    """Look up private details for a student assignment."""

    name = assignment_name.upper().strip()

    if name not in ASSIGNMENTS:
        return f"Unknown assignment: {assignment_name}"

    return ASSIGNMENTS[name]


ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
}


def safe_calculator(expression):
    """Calculate a simple arithmetic expression safely."""

    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            return ALLOWED_OPERATORS[type(node.op)](left, right)

        raise ValueError("Unsupported expression")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


TOOL_FUNCTIONS = {
    "get_assignment_details": get_assignment_details,
    "safe_calculator": safe_calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_assignment_details",
            "description": "Look up private student assignment information such as subject, marks, and days remaining.",
            "parameters": {
                "type": "object",
                "properties": {
                    "assignment_name": {
                        "type": "string",
                        "description": "Assignment name such as PYTHON LAB, AI REPORT, or MATH QUIZ",
                    }
                },
                "required": ["assignment_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "safe_calculator",
            "description": "Calculate a simple arithmetic expression. Do not use Python eval().",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression such as 20+30 or 30-15",
                    }
                },
                "required": ["expression"],
            },
        },
    },
]