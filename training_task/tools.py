"""Tools used by the Day 1 AI agent."""

import ast
import operator as op

from config import COURSE_FEES


def get_course_fee(course_code):
    """Look up private course fee information."""

    code = course_code.upper().strip()

    if code not in COURSE_FEES:
        return f"Unknown course: {course_code}"

    return COURSE_FEES[code]


ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
}


def calculator(expression):
    """Safely calculate a simple arithmetic expression."""

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
    "get_course_fee": get_course_fee,
    "calculator": calculator,
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": (
                "Look up private college course fee information. "
                "Use this for exact course fees."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303",
                    }
                },
                "required": ["course_code"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Calculate a simple arithmetic expression. "
                "Do not use Python eval()."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": (
                            "Arithmetic expression such as "
                            "12000+18000 or (12000+18000)*0.9"
                        ),
                    }
                },
                "required": ["expression"],
            },
        },
    },
]