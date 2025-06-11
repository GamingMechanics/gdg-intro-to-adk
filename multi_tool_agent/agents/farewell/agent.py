from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from typing import Optional
from ...tools.farewell import say_goodbye

MODEL_GEMINI_2_0_FLASH = "gemini/gemini-2.0-flash"

def create_farewell_agent() -> Optional[Agent]:
    """Creates and returns the farewell agent, or None if creation fails."""
    try:
        agent = Agent(
            model=LiteLlm(model=MODEL_GEMINI_2_0_FLASH),
            name="farewell_agent",
            instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. "
                      "Use the 'say_goodbye' tool when the user indicates they are leaving or ending the conversation "
                      "(e.g., using words like 'bye', 'goodbye', 'thanks bye', 'see you'). "
                      "Do not perform any other actions.",
            description="Handles simple farewells and goodbyes using the 'say_goodbye' tool.",
            tools=[say_goodbye],
        )
        print(f"✅ Agent '{agent.name}' created using model '{agent.model}'.")
        return agent
    except Exception as e:
        print(f"❌ Could not create Farewell agent. Check API Key. Error: {e}")
        return None
