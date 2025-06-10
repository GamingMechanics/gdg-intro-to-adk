import os
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
        # Get API key from environment variable
        api_key = os.getenv("WEATHER_API_KEY")
        if not api_key:
            error_msg = "Weather API key not found in environment variables."
            print(f"--- Tool: Error - {error_msg} ---")
            return {"status": "error", "error_message": error_msg}

        # Make API call
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        weather_data = response.json()

        # Extract relevant data
        temp_c = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        # Format based on user preference
        temp = weather_data["current"]["temp_c"] if preferred_unit == "Celsius" else weather_data["current"]["temp_f"]
        unit_symbol = "°C" if preferred_unit == "Celsius" else "°F"
        
        weather_report = (
            f'Weather in {weather_data["location"]["name"]}: '
            f'{temp}{unit_symbol}, '
            f'{weather_data["current"]["condition"]["text"]}'
        )

        # Store the last checked city in state
        tool_context.state["last_city_checked"] = city
        print(f"--- Tool: Updated state 'last_city_checked': {city} ---")

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
