from agents import Agent
from setup_config import model
from tools.roll_dice import roll_dice


monster_agent = Agent(
    name="Monster Agent",
    instructions="Handle combat situations. Use roll_dice tool to determine attack success.",
    model=model,
    tools=[roll_dice]
)