"""
https://platform.openai.com/docs/guides/text?api-mode=responses

Some of our official SDKs include an output_text property on model responses for convenience,
which aggregates all text outputs from the model into a single string. This may be useful as
a shortcut to access text output from the model.
"""

from openai import OpenAI
import rich
from rich.panel import Panel
from rich.pretty import Pretty
from agent_examples.env import load_env

load_env()

client = OpenAI()

model = "gpt-4.1-nano"


response = client.responses.create(
    model=model,
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

rich.print(Panel(Pretty(response), title="instructions and input"))
print()
rich.print(response.output_text)


response = client.responses.create(
    model=model,
    input=[
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

rich.print(Panel(Pretty(response), title="developer and user role"))
print()
rich.print(response.output_text)
