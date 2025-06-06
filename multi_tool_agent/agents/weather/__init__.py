from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from typing import Optional
from ...tools.weather import get_weather
from ...tools.time import get_current_time
from ...tools.temperature import set_temperature_unit
from ..greeting import create_greeting_agent
from ..farewell import create_farewell_agent

MODEL_GEMINI_2_0_FLASH = "gemini/gemini-2.0-flash"

def create_weather_agent() -> Optional[Agent]:
    """Creates and returns the main weather agent with its sub-agents, or None if creation fails."""
    
    # Create sub-agents first
    greeting_agent = create_greeting_agent()
    farewell_agent = create_farewell_agent()
    
    if greeting_agent and farewell_agent:
        try:
            agent = Agent(
                name="weather_agent_v2",
                model=LiteLlm(model=MODEL_GEMINI_2_0_FLASH),
                description="The main coordinator agent. Handles weather, time, and temperature unit preference requests and delegates greetings/farewells to specialists.",
                instruction="You are the main Weather Agent coordinating a team. Your primary responsibilities are: "
                          "1. Provide weather information using the 'get_weather' tool for specific weather requests (e.g., 'weather in London'). "
                          "The 'get_weather' tool will format the temperature based on user preference stored in state. "
                          "2. Provide time information using the 'get_current_time' tool for time requests (e.g., 'current time in New York'). "
                          "3. Manage temperature unit preferences using the 'set_temperature_unit' tool when users want to switch between Celsius and Fahrenheit. "
                          "You should detect requests like 'switch to fahrenheit', 'use celsius', 'change temperature to fahrenheit', etc. "
                          "If you don't know which city the user is asking about for weather or time, use the state value for 'last_city_checked' if present. "
                          "\nYou have specialized sub-agents: "
                          "1. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                          "2. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'. Delegate to it for these. "
                          "\nAnalyze the user's query: "
                          "- If it's a greeting, delegate to 'greeting_agent' "
                          "- If it's a farewell, delegate to 'farewell_agent' "
                          "- If it's a weather request, use 'get_weather' "
                          "- If it's a time request, use 'get_current_time' "
                          "- If it's about changing temperature units, use 'set_temperature_unit' "
                          "- For anything else, respond appropriately or state that you cannot handle it.",
                tools=[get_weather, get_current_time, set_temperature_unit],
                sub_agents=[greeting_agent, farewell_agent],
                output_key="last_weather_report"
            )
            print(f"✅ Root Agent '{agent.name}' created with sub-agents: {[sa.name for sa in agent.sub_agents]}")
            return agent
        except Exception as e:
            print(f"❌ Could not create Weather agent. Error: {e}")
            return None
    else:
        print("❌ Cannot create root agent because one or more sub-agents failed to initialize.")
        return None
