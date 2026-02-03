"""
Utility functions for the Quiz Generator project.
Handles API key retrieval from environment variables.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_openai_api_key():
    """Get OpenAI API key from environment variables."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found. Please set it in your .env file or environment variables."
        )
    return api_key
