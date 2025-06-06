import requests
from google.adk.tools.tool_context import ToolContext

def get_weather(city: str, tool_context: ToolContext) -> dict:
    """Retrieves the current weather report for a specified city using WeatherAPI.com.

    Args:
        city (str): The mandatory name of the city for which to retrieve the weather report.
        tool_context (ToolContext): The context containing the session state

    Returns:
        dict: status and result or error msg.
    """
    if city is None or city.strip() == "":
        return {
            "status": "error",
            "error": "Please provide a city name for the weather report."
        }

    # Read preference from state
    preferred_unit = tool_context.state.get("user_preference_temperature_unit", "Celsius")

    try:
        # Mock weather data for demo
        mock_weather = {
            "location": {"name": city},
            "current": {
                "temp_c": 22,
                "temp_f": 71.6,
                "condition": {"text": "Partly cloudy"}
            }
        }

        # Format based on user preference
        temp = mock_weather["current"]["temp_c"] if preferred_unit == "Celsius" else mock_weather["current"]["temp_f"]
        unit_symbol = "°C" if preferred_unit == "Celsius" else "°F"
        
        weather_report = (
            f'Weather in {mock_weather["location"]["name"]}: '
            f'{temp}{unit_symbol}, '
            f'{mock_weather["current"]["condition"]["text"]}'
        )
        
        return {"status": "success", "report": weather_report}

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "error": f"Failed to retrieve weather data: {str(e)}"
        }
    except (KeyError, ValueError) as e:
        return {
            "status": "error",
            "error": f"Error processing weather data: {str(e)}"
        }
