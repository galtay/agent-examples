from anthropic import Anthropic
import rich
from agent_examples.env import load_env

load_env()

client = Anthropic()
message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
    model="claude-3-5-haiku-20241022",
)
rich.print(message)
