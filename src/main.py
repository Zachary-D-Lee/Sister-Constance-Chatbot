"""
The main.py module runs the chatbot loop, sends user input to the client.py module, and 
prints Sister Constance's response. 
"""

from __future__ import annotations

# =====================
# Local Module Imports
# =====================
from client import get_response
from chat_helpers import print_initial_greeting, print_exit_message, get_user_input, print_constance_response

# ===========================
# Sister Constance main loop
# ===========================
def main() -> None:
    print_initial_greeting()

    # Begin main interaction loop
    while True:
        user_input = get_user_input()
        
        if user_input.lower() == "quit":
            print_exit_message()
            break
        
        if not user_input:
            continue 

        reply = get_response(user_input)
        print_constance_response(reply)

# ============
# Call Main()
# ============
if __name__ == "__main__":
    main()