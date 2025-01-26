GPS API - FastAPI Backend

Overview

A simple FastAPI backend to store and process GPS data. Includes endpoints for uploading GPS coordinates, retrieving stored data, and calculating the average latitude and longitude.

Installation

Clone or Download the project.

Install Dependencies:

bash
Copy
Edit
pip install fastapi uvicorn
Running the API
Start the server:

bash
Copy
Edit
uvicorn gps_api:app --reload
Access the API at http://127.0.0.1:8000.

Endpoints
POST /upload: Upload a list of GPS data (timestamp, latitude, longitude).

GET /data: Retrieve all uploaded GPS data.

GET /summary: Get the average latitude and longitude of uploaded data.

Example Usage
Upload Data (POST)
python
Copy
Edit
import requests

url = "http://127.0.0.1:8000/upload"
data = [
    {"timestamp": "2025-01-23T12:00:00Z", "latitude": 52.5200, "longitude": 13.4050},
    {"timestamp": "2025-01-23T12:05:00Z", "latitude": 48.8566, "longitude": 2.3522}
]
response = requests.post(url, json=data)
print(response.json())
Retrieve Data (GET)
bash
Copy
Edit
curl http://127.0.0.1:8000/data
Summary (GET)
bash
Copy
Edit
curl http://127.0.0.1:8000/summary
License
MIT License.
