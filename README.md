# CrewAI Demo

A minimal learning project to explore multiple AI agents with CrewAI.

## What it does

A simple document Q&A system with three agents:

- **Question Validator**: Checks if questions are valid
- **Researcher**: Searches through documents
- **Writer**: Generates responses

## Setup

1. Install dependencies:

```bash
poetry install
```

2. Create a `.env` file with your OpenAI API key:

```
cp .env.example .env
# Edit .env to add your OpenAI API key
```

3. Run the application:

```bash
poetry run streamlit run src/demo/app.py
```
