from agents import Agent
from setup_config import model
from tools.generate_event import generate_event


narrator_agent = Agent(
    name="Narrator Agent",
    instructions="Narrate the story based on user choices. Use generate_event tool when needed.",
    model=model,
    tools=[generate_event]
)