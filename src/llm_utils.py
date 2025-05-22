"""Utility for initializing Azure OpenAI client."""
import os
from datetime import datetime
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI


def init_llm(trace_id: str = "mvp"):
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    load_dotenv(env_path, override=True)

    required = [
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_DEPLOYMENT_NAME",
        "AZURE_OPENAI_API_VERSION",
    ]
    for var in required:
        if not os.getenv(var):
            raise ValueError(f"Missing environment variable: {var}")

    client = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    )

    os.environ["LANGCHAIN_PROJECT"] = f"{trace_id}_{datetime.now().date()}"
    return client
