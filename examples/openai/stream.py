from openai import OpenAI
from agent_examples.env import load_env

load_env()

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {
            "role": "user",
            "content": "Tell me a short story about a robot learning to paint.",
        }
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
