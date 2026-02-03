# LLMOps Evaluation Pipeline

A CI/CD pipeline for automated testing and evaluation of LLM applications using GitHub Actions.


## Overview

This project demonstrates how to build an **automated evaluation pipeline** for LLM-powered applications. It shows best practices for:

- Writing evaluation tests for LLM outputs
- Running automated evals on every code change
- Catching regressions in prompt engineering
- Validating model behavior (correct responses & proper refusals)

## The Evaluation Approach

### Types of Tests

| Test Type | Purpose | Example |
|-----------|---------|---------|
| **Content Validation** | Verify LLM includes expected information | Check if science quiz mentions "telescope", "physics" |
| **Refusal Testing** | Ensure LLM declines out-of-scope requests | Asking about "Rome" should return "I'm sorry" |

### Why Automated LLM Evals Matter

- **Prompt changes can break things** — automated tests catch regressions
- **Model updates may change behavior** — tests verify consistency
- **CI/CD integration** — evaluations run on every push/PR



## The Evaluation Tests

```python
# test.py - Example evaluation patterns

def test_science_quiz():
    """Verify LLM generates relevant content for valid categories"""
    response = assistant_chain().invoke({"question": "Generate a quiz about science."})
    expected_words = ["davinci", "telescope", "physics", "curie"]
    assert any(word in response.lower() for word in expected_words)

def test_refusal_rome():
    """Verify LLM refuses out-of-scope requests appropriately"""
    response = assistant_chain().invoke({"question": "Generate a quiz about Rome"})
    assert "i'm sorry" in response.lower()
```

## Running Evaluations

### Locally

```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your OPENAI_API_KEY

# Run evals
pytest test.py -v
```

### In CI (GitHub Actions)

The pipeline automatically runs on every push to `main` or pull request:

1. **Add secret**: Go to repo **Settings → Secrets → Actions** → Add `OPENAI_API_KEY`
2. **Push code**: Evaluations run automatically
3. **View results**: Check the **Actions** tab

## Sample Application

The demo uses a quiz generator as the LLM application being tested:

- **Input**: Category request (Geography, Science, Art)
- **Output**: 3 quiz questions based on a knowledge base
- **Refusal**: Returns error for unsupported categories

This pattern applies to any LLM application — chatbots, content generators, classification systems, etc.

## Tech Stack

- **LangChain** — LLM application framework
- **OpenAI GPT-3.5-turbo** — Language model
- **Pytest** — Test framework
- **GitHub Actions** — CI/CD pipeline
