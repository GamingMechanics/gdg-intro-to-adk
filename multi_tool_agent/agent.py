import asyncio
import logging
import warnings
from google.adk.sessions import InMemorySessionService
from .agents import create_weather_agent

# Ignore all warnings
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

APP_NAME = "multi_tool_agent_demo"
SESSION_ID_STATEFUL = "session_state_demo_001"
USER_ID_STATEFUL = "user_state_demo"

# Initialize session service
session_service_stateful = InMemorySessionService()

# Define initial state data - user prefers Celsius initially
initial_state = {
    "user_preference_temperature_unit": "Celsius"
}

async def initialize_session():
    """Initialize the session with initial state."""
    session_stateful = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID_STATEFUL,
        session_id=SESSION_ID_STATEFUL,
        state=initial_state
    )
    print(f"✅ Session '{SESSION_ID_STATEFUL}' created for user '{USER_ID_STATEFUL}'.")

    # Verify the initial state was set correctly
    retrieved_session = await session_service_stateful.get_session(
        app_name=APP_NAME,
        user_id=USER_ID_STATEFUL,
        session_id=SESSION_ID_STATEFUL
    )
    return retrieved_session

# Initialize session
retrieved_session = None

async def init():
    """Initialize the application."""
    global retrieved_session
    retrieved_session = await initialize_session()
    print("\n--- Initial Session State ---")
    if retrieved_session:
        print(retrieved_session.state)
    else:
        print("Failed to initialize session")

# Use asyncio.ensure_future to schedule the initialization
asyncio.ensure_future(init())

# Create the root agent
root_agent = create_weather_agent()
