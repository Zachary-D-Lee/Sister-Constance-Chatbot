"""
chat_helpers.py modules contains helper functions, for the main chat loop and initial presentation.
"""
from __future__ import annotations

# =============
# Presentation
# =============

def print_initial_greeting() -> None:
    print("Sister Constance awaits. Speak. (type 'quit' to exit)")

def print_exit_message() -> None:
    print("Constance: Go, then. Endure the road before you.")

def print_constance_response(reply: str) -> None:
    print(f"Constance: {reply}")

# ===========
# User Input
# ===========

def get_user_input() -> str:
    return input("You: ").strip()