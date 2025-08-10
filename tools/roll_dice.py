from agents import function_tool
import chainlit as cl

@function_tool
@cl.step(type="Roll Dice")
def roll_dice(sides: int = 6) -> dict:
    """"Roll dice to generate random number with this random number"""
    import random
    result = random.randint(1, sides)
    return {"result": result}