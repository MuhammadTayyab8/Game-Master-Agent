import os
import chainlit as cl
from dotenv import load_dotenv, find_dotenv

from agents import (
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    RunConfig,
    function_tool,
    Agent,
    Runner
)

from openai.types.responses import ResponseTextDeltaEvent



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



# Tools
@function_tool
def roll_dice(sides: int = 6) -> dict:
    """"Roll dice to generate random number with this random number"""
    import random
    result = random.randint(1, sides)
    return {"result": result}


@function_tool
def generate_event(location: str) -> dict:
    """"Provide Agent to dynamic storytelling abilities based on user selected location"""
    events = {
        "forest": "You hear rustling behind the trees.",
        "cave": "A bat swoops down from the ceiling.",
        "village": "A merchant offers you a rare sword."
    }
    return {"event": events.get(location.lower(), "Nothing happens...")}





# narrator agent
narrator_agent = Agent(
    name="NarratorAgent",
    instructions="Narrate the story based on user choices. Use generate_event tool when needed.",
    tools=[generate_event]
)

# monster agent
monster_agent = Agent(
    name="MonsterAgent",
    instructions="Handle combat situations. Use roll_dice tool to determine attack success.",
    tools=[roll_dice]
)

# Item Agent
item_agent = Agent(
    name="ItemAgent",
    instructions="Provide inventory updates and rewards. Use generate_event tool to simulate loot.",
    tools=[generate_event]
)



# main agent
game_master_agent = Agent(
    name="GameMasterAgent",
    instructions="""
    You are the main controller of a fantasy adventure game.
    Hand off to: 
    - NarratorAgent for story progression
    - MonsterAgent for combat
    - ItemAgent for inventory
    """,
    handoffs=[narrator_agent, monster_agent, item_agent]
)








@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message("Hello! I am a Game Master Agent").send()



@cl.on_message
async def main(message: cl.Message):
    try:
        history = cl.user_session.get("history")

        msg = cl.Message(content="Thinking...")
        await msg.send()

        history.append({"role": "user", "content": message.content})


        result = Runner.run_streamed(
            game_master_agent,
            input=history,
            run_config=config
        )


        collected = ''

        async for event in result.stream_events():

            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                token = event.data.delta
                collected += token
                await msg.stream_token(token)

        history.append({"role": "assistant", "content": result.final_output})

        msg.content = collected
        await msg.update()

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        # await cl.Message(msg.content).send()
        await msg.update()
        raise
    