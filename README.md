# CV to PowerPoint MVP

This project converts a plain text CV to structured JSON using Azure OpenAI and generates a simple PowerPoint file. A small web interface lets you paste text and download the result.

## Running locally

1. Create a `.env` file in the project root with your Azure OpenAI credentials:

```
AZURE_OPENAI_API_KEY=<key>
AZURE_OPENAI_ENDPOINT=<endpoint>
AZURE_OPENAI_DEPLOYMENT_NAME=<deployment>
AZURE_OPENAI_API_VERSION=<version>
```

2. Build and start using Docker Compose:

```
docker-compose up --build
```

The app will be available at `http://localhost:8000`.

## Manual usage

You can still run the converter script directly:

```
python -m src.convert my_cv.txt
```
