"""
This module is responsible for logging Sister_Constance interaction to a single JSONL file.

Each log entry tracks:
1). Timestamp
2). user_input
3). model_response

"""

from __future__ import annotations

# ================
# Library Imports
# ================

from datetime import datetime
from typing import Any
from pathlib import Path
import json

# ==========
# Constants
# ==========

LOG_FILE_PATH = Path("logs/sister_constance.jsonl")

# =====================
# Logging Function
# =====================

def log_interaction(user_input: str, response: str) -> None:
    # prepare information for the logging entry
    timestamp = datetime.now().isoformat()
    clean_input = user_input.replace("\n", " ")
    clean_response = response.replace("\n", " ")

    log = {
        "timestamp": timestamp,
        "user_input": clean_input,
        "model_response": clean_response,
    }

    jsonl_log = json.dumps(log) + "\n" # convert Python dict to JSONL

    # Write log to a JSONL file 
    LOG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(LOG_FILE_PATH, "a", encoding="utf-8") as file:
        file.write(jsonl_log)