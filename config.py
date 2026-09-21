"""Shared configuration: chooses the LLM provider and holds the lab data."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq").strip().lower()

if PROVIDER == "groq":
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. Use groq."
    )

if not API_KEY:
    raise SystemExit(
        "No API key found. Check your .env file."
    )

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

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

QUESTIONS = [
    "How many marks is the AI Report worth?",
    "What is the total marks for the Python Lab and AI Report?",
    "Is the AI Report worth more marks than the Math Quiz, and by how many?",
    "Write a two-line reminder for my upcoming assignments.",
]

def banner(system_name):
    print(
        f"\n=== {system_name} | "
        f"provider: {PROVIDER} | model: {MODEL} ===\n"
    )