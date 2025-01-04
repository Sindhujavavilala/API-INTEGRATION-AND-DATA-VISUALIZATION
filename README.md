# API-INTEGRATION-AND-DATA-VISUALIZATION

**COMPANY**: CODTECH IT SOLUTIONS PVT.LTD

**NAME**: SINDHUJA VAVILALA

**INTERN ID**: CT08FWC

**DOMAIN**: Python Programming

**BATCH DURATION**: December 25th, 2024 to January 25th, 2025

**MENTOR NAME**: NEELA SANTHOSH

**Overview**
This project demonstrates how to fetch and visualize weather data for a city using the OpenWeatherMap API. By leveraging Python for API integration and data visualization, the script provides a 5-day weather forecast in an interactive, graphical format. The goal is to create an easy-to-use tool for extracting real-time weather data and generating insightful visualizations.

**Features**
 - Fetches real-time weather data for any city worldwide.
 - Extracts key information, such as temperatures and timestamps.
 - Displays a user-friendly line plot of temperature trends over the next five days.
 - Incorporates error handling to ensure smooth operation and clear feedback for incorrect city names or invalid API keys.

**Tools and Technologies Used**
**Python**: The programming language used to build the entire application.
**OpenWeatherMap API**: A public API that provides weather data.
**Matplotlib**: A Python library for creating static, animated, and interactive visualizations.
**Seaborn**: A Python visualization library built on Matplotlib that provides a high-level interface for attractive and informative statistical graphics.
**Requests Library**: A Python library for sending HTTP requests to interact with APIs.

**Resources**
**OpenWeatherMap API Documentation**: Used to understand API endpoints, parameters, and the JSON response structure.
**Python Official Documentation**: Referenced for understanding library functions and best practices.
**Online Tutorials**: Resources such as Python.org and DataCamp for coding practices and visualization tips.
**Stack Overflow**: For troubleshooting issues with API requests and data processing.
**Seaborn and Matplotlib Documentation**: Used for creating the line plot and customizing its aesthetics.

**Libraries Used**
**Requests**: To send HTTP requests and receive responses from the OpenWeatherMap API.
**Matplotlib**: To create the base visualization of the temperature trend.
**Seaborn**: To enhance the aesthetics and readability of the graph.

**Output**
The output is a line graph displaying the 5-day temperature forecast for a user-specified city. The graph includes:
- A title indicating the city name.
- Temperature values (in Celsius) plotted against timestamps.
- Clear x-axis labels for dates and times, rotated for readability.
- A smooth line connecting temperature points, with markers indicating each data point.
The graph helps users quickly understand temperature variations over time, making it a practical tool for weather analysis.

**Challenges Faced**
**Unauthorized API Requests**: Ensured the API key was valid and active.
**City Name Variations**: Added error handling to prompt users if the city name is incorrect.
**Formatting Data**: Managed nested JSON data to extract and format timestamps and temperatures.

**How the Output Was Generated**
**Data Extraction**:
 - Weather data (temperature, timestamps) was fetched in JSON format.
 - The JSON response was parsed, and the required fields were extracted.
**Data Visualization**:
 - Using Seaborn and Matplotlib, a line graph was created with appropriate labels, markers, and gridlines.
**User Interaction**:
 - The script prompts the user for a city name.
 - Outputs a graph based on the fetched data for the given city.

**Conclusion**
This project highlights the seamless integration of APIs and data visualization libraries to create a practical tool. The combination of OpenWeatherMap, Matplotlib, and Seaborn makes it easy to fetch, process, and visualize weather data in a meaningful way.
