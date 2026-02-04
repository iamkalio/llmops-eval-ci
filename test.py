from app import assistant_chain
from app import system_message
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

import os
import re

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


def eval_expected_words(
    system_message,
    question,
    expected_words,
    human_template="{question}",
    llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
    output_parser=StrOutputParser()):

    assistant = assistant_chain(system_message)
    answer = assistant.invoke({"question": question})
    print(answer)

    assert any(word in answer.lower()
               for word in expected_words), \
        f"Expected the assistant questions to include \
        '{expected_words}', but it did not"


def evaluate_refusal(
    system_message,
    question,
    decline_response,
    human_template="{question}",
    llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
    output_parser=StrOutputParser()):

    assistant = assistant_chain(
        system_message,
        human_template,
        llm,
        output_parser)

    answer = assistant.invoke({"question": question})
    print(answer)

    assert decline_response.lower() in answer.lower(), \
        f"Expected the bot to decline with \
        '{decline_response}' got {answer}"


def eval_quiz_format(
    system_message,
    question,
    expected_questions=3,
    human_template="{question}",
    llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
    output_parser=StrOutputParser()):
    """
    Verify the quiz follows the expected delimiter-based format.
    Checks for 'Question N:####' pattern to ensure LLM maintains output structure.
    """
    assistant = assistant_chain(system_message)
    answer = assistant.invoke({"question": question})
    print(answer)

    # Pattern to match "Question 1:####", "Question 2:####", etc.
    pattern = r'Question\s+\d+:####'
    matches = re.findall(pattern, answer)

    assert len(matches) == expected_questions, \
        f"Expected {expected_questions} questions in format 'Question N:####', " \
        f"found {len(matches)}. Output: {answer[:200]}..."


def eval_output_type(
    system_message,
    question,
    should_be_plain_text=True,
    human_template="{question}",
    llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
    output_parser=StrOutputParser()):
    """
    Verify output format is as expected (plain text vs markdown-wrapped).
    Prevents LLM from returning markdown code blocks when plain text is expected.
    """
    assistant = assistant_chain(system_message)
    answer = assistant.invoke({"question": question})
    print(answer)

    if should_be_plain_text:
        # Should NOT be wrapped in markdown code blocks
        assert not answer.strip().startswith('```'), \
            f"Expected plain text, got markdown-wrapped output: {answer[:100]}..."
        
        # Should NOT start with JSON/dict characters if we expect text
        assert not answer.strip().startswith('{') and not answer.strip().startswith('['), \
            f"Expected plain text, got JSON-like output: {answer[:100]}..."


"""
  Test cases
"""


def test_science_quiz():
    question = "Generate a quiz about science."
    expected_subjects = ["davinci", "telescope", "physics", "curie"]
    eval_expected_words(
        system_message,
        question,
        expected_subjects)


def test_geography_quiz():
    question = "Generate a quiz about geography."
    expected_subjects = ["paris", "france", "louvre"]
    eval_expected_words(
        system_message,
        question,
        expected_subjects)


def test_refusal_rome():
    question = "Help me create a quiz about Rome"
    decline_response = "I'm sorry"
    evaluate_refusal(
        system_message,
        question,
        decline_response)


def test_science_quiz_format():
    """Test that science quiz follows the required delimiter format"""
    question = "Generate a quiz about science."
    eval_quiz_format(
        system_message,
        question,
        expected_questions=3)


def test_geography_quiz_format():
    """Test that geography quiz follows the required delimiter format"""
    question = "Generate a quiz about geography."
    eval_quiz_format(
        system_message,
        question,
        expected_questions=3)


def test_output_is_plain_text():
    """Test that output is plain text, not markdown or JSON wrapped"""
    question = "Generate a quiz about art."
    eval_output_type(
        system_message,
        question,
        should_be_plain_text=True)
