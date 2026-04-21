"""
The main.py module runs the chatbot loop, sends user input to the client.py module, and 
prints Sister Constance's response. 
"""

from __future__ import annotations

# =====================
# Local Module Imports
# =====================
from client import get_response

# ===========================
# Sister Constance main loop
# ===========================
def main() -> None:
    print("Sister Constance awaits. Speak. (type 'quit' to exit)")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "quit":
            print("Constance: Go, then. Endure the road before you.")
            break
        
        if not user_input:
            continue 

        reply = get_response(user_input)
        print(f"Constance: {reply}")

# ============
# Call Main()
# ============

if __name__ == "__main__":
    main()