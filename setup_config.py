import os
from dotenv import load_dotenv, find_dotenv

from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig,
)




load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")



# Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)


# Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)


# Config
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)