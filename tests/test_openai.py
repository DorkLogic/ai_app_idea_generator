import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    print("Please set your OpenAI API key in the .env file or as an environment variable.")
    print("Example .env file content:")
    print("OPENAI_API_KEY=your_api_key_here")
    exit(1)

# Initialize the client with your API key
client = OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, world!"}
        ]
    )
    print("API Response:")
    print(response.choices[0].message.content.strip())
except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("OpenAI API test completed.")
