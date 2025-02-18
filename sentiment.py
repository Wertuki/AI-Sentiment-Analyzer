import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def analyze_sentiment(text):
    """Analyzes sentiment of given text using OpenAI GPT API."""
    openai.api_key = API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Analyze the sentiment of this text (Positive, Neutral, or Negative):"},
                  {"role": "user", "content": text}],
        max_tokens=10
    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("Enter text to analyze sentiment: ")
    result = analyze_sentiment(user_input)
    print("\nSentiment:", result)
