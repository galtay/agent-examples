import json
from openai import OpenAI
import rich
from pydantic import BaseModel, Field
from rich.panel import Panel
from rich.pretty import Pretty
from agent_examples.read_resource import read_text_resource

client = OpenAI()
model = "gpt-4.1-nano"


class ResearchPaperDetails(BaseModel):
    """Research paper details extraction."""

    title: str = Field(title="Paper Title", description="The title of the paper")
    abstract: str
    authors: list[str]
    keywords: list[str]


# Print the JSON schema
print("JSON Schema:")
rich.print(json.dumps(ResearchPaperDetails.model_json_schema(), indent=2))

content = read_text_resource("wf92.txt")

response = client.responses.parse(
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
    text_format=ResearchPaperDetails,
)

rich.print(Panel(Pretty(response)))
structured = json.loads(response.output_text)
rich.print(structured)
