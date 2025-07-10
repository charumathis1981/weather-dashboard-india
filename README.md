# Weather Dashboard - India

A beautiful, responsive two-page weather dashboard that displays real-time weather information for major Indian cities with satellite imagery integration.

## Features

### Page 1: City Selection
- Dropdown menu with 20 major Indian cities
- Quick-select cards for popular cities (Mumbai, Delhi, Bangalore, Chennai, Hyderabad, Kolkata)
- Modern, responsive design with smooth animations
- Keyboard navigation support

### Page 2: Weather Details
- **Current Weather**: Temperature, feels-like temperature, weather description with icons
- **Detailed Metrics**: Humidity, pressure, wind speed, visibility, sunrise/sunset times
- **Interactive Satellite Map**: 
  - Base map view
  - Cloud coverage overlay
  - Precipitation overlay  
  - Temperature overlay
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Mapping**: Leaflet.js for interactive maps
- **Weather API**: OpenWeatherMap API
- **Styling**: Modern CSS with gradients, backdrop filters, and animations
- **Icons**: Font Awesome

## Setup Instructions

### 1. Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### 2. Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Get OpenWeatherMap API Key**:
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Get your API key from the dashboard

4. **Configure Environment Variables**:
   - Copy `.env.example` to `.env`
   - Replace `your_api_key_here` with your actual API key:
   ```
   OPENWEATHER_API_KEY=your_actual_api_key_here
   ```

### 3. Running the Application

1. **Start the Flask server**:
   ```bash
   python3 app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. **Select a City**: Choose from the dropdown or click on one of the popular city cards
2. **View Weather**: Click "View Weather Report" to see detailed information
3. **Explore Satellite Data**: Use the map controls to switch between different weather layers
4. **Navigate Back**: Use the back button or press ESC to return to city selection

## API Integration

The application integrates with OpenWeatherMap API to provide:
- Real-time weather data
- Weather icons
- Satellite imagery layers
- Detailed meteorological information

## Responsive Design

The dashboard is fully responsive and optimized for:
- **Desktop**: Full-featured experience with large maps and detailed layouts
- **Tablet**: Adapted layouts with touch-friendly controls
- **Mobile**: Compact design with stacked elements and mobile-optimized interactions

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Project Structure

```
weather-dashboard/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # City selection page
│   └── weather.html      # Weather details page
└── static/
    ├── css/
    │   └── style.css     # Main stylesheet
    └── js/
        └── main.js       # JavaScript functionality
```

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your OpenWeatherMap API key is valid and properly set in the `.env` file
2. **Module Not Found**: Ensure all dependencies are installed with `pip3 install -r requirements.txt`
3. **Port Already in Use**: If port 5000 is busy, modify the port in `app.py`

### Demo Mode

If you don't have an API key yet, the application will run in demo mode with placeholder data. Get your free API key from OpenWeatherMap to see real weather data.

## Contributing

Feel free to contribute to this project by:
- Adding more Indian cities
- Improving the UI/UX
- Adding more weather data visualizations
- Optimizing performance

## License

This project is open source and available under the MIT License.
