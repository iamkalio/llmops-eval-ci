"""
Utility functions for the Quiz Generator project.
Handles API key retrieval and configuration.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def get_openai_api_key():
    """Get OpenAI API key from environment variables."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found. Please set it in your .env file or environment variables."
        )
    return api_key


def get_circle_api_key():
    """Get CircleCI API key from environment variables."""
    api_key = os.getenv("CIRCLE_API_KEY")
    if not api_key:
        print("Warning: CIRCLE_API_KEY not found in environment variables.")
        return None
    return api_key


def get_gh_api_key():
    """Get GitHub API key from environment variables."""
    api_key = os.getenv("GITHUB_API_KEY")
    if not api_key:
        print("Warning: GITHUB_API_KEY not found in environment variables.")
        return None
    return api_key


def get_repo_name():
    """Get the repository name from environment variables."""
    repo_name = os.getenv("REPO_NAME", "quiz-generator")
    return repo_name


def get_branch():
    """Get the branch name from environment variables."""
    branch = os.getenv("BRANCH_NAME", "main")
    return branch
