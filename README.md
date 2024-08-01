# Weather Notification Script

This script fetches the current weather information for a specified city and displays it as a desktop notification every hour. It uses the OpenWeatherMap API to retrieve the weather data and the `notify-py` library to show notifications.

## Prerequisites

- Python 3.x
- An OpenWeatherMap API key

## Installation

1. **Clone the repository or download the script:**

    ```sh
    git clone https://github.com/yourusername/weather-notification.git
    cd weather-notification
    ```

2. **Install the required Python packages:**

    ```sh
    pip install requests notify-py
    ```

3. **Ensure the notification service is installed on your system (Linux only):**

    For Ubuntu/Debian-based distributions:
    
    ```sh
    sudo apt-get install libnotify-bin
    ```

## Usage

1. **Replace the placeholder API key with your OpenWeatherMap API key:**

    Open `weather_notification.py` and replace `'your_api_key_here'` with your actual OpenWeatherMap API key.

    ```python
    API_KEY = 'your_api_key_here'
    ```

2. **Specify the city for which you want to fetch the weather data:**

    Replace `'London'` with the desired city name.

    ```python
    CITY = 'London'
    ```

3. **Run the script:**

    ```sh
    python weather_notification.py
    ```

    The script will fetch the weather data for the specified city every hour and display it as a desktop notification.

## Example

Here is an example of how to modify and run the script:

1. Open `weather_notification.py` in a text editor.
2. Replace the API key and city:

    ```python
    API_KEY = 'your_actual_api_key'
    CITY = 'New York'
    ```

3. Save the changes and run the script:

    ```sh
    python weather_notification.py
    ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Issues

If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/yourusername/weather-notification/issues).

