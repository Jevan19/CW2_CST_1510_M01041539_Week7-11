import os
from openai import OpenAI

# Initialize the OpenAI client with your API key
# Use environment variable for security
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

# Make a simple API call
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Hello! What is AI?"}
]
)

# Print the response
print(completion.choices[0].message.content)
