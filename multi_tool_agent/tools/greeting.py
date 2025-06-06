from google.adk.tools.tool_context import ToolContext
from typing import Optional

def say_hello(name: Optional[str], tool_context: ToolContext) -> str:
    """Provides a simple greeting. If a name is provided, it will be used.

    Args:
        name (str, optional): The name of the person to greet. Defaults to a generic greeting if not provided.
        tool_context (ToolContext): The context containing the session state

    Returns:
        str: A friendly greeting message.
    """
    if name:
        greeting = f"Hello {name}! Welcome!"
    else:
        greeting = "Hello! Welcome!"
    return greeting
