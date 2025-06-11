from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from typing import Optional
from ...tools.greeting import say_hello

MODEL_GEMINI_2_0_FLASH = "gemini/gemini-2.0-flash"

def create_greeting_agent() -> Optional[Agent]:
    """Creates and returns the greeting agent, or None if creation fails."""
    try:
        agent = Agent(
            model=LiteLlm(model=MODEL_GEMINI_2_0_FLASH),
            name="greeting_agent",
            instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. "
                      "Use the 'say_hello' tool to generate the greeting. "
                      "If the user provides their name, make sure to pass it to the tool. "
                      "Do not engage in any other conversation or tasks.",
            description="Handles simple greetings and hellos using the 'say_hello' tool.",
            tools=[say_hello],
        )
        print(f"✅ Agent '{agent.name}' created using model '{agent.model}'.")
        return agent
    except Exception as e:
        print(f"❌ Could not create Greeting agent. Check API Key. Error: {e}")
        return None
