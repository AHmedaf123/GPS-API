Backend Development with Python
Objective: Design and implement a simple backend system to store and process data using Python, with the ability to handle high-frequency data.

Description:
1. Step 1: Design a Backend System  
   - Use ChatGPT to figure out how to design a basic backend system.
   - Define an API that includes endpoints for:
     - Uploading data (e.g., sensor readings or GPS coordinates).
     - Retrieving processed data.

2. Step 2: Simulate Data Generation  
   - Write a Python script to simulate the generation of random data in real time.  
     Example: Random GPS data generation.
     ```json
     {
       "timestamp": "2025-01-23T12:00:00Z",
       "latitude": 52.5200,
       "longitude": 13.4050
     }
     ```

3. Step 3: Implement the Backend  
   - Use a framework like Flask or FastAPI to build the backend.
   - Add basic data processing functionality, such as:
     - Storing data in memory or a simple file.
     - Calculating a summary (e.g., the average latitude/longitude over time).

4. Step 4: Test the System  
   - Create a Python script to send requests to the API (e.g., POST and GET) and validate its functionality.

5. Step 5: Document Results  
   - Provide an explanation of how the backend was implemented, including code snippets and any challenges faced.
