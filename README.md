# 🧙‍♂️ Game Master Agent (Fantasy Adventure Game)

This is a multi-agent, interactive text-based fantasy adventure game powered by OpenAI Agent SDK and Chainlit. Players can explore stories, fight monsters, and collect loot — all guided by intelligent agents and tools.

---

## 🧠 How It Works

### 🧩 Agents Involved:

1. **game_master_agent** – The main agent its role is:
    The main controller of a fantasy adventure game.
    Hand off to: 
    - NarratorAgent for story progression
    - MonsterAgent for combat
    - ItemAgent for inventory

2. **narrator_agent** – Narrate the story based on user choices. Use `generate_event` tool when needed.

3. **monster_agent** – Handle combat situations. Use `roll_dice tool` to determine attack success.

4. **item_agent** – Provide inventory updates and rewards. Use `generate_event` tool to simulate loot.
---

## 🔧 Tool Used

### `roll_dice(sides: int = 6) -> dict`

Roll dice to generate random number with this random number.

### `generate_event(location: str) -> dict:`

Provide Agent to dynamic storytelling abilities based on user selected location.


---

## 🛠️ Technologies

- Python 
- Chainlit (for chat interface)
- OpenAI Agent SDK
- Mock tools + multi-agent system
- Handsoff


