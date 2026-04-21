"""
The client.py module loads environment variables, retrieves the OpenAI API key, and handles
communication with the OpenAI model by sending the user input along with the defined persona, and returning the model's
response. 
"""

from __future__ import annotations

# ================
# Standard Imports
# ================
import os

# ====================
# Third Party Imports
# ====================
from dotenv import load_dotenv
from openai import OpenAI # Client used to send requests to OpenAI models

# =====================
# Local Module Imports
# =====================
from persona import PERSONA

# load .env file and retrieve OpenAPI Key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_Key"))

def get_response(user_input: str) -> str:
    response = client.responses.create(
        model="gpt-5.2",
        instructions=PERSONA,
        input=user_input,
    )
    return response.output_text