# CV to JSON MVP

This project provides a minimal utility that converts a plain text CV into a JSON structure using Azure OpenAI.

## Usage

1. Create a `.env` file in the project root with your Azure OpenAI credentials:

```
AZURE_OPENAI_API_KEY=<key>
AZURE_OPENAI_ENDPOINT=<endpoint>
AZURE_OPENAI_DEPLOYMENT_NAME=<deployment>
AZURE_OPENAI_API_VERSION=<version>
```

2. Install dependencies (see `requirements.txt`).

3. Run the converter with a path to a text CV:

```
python -m src.convert my_cv.txt
```

The output will be printed as a JSON document that conforms to the simplified schema defined in `src/json_schema.py`.
