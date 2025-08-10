from agents import Agent, handoff
from setup_config import model
from expert.item_agent import item_agent
from expert.monster_agent import monster_agent
from expert.narrator_agent import narrator_agent
from utils.make_on_handoff_message import make_on_handoff_message


game_master_agent = Agent(
    name="Game Master Agent",
    instructions="""
    You are the main controller of a fantasy adventure game.
    Hand off to: 
    - NarratorAgent for story progression
    - MonsterAgent for combat
    - ItemAgent for inventory
    """,
    model=model,

    handoffs=[
        handoff(agent=item_agent, on_handoff=make_on_handoff_message(item_agent)),
        handoff(agent=monster_agent, on_handoff=make_on_handoff_message(monster_agent)),
        handoff(agent=narrator_agent, on_handoff=make_on_handoff_message(narrator_agent))
    ]
)
