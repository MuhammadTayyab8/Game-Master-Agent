from agents import Agent
from setup_config import model
from tools.generate_event import generate_event


item_agent = Agent(
    name="Item Agent",
    instructions="Provide inventory updates and rewards. Use generate_event tool to simulate loot.",
    model=model,
    tools=[generate_event]
)
