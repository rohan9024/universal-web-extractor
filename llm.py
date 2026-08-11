import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.getenv(
        "OPENROUTER_API_KEY"
    ),
    base_url=
    "https://openrouter.ai/api/v1"
)

def extract_data(
    text,
    schema
):

    prompt = f"""
Extract data.

Return ONLY valid JSON.

Schema:

{json.dumps(schema, indent=2)}

Text:

{text[:15000]}
"""

    response = client.chat.completions.create(
        model="qwen/qwen3-8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = (
        response
        .choices[0]
        .message
        .content
    )

    content = (
        content
        .replace(
            "```json",
            ""
        )
        .replace(
            "```",
            ""
        )
    )

    return json.loads(
        content
    )
    