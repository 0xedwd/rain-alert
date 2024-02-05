# Rain SMS Notification System

## Overview
Checks the weather for a specific location using the OpenWeatherMap API and sends a 
notification via SMS through Twilio if rain is forecasted within the next 12 hours. 

## Features

- Fetches weather data from OpenWeatherMap onecall API.
- Checks the forecast for rain in the next 12 hours. 
- Sends an SMS alert if rain is expected.

## Requirements

1. Clone the repository.
2. Account and API key from OpenWeatherMap 
3. An account, a verified phone number, and API credentials (SID and Auth Token) from Twilio.

## Setup

1. Rename api_keys.py.example to api_keys.py and fill in your Twilio and OpenWeatherMap API keys.
2. Modify config.py with your preferred settings, including your phone numbers and the coordinates for your location.

## Files

- api_keys.py: Stores your Twilio and OpenWeatherMap API keys. (Ensure this file is kept secure and not shared publicly.)
- config.py: Contains configuration settings like phone numbers and geographic coordinates for weather checks.
- weather_service.py: Handles the interaction with the OpenWeatherMap API to fetch weather data.
- notification_service.py: Manages sending SMS notifications through Twilio.
- main.py: The entry point for the application, orchestrating the weather check and sending notifications if necessary.

## Running the Application

In terminal:
```bash
python main.py
```
