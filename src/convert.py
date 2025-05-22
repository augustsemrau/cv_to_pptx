"""Convert a text based CV to a structured JSON using Azure OpenAI."""
import json
import sys
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

from .json_schema import get_json_schema, validate_json
from .llm_utils import init_llm


def build_prompt(schema: str, cv_text: str) -> str:
    template = (
        "You extract structured data from CV text.\n"
        "Return a JSON object that follows this schema exactly:\n{schema}\n"
        "CV text:\n{cv_text}"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", template)
    ])
    return prompt.format(schema=schema, cv_text=cv_text)


def convert(cv_text: str) -> dict:
    llm = init_llm("convert")
    schema_str = get_json_schema(return_string=True)
    prompt = build_prompt(schema_str, cv_text)
    response = llm.invoke([HumanMessage(prompt)])
    data = json.loads(response.content)
    valid, err = validate_json(data)
    if not valid:
        raise ValueError(f"Generated JSON did not validate:\n{err}")
    return data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py <cv_text_file>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        text = f.read()
    result = convert(text)
    print(json.dumps(result, indent=2))
