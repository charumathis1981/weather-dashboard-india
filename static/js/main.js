// Main JavaScript file for Weather Dashboard

// Utility functions
function formatTime(timestamp) {
    const date = new Date(timestamp * 1000);
    return date.toLocaleTimeString('en-IN', { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: false 
    });
}

function getWindDirection(degrees) {
    const directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'];
    const index = Math.round(degrees / 22.5) % 16;
    return directions[index];
}

// Weather condition backgrounds
function getWeatherBackground(condition) {
    const backgrounds = {
        'clear': 'linear-gradient(135deg, #74b9ff 0%, #0984e3 100%)',
        'clouds': 'linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%)',
        'rain': 'linear-gradient(135deg, #81ecec 0%, #00b894 100%)',
        'thunderstorm': 'linear-gradient(135deg, #636e72 0%, #2d3436 100%)',
        'snow': 'linear-gradient(135deg, #ddd6fe 0%, #8b5cf6 100%)',
        'mist': 'linear-gradient(135deg, #b2bec3 0%, #636e72 100%)',
        'default': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    };
    
    return backgrounds[condition.toLowerCase()] || backgrounds.default;
}

// Apply dynamic background based on weather
function updateBackgroundForWeather(weatherData) {
    if (weatherData && weatherData.description) {
        const condition = weatherData.description.toLowerCase();
        let backgroundType = 'default';
        
        if (condition.includes('clear')) backgroundType = 'clear';
        else if (condition.includes('cloud')) backgroundType = 'clouds';
        else if (condition.includes('rain') || condition.includes('drizzle')) backgroundType = 'rain';
        else if (condition.includes('thunder')) backgroundType = 'thunderstorm';
        else if (condition.includes('snow')) backgroundType = 'snow';
        else if (condition.includes('mist') || condition.includes('fog') || condition.includes('haze')) backgroundType = 'mist';
        
        document.body.style.background = getWeatherBackground(backgroundType);
    }
}

// Add loading animation
function showLoading(element) {
    if (element) {
        element.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    }
}

// Add smooth transitions
document.addEventListener('DOMContentLoaded', function() {
    // Add fade-in animation to main content
    const mainContent = document.querySelector('.main');
    if (mainContent) {
        mainContent.style.opacity = '0';
        mainContent.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            mainContent.style.transition = 'all 0.6s ease';
            mainContent.style.opacity = '1';
            mainContent.style.transform = 'translateY(0)';
        }, 100);
    }
    
    // Add hover effects to interactive elements
    const interactiveElements = document.querySelectorAll('.city-card, .weather-btn, .map-btn, .btn-back');
    interactiveElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        element.addEventListener('mouseleave', function() {
            if (!this.classList.contains('selected') && !this.classList.contains('active')) {
                this.style.transform = 'translateY(0)';
            }
        });
    });
});

// Add keyboard navigation support
document.addEventListener('keydown', function(event) {
    // ESC key to go back
    if (event.key === 'Escape') {
        const backButton = document.querySelector('.btn-back');
        if (backButton) {
            backButton.click();
        }
    }
    
    // Enter key to submit city selection
    if (event.key === 'Enter') {
        const viewWeatherBtn = document.getElementById('viewWeatherBtn');
        if (viewWeatherBtn && !viewWeatherBtn.disabled) {
            viewWeatherBtn.click();
        }
    }
});

// Add touch support for mobile devices
if ('ontouchstart' in window) {
    document.addEventListener('touchstart', function() {}, { passive: true });
}

// Service worker registration for offline support (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Uncomment the following lines if you want to add offline support
        // navigator.serviceWorker.register('/sw.js')
        //     .then(function(registration) {
        //         console.log('SW registered: ', registration);
        //     })
        //     .catch(function(registrationError) {
        //         console.log('SW registration failed: ', registrationError);
        //     });
    });
}

// Export functions for use in other scripts
window.WeatherDashboard = {
    formatTime,
    getWindDirection,
    updateBackgroundForWeather,
    showLoading
};
