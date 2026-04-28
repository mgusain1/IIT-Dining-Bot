import os
import json
from openai import OpenAI

client = None

if os.getenv("OPENAI_API_KEY"):
    client = OpenAI()

SYSTEM_PROMPT = """
You are an intent parser for an IIT dining chatbot.

Return ONLY valid JSON with this exact schema:
{
  "valid_query": true,
  "meal": null,
  "protein": false,
  "show_menu": false
}

Rules:
- "meal" must be one of: "breakfast", "lunch", "dinner", or null
- "protein" must be true if the user is asking for protein-rich / high-protein items
- "show_menu" must be true if the user is asking for the menu in general
- "valid_query" must be false if the question is unrelated to dining/menu/food offered today
- Do not include any extra keys
- Output JSON only
"""

def parse_query_with_gpt(question: str) -> dict:
    # No API key → fallback trigger
    if client is None:
        return None

    try:
        response = client.responses.create(
            model="gpt-5.4",
            instructions=SYSTEM_PROMPT,
            input=question
        )

        text = response.output_text.strip()
        data = json.loads(text)

        return {
            "valid_query": bool(data.get("valid_query", False)),
            "meal": data.get("meal"),
            "protein": bool(data.get("protein", False)),
            "show_menu": bool(data.get("show_menu", False)),
        }

    except Exception:
        return None