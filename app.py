from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'demo_key')
print(f"API Key loaded: {API_KEY[:10]}..." if API_KEY != 'demo_key' else "Using demo key")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
SATELLITE_URL = "http://tile.openweathermap.org/map"

# Major Indian cities with their coordinates
INDIAN_CITIES = {
    # Metro Cities
    "Mumbai": {"lat": 19.0760, "lon": 72.8777},
    "Delhi": {"lat": 28.7041, "lon": 77.1025},
    "Bangalore": {"lat": 12.9716, "lon": 77.5946},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "Chennai": {"lat": 13.0827, "lon": 80.2707},
    "Kolkata": {"lat": 22.5726, "lon": 88.3639},

    # Major Cities
    "Pune": {"lat": 18.5204, "lon": 73.8567},
    "Ahmedabad": {"lat": 23.0225, "lon": 72.5714},
    "Jaipur": {"lat": 26.9124, "lon": 75.7873},
    "Surat": {"lat": 21.1702, "lon": 72.8311},
    "Lucknow": {"lat": 26.8467, "lon": 80.9462},
    "Kanpur": {"lat": 26.4499, "lon": 80.3319},
    "Nagpur": {"lat": 21.1458, "lon": 79.0882},
    "Indore": {"lat": 22.7196, "lon": 75.8577},
    "Thane": {"lat": 19.2183, "lon": 72.9781},
    "Bhopal": {"lat": 23.2599, "lon": 77.4126},
    "Visakhapatnam": {"lat": 17.6868, "lon": 83.2185},
    "Pimpri-Chinchwad": {"lat": 18.6298, "lon": 73.7997},
    "Patna": {"lat": 25.5941, "lon": 85.1376},
    "Vadodara": {"lat": 22.3072, "lon": 73.1812},

    # Additional Popular Cities
    "Kochi": {"lat": 9.9312, "lon": 76.2673},
    "Coimbatore": {"lat": 11.0168, "lon": 76.9558},
    "Madurai": {"lat": 9.9252, "lon": 78.1198},
    "Thiruvananthapuram": {"lat": 8.5241, "lon": 76.9366},
    "Mysore": {"lat": 12.2958, "lon": 76.6394},
    "Mangalore": {"lat": 12.9141, "lon": 74.8560},
    "Guwahati": {"lat": 26.1445, "lon": 91.7362},
    "Chandigarh": {"lat": 30.7333, "lon": 76.7794},
    "Dehradun": {"lat": 30.3165, "lon": 78.0322},
    "Shimla": {"lat": 31.1048, "lon": 77.1734},
    "Agra": {"lat": 27.1767, "lon": 78.0081},
    "Varanasi": {"lat": 25.3176, "lon": 82.9739},
    "Amritsar": {"lat": 31.6340, "lon": 74.8723},
    "Jodhpur": {"lat": 26.2389, "lon": 73.0243},
    "Udaipur": {"lat": 24.5854, "lon": 73.7125},
    "Ranchi": {"lat": 23.3441, "lon": 85.3096},
    "Bhubaneswar": {"lat": 20.2961, "lon": 85.8245},
    "Cuttack": {"lat": 20.4625, "lon": 85.8828},
    "Raipur": {"lat": 21.2514, "lon": 81.6296},
    "Jabalpur": {"lat": 23.1815, "lon": 79.9864},
    "Gwalior": {"lat": 26.2183, "lon": 78.1828},
    "Aurangabad": {"lat": 19.8762, "lon": 75.3433},
    "Nashik": {"lat": 19.9975, "lon": 73.7898},
    "Rajkot": {"lat": 22.3039, "lon": 70.8022},
    "Jammu": {"lat": 32.7266, "lon": 74.8570},
    "Srinagar": {"lat": 34.0837, "lon": 74.7973}
}

@app.route('/')
def index():
    """Home page with city selection dropdown"""
    return render_template('index.html', cities=list(INDIAN_CITIES.keys()))

@app.route('/weather/<city>')
def weather(city):
    """Weather details page for selected city"""
    if city not in INDIAN_CITIES:
        return "City not found", 404
    
    return render_template('weather.html', city=city)

@app.route('/api/weather/<city>')
def get_weather_data(city):
    """API endpoint to fetch weather data"""
    if city not in INDIAN_CITIES:
        return jsonify({"error": "City not found"}), 404
    
    try:
        # Get coordinates for the city
        coords = INDIAN_CITIES[city]
        
        # Make API request to OpenWeatherMap
        params = {
            'lat': coords['lat'],
            'lon': coords['lon'],
            'appid': API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            # Format the weather data
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'wind_direction': data['wind'].get('deg', 0),
                'visibility': data.get('visibility', 0) / 1000,  # Convert to km
                'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
                'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M'),
                'coordinates': coords,
                'satellite_layers': {
                    'clouds': f"{SATELLITE_URL}/clouds_new/{{z}}/{{x}}/{{y}}.png?appid={API_KEY}",
                    'precipitation': f"{SATELLITE_URL}/precipitation_new/{{z}}/{{x}}/{{y}}.png?appid={API_KEY}",
                    'temperature': f"{SATELLITE_URL}/temp_new/{{z}}/{{x}}/{{y}}.png?appid={API_KEY}"
                }
            }

            return jsonify(weather_data)
        else:
            # Return more detailed error information
            error_msg = f"API Error: {response.status_code}"
            if response.status_code == 401:
                error_msg = "Invalid API key. Please check your OpenWeatherMap API key."
            elif response.status_code == 404:
                error_msg = "Location not found."
            try:
                error_data = response.json()
                if 'message' in error_data:
                    error_msg += f" - {error_data['message']}"
            except:
                pass
            return jsonify({"error": error_msg}), 500
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
