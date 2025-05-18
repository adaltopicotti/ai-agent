# AI Research Assistant

A Python-based research assistant that leverages both OpenAI's GPT-4 and Anthropic's Claude models to generate comprehensive research reports.

## Features

- Multi-model support (OpenAI GPT-4 and Anthropic Claude)
- Web search capabilities using DuckDuckGo
- Wikipedia integration for detailed information
- Automatic report saving with timestamps
- Structured output using Pydantic models

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key
   ANTHROPIC_API_KEY=your_anthropic_key
   ```

## Usage

Run the main script:
   ```bash
   python main.py
   ```
