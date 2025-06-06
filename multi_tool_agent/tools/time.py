import datetime
from zoneinfo import ZoneInfo

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    city_normalized = city.lower().replace(" ", "")  # Basic normalization

    # Mock timezone data
    mock_tz_db = {
        "newyork": {"status": "success", "identifier": "America/New_York"},
        "london": {"status": "success", "identifier": "Europe/London"},
        "tokyo": {"status": "success", "identifier": "Asia/Tokyo"},
        "douglas": {"status": "success", "identifier": "Europe/Isle_of_Man"},
        "isleofman": {"status": "success", "identifier": "Europe/Isle_of_Man"},
    }

    if city_normalized not in mock_tz_db:
        return {
            "status": "error",
            "error": f"Sorry, I don't know the timezone for {city}."
        }

    tz_data = mock_tz_db[city_normalized]
    tz_identifier = tz_data["identifier"]
    
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}
