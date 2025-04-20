from openai import OpenAI
import rich
from agent_examples.env import load_env

load_env()

client = OpenAI()

model = "gpt-4.1-nano"
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)

rich.print(completion)
