from google.adk.tools.tool_context import ToolContext

def set_temperature_unit(unit: str, tool_context: ToolContext) -> dict:
    """Changes the user's preferred temperature unit in the session state.

    Args:
        unit (str): The temperature unit to set ('Celsius' or 'Fahrenheit')
        tool_context (ToolContext): The context containing the session state

    Returns:
        dict: status and result or error msg.
    """
    unit = unit.capitalize()  # Normalize input
    if unit not in ["Celsius", "Fahrenheit"]:
        return {
            "status": "error",
            "error": f"Invalid temperature unit: {unit}. Please use 'Celsius' or 'Fahrenheit'."
        }
    
    # Update the state
    tool_context.state["user_preference_temperature_unit"] = unit
    return {
        "status": "success",
        "report": f"Temperature unit preference has been set to {unit}."
    }
