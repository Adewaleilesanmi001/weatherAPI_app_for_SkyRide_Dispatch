
# SkyRide Dispatch Hub

SkyRide Dispatch Hub is a weather-check and dispatch management tool designed for urban bike couriers. The application provides live weather data, helping couriers make informed decisions about their route planning. The backend is built using FastAPI and Python, while the frontend is a sleek and responsive interface built with HTML, CSS, and JavaScript. This project allows dispatchers to track weather conditions across different cities and zones in real-time, ensuring safety and timely deliveries.

## Table of Contents

1. [Description](#description)
2. [Tech Stack](#tech-stack)
3. [Backend Setup](#backend-setup)
4. [Frontend Setup](#frontend-setup)
5. [Running the Project](#running-the-project)
6. [API Documentation](#api-documentation)
7. [Environment Variables](#environment-variables)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact Information](#contact-information)

## Description

SkyRide Dispatch Hub helps urban bike couriers stay ahead of the weather with real-time weather data for their dispatch zones. The backend fetches weather data using open APIs and provides it to the frontend, which displays the data in an intuitive user interface. This enables dispatchers to assess weather conditions quickly and adjust their plans accordingly. The backend handles the weather and geocoding APIs, while the frontend allows users to input locations and receive live weather updates.

## Tech Stack

### Backend:
- **FastAPI** - Framework for building the backend APIs.
- **Python** - Backend programming language.
- **Requests** - For making HTTP requests to external APIs.
- **Geoapify API** - Used for geocoding to convert city names into geographic coordinates.
- **OpenWeatherMap API** - Provides real-time weather data.
- **dotenv** - Loads environment variables from a `.env` file.
- **CORS Middleware** - Allows cross-origin requests to be made to the backend from the frontend.

### Frontend:
- **HTML** - Structure of the weather app.
- **CSS** - Styles the frontend interface.
- **JavaScript** - Handles dynamic interactions with the backend and renders weather data.
- **Fetch API** - Makes HTTP requests to the backend for weather updates.

## Backend Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/skyride-dispatch.git
    cd skyride-dispatch
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the root directory of the project and add your API keys:
    ```env
    GEOCODING_API=your_geoapify_api_key
    CURRENT_WEATHER_API=your_openweathermap_api_key
    ```

5. **Run the backend server**:
    ```bash
    uvicorn app:app --reload
    ```

    The backend should now be running on `http://localhost:8000`.

## Frontend Setup

1. **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/yourusername/skyride-dispatch.git
    cd skyride-dispatch
    ```

2. **Open the HTML file**:
    - Navigate to the `index.html` file in the frontend folder.
    - Open the file in your web browser to view the app.

## Running the Project

1. **Backend**:
    - The backend server runs on `http://localhost:8000`.
    - You can test it by visiting `http://localhost:8000/weather?city=New+York` to check the weather for a specific city.

2. **Frontend**:
    - Open the `index.html` file in your browser.
    - You will see the UI, where you can input a city or select from a list of predefined cities.
    - The weather data will be fetched from the backend and displayed on the page.

## API Documentation

### `/weather`
**GET**: Fetches weather data for a specific city.

**Query Parameters**:
- `city` (string): Name of the city to get weather data for.

**Response**:
```json
{
  "city": "New York",
  "country": "US",
  "coordinates": {"lat": 40.7128, "lon": -74.0060},
  "conditions": {
    "label": "Clear",
    "description": "clear sky",
    "icon": "01d"
  },
  "temperature": {
    "current_c": 20.5,
    "feels_like_c": 18.2,
    "min_c": 18.0,
    "max_c": 22.0
  },
  "humidity": 65,
  "pressure": 1015,
  "wind": {
    "speed_mps": 5.0,
    "direction_deg": 270,
    "gust_mps": 8.0
  },
  "visibility_m": 10000,
  "cloud_cover_pct": 0,
  "timestamp": 1609459200,
  "timezone_offset_s": -18000,
  "source": "openweathermap & geoapify",
  "raw": {}
}
```

## Environment Variables

Ensure that the following environment variables are set up in your `.env` file for the backend to function correctly:

- `GEOCODING_API`: Your Geoapify geocoding API key.
- `CURRENT_WEATHER_API`: Your OpenWeatherMap API key.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure that you follow proper coding standards and include tests if applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information

For support or inquiries, you can reach out to the development team:

- Email: support@skyride.com
- GitHub: [SkyRide Dispatch GitHub](https://github.com/yourusername/skyride-dispatch)
