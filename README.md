# AI-Powered Quiz Generator

An AI-powered quiz generator built with LangChain and OpenAI's GPT-3.5-turbo model.

## Features

- Generates customized quizzes based on user-specified categories (Geography, Science, Art)
- Uses a knowledge base of facts about various subjects (Leonardo DaVinci, Paris, Telescopes, etc.)
- Includes evaluation functions to test the quiz generation

## Setup Instructions

### 1. Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit the `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

**Getting an OpenAI API Key:**
1. Go to [OpenAI's platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key

### 4. Run the Notebook

```bash
# Start Jupyter
jupyter notebook

# Or use Jupyter Lab
jupyter lab
```

Then open `quiz_generator.ipynb` in the browser.

Alternatively, you can open the notebook directly in VS Code or Cursor with the Jupyter extension.

## Project Structure

```
circleci/
├── quiz_generator.ipynb  # Main notebook with the quiz generator
├── utils.py              # Utility functions for API key management
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables file
├── .env                  # Your actual environment variables (not tracked)
└── README.md             # This file
```

## Usage

1. Run the notebook cells in order
2. The quiz generator will create quizzes based on the categories:
   - **Geography**: Questions about Paris
   - **Science**: Questions about Leonardo DaVinci, Telescopes, Physics
   - **Art**: Questions about Leonardo DaVinci, Paris, Starry Night

## Evaluation

The notebook includes two evaluation functions:

1. **`eval_expected_words`**: Tests if the generated quiz contains expected keywords
2. **`evaluate_refusal`**: Tests if the model refuses to answer invalid requests

## Notes

- The refusal test is expected to fail because the current prompt doesn't explicitly instruct the model to refuse out-of-scope requests
- To make the refusal test pass, you would need to modify the `prompt_template` to include instructions for handling invalid categories
