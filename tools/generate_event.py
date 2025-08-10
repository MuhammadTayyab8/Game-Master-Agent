import os
from dotenv import find_dotenv, load_dotenv
from agents import AsyncOpenAI, function_tool, RunContextWrapper
from typing import TypedDict
import chainlit as cl

# Load env variables
load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("BASE_URL")

# Client setup
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

# Input schema
class EventGenerate(TypedDict):
    location: str

@function_tool
@cl.step(type="Story Generation")
async def generate_event(wrapper: RunContextWrapper, event_input: EventGenerate) -> dict:
    """Provide dynamic storytelling based on the user-selected location."""
    print("Tool Call: generate_event")
    try:
        prompt = f"Generate a dynamic fantasy story or continue the story set in {event_input['location']}."

        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}]
        )

        story_data = response.choices[0].message.content.strip()
        print(story_data, "story_data")
        return {"story": story_data}

    except Exception as e:
        print(f"Error in tool: {str(e)}")
        return {"error": f"Error in tool: {str(e)}"}
