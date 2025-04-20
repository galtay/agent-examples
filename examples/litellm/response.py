from litellm import completion
import rich
from rich.panel import Panel
from rich.pretty import Pretty
from agent_examples.env import load_env
import logging

# logging.basicConfig(level=logging.DEBUG)

load_env()

messages = [{"role": "user", "content": "Hello, how are you?"}]


# Gemini
# model = "gemini/gemini-2.5-pro-preview-03-25"
# model = "gemini/gemini-2.5-flash-preview-04-17"
# model = "gemini/gemini-2.0-flash"
model = "gemini/gemini-2.0-flash-lite"
# model = "gemini/gemma-3-27b-it"
response = completion(model=model, messages=messages)
rich.print(
    Panel(
        Pretty(response),
        title=model,
    )
)

# OpenAI
# model = "gpt-4.1-nano-2025-04-14"
model = "gpt-4.1-mini-2025-04-14"
response = completion(model=model, messages=messages)
rich.print(
    Panel(
        Pretty(response),
        title=model,
    )
)

# Anthropic
model = "anthropic/claude-3-5-haiku-20241022"
response = completion(model=model, messages=messages)
rich.print(
    Panel(
        Pretty(response),
        title=model,
    )
)
