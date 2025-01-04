import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set your OpenWeatherMap API key and base URL
API_KEY = "4ccf51647eaec264c3c97fdcdbcca7b4"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def fetch_weather_data(city):
    """
    Fetch weather data for the given city from the OpenWeatherMap API.

    Args:
        city (str): The name of the city to fetch the weather data for.

    Returns:
        dict: The JSON response containing weather data.
    
    Raises:
        requests.exceptions.RequestException: If there's an issue with the HTTP request.
    """
    params = {
        "q": city,         # The city name
        "appid": API_KEY,  # Your API key
        "units": "metric"  # Use metric system for temperatures (Celsius)
    }
    response = requests.get(BASE_URL, params=params)  # Send GET request to API
    response.raise_for_status()  # Raise an error if the response status is not 200
    return response.json()  # Return the JSON response

def process_weather_data(data):
    """
    Process the weather data to extract timestamps and temperatures.

    Args:
        data (dict): The raw JSON data from the API.

    Returns:
        tuple: A tuple containing:
            - List of timestamps (str)
            - List of temperatures (float)
    """
    # Extract timestamps and temperatures from the JSON data
    timestamps = [item["dt_txt"] for item in data["list"]]
    temperatures = [item["main"]["temp"] for item in data["list"]]
    return timestamps, temperatures

def plot_weather_data(timestamps, temperatures, city):
    """
    Create a line plot of temperatures over time.

    Args:
        timestamps (list): List of date and time strings.
        temperatures (list): List of temperatures in Celsius.
        city (str): The name of the city for the plot title.
    """
    # Initialize the plot with a specified figure size
    plt.figure(figsize=(10, 6))
    
    # Create a line plot using Seaborn
    sns.lineplot(x=timestamps, y=temperatures, marker="o", color="b")
    
    # Set the plot title and axis labels
    plt.title(f"5-Day Weather Forecast for {city}", fontsize=16)
    plt.xlabel("Date and Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, fontsize=10)
    
    # Add grid lines to the plot
    plt.grid(True)
    
    # Adjust the layout to fit everything nicely
    plt.tight_layout()
    
    # Display the plot
    plt.show()

def main():
    """
    Main function to fetch, process, and visualize weather data for a city.
    """
    # Prompt the user to enter a city name
    city = input("Enter the name of the city: ")
    
    try:
        # Fetch weather data for the city
        weather_data = fetch_weather_data(city)
        
        # Process the weather data to extract timestamps and temperatures
        timestamps, temperatures = process_weather_data(weather_data)
        
        # Plot the weather data as a line graph
        plot_weather_data(timestamps, temperatures, city)
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"Error fetching data: {e}")
    except KeyError:
        # Handle issues with processing data, e.g., invalid city name
        print("Error processing data. Check if the city name is correct.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
