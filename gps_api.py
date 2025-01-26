from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import statistics
import logging

app = FastAPI()

# Data storage: A list to hold uploaded data temporarily
data_store = []

# Define the data model for individual location data
class LocationData(BaseModel):
    timestamp: str
    latitude: float
    longitude: float

@app.get("/summary", tags=["Summary"])
async def get_summary():
    """
    Endpoint to calculate and return the average of latitude and longitude.
    """
    if not data_store:
        raise HTTPException(status_code=404, detail="No data available to summarize.")

    # Extract latitude and longitude values from data_store
    latitudes = [item["latitude"] for item in data_store]
    longitudes = [item["longitude"] for item in data_store]

    # Calculate averages
    average_latitude = statistics.mean(latitudes)
    average_longitude = statistics.mean(longitudes)

    return {
        "average_latitude": average_latitude,
        "average_longitude": average_longitude
    }

@app.post("/upload", tags=["Upload"])
async def upload_data(locations: List[LocationData]):
    """
    Endpoint to upload new data temporarily.
    Accepts a list of location data.
    """
    if not locations:
        raise HTTPException(status_code=400, detail="No data provided.")
    
    try:
        # Append all the valid data to the in-memory data store
        for location in locations:
            # You can add validation for each location here if needed
            data_store.append(location.dict())
        return {"message": f"Successfully uploaded {len(locations)} entries."}
    except Exception as e:
        logging.error(f"Error while uploading data: {e}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Error uploading data: {str(e)}"
        )

# Set up basic logging
logging.basicConfig(level=logging.INFO)

@app.get("/data", tags=["Data"])
async def get_data():
    """
    Retrieve all uploaded data.
    """
    if not data_store:
        logging.error("No data available to retrieve.")
        raise HTTPException(status_code=404, detail="No data available.")
    
    logging.info(f"Returning {len(data_store)} data entries.")
    return {"data": data_store}