import requests
import json

# URL of your API
base_url = "http://127.0.0.1:8000"

# Sample Data to upload (POST)
data = [
    {
        "timestamp": "2025-01-23T12:00:00Z",  
        "latitude": 52.5200,
        "longitude": 13.4050
    },
    {
        "timestamp": "2025-01-23T12:05:00Z",  
        "latitude": 48.8566,
        "longitude": 2.3522
    },
    {
        "timestamp": "2025-01-23T12:10:00Z",  
        "latitude": 34.0522,
        "longitude": -118.2437
    }
]

# POST request to upload data
response_post = requests.post(f"{base_url}/upload", json=data)

# Check POST request response
if response_post.status_code == 200:
    print(f"Data uploaded successfully: {response_post.json().get('message', 'No message')}")
else:
    print(f"Error uploading data: {response_post.status_code} - {response_post.json().get('detail', 'No detail available')}")

# GET request to retrieve data
response_get = requests.get(f"{base_url}/data")

# Check GET request response
if response_get.status_code == 200:
    print("\nData retrieved successfully:")
    retrieved_data = response_get.json()
    print(json.dumps(retrieved_data, indent=4))
else:
    print(f"Error retrieving data: {response_get.status_code} - {response_get.json().get('detail', 'No detail available')}")

# GET request to retrieve summary (average latitude and longitude)
response_summary = requests.get(f"{base_url}/summary")

# Check summary response
if response_summary.status_code == 200:
    print("\nSummary retrieved successfully:")
    summary_data = response_summary.json()
    print(json.dumps(summary_data, indent=4))
else:
    print(f"Error retrieving summary: {response_summary.status_code} - {response_summary.json().get('detail', 'No detail available')}")