import json
from openai import OpenAI
import rich
from rich.panel import Panel
from rich.pretty import Pretty
from agent_examples.read_resource import read_text_resource

client = OpenAI()
model = "gpt-4.1-nano"

json_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "authors": {"type": "array", "items": {"type": "string"}},
        "abstract": {"type": "string"},
        "keywords": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["title", "authors", "abstract", "keywords"],
    "additionalProperties": False,
}

content = read_text_resource("wf92.txt")

response = client.responses.create(
    model=model,
    input=[
        {
            "role": "developer",
            "content": (
                "You are an expert at structured data extraction. "
                "You will be given unstructured text from a research paper "
                "and should convert it into the given structure."
            ),
        },
        {"role": "user", "content": content},
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "research_paper_extraction",
            "schema": json_schema,
            "strict": True,
        },
    },
)

rich.print(Panel(Pretty(response)))
structured = json.loads(response.output_text)
rich.print(structured)
