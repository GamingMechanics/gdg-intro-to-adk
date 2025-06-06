# Multi-Tool Agent Demo

This project demonstrates the implementation of a multi-tool agent using Google's AI Development Kit (ADK). The agent can handle various tasks including weather information, time queries, and temperature unit preferences.

## Prerequisites

- Python 3.13.3
- Google ADK access
- WeatherAPI.com API key

## Installation

1. Clone the repository:
```bash
git clone git@github.com:GamingMechanics/gdg-intro-to-adk.git
cd gdg-intro-to-adk
```

2. Set up a Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the `multi_tool_agent` directory with the following variables:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
WEATHER_API_KEY=your_weather_api_key
GEMINI_API_KEY=your_google_api_key
```

Replace the placeholder values with your actual API keys:
- Get a WeatherAPI key from [WeatherAPI.com](https://www.weatherapi.com/)
- Get a Google API key from the [Google AI Studio](https://aistudio.google.com/apikey)

## Project Structure

```
multi_tool_agent/
├── __init__.py
├── agent.py
├── agents/
│   ├── __init__.py
│   ├── farewell/
│   │   └── __init__.py
│   ├── greeting/
│   │   └── __init__.py
│   └── weather/
│       └── __init__.py
└── tools/
    ├── __init__.py
    ├── farewell.py
    ├── greeting.py
    ├── temperature.py
    ├── time.py
    └── weather.py
```

The application is organized into the following components:

- `agent.py`: Main application entry point that handles session management and agent initialization
- `agents/`: Directory containing specialized agents:
  - `farewell/`: Agent for handling goodbye messages
  - `greeting/`: Agent for handling welcome messages
  - `weather/`: Main agent that coordinates weather, time, and temperature functionality
- `tools/`: Directory containing the individual tools:
  - `farewell.py`: Tool for generating goodbye messages
  - `greeting.py`: Tool for generating welcome messages
  - `temperature.py`: Tool for managing temperature unit preferences
  - `time.py`: Tool for retrieving current time in different cities
  - `weather.py`: Tool for retrieving weather information

## Available Tools

1. `say_hello`: Provides a personalized greeting
2. `say_goodbye`: Provides a farewell message
3. `get_weather`: Retrieves weather information for a specified city
4. `get_current_time`: Gets the current time for a specified city
5. `set_temperature_unit`: Sets the user's preferred temperature unit (Celsius/Fahrenheit)

## Usage

```python
from multi_tool_agent import agent

# The agent initialization is handled automatically when importing the module
# You can then use the various tools through the root_agent
```

For an interactive web UI, run:

```bash
adk web
```

The ADK web server will then run on `http://localhost:8000`

## VS Code Integration

This project includes VS Code settings for an optimal development experience. The recommended extensions are:
- Python extension
- Pylance
- Python Indent
- debugpy
- Code Spell Checker

These extensions will be automatically suggested when you open the project in VS Code.

## Development

The project uses:
- Type checking (basic mode)
- In-memory session management
- Gemini 2.0 Flash model for AI capabilities

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For any questions or support, please open an issue in the repository.
