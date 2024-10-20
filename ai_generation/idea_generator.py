# Example: ai_generation/idea_generator.py

from config.settings import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

# Your code here
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Generate an app idea based on the following trends...",
    max_tokens=150
)

print(response.choices[0].text.strip())
