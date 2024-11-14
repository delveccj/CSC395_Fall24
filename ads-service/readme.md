### Prerequisites

1. **Install Flask and Requests**:
   ```bash
   pip install Flask requests
   ```
2. **OpenSky Network Account** (optional but recommended): Sign up at [OpenSky Network](https://opensky-network.org/) to get login credentials for more stable access to their API.

### Step 1: Set Up Flask App Structure

Create a new project folder. Inside, create the following files:
- `app.py` (main Python file)
- `templates/` folder with an `index.html` file
- `static/` folder for CSS or JavaScript if needed (optional)

### Step 2: Write the Flask App (app.py)

In `app.py`, set up a basic Flask app that will fetch ADS-B data from the OpenSky API and display it on a webpage.

```python
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Define the OpenSky API URL and (optional) your account credentials
API_URL = "https://opensky-network.org/api/states/all"

USERNAME = "your_username"  # optional
PASSWORD = "your_password"  # optional

def fetch_flight_data():
    try:
        # Request data from the OpenSky API
        response = requests.get(API_URL, auth=(USERNAME, PASSWORD))
        response.raise_for_status()  # Check for request errors
        data = response.json()
        
        # Extract basic flight information
        flights = []
        for state in data["states"][:10]:  # Limit to 10 for simplicity
            flight = {
                "icao24": state[0],
                "callsign": state[1],
                "origin_country": state[2],
                "altitude": state[13],
                "velocity": state[9],
                "longitude": state[5],
                "latitude": state[6],
            }
            flights.append(flight)
        return flights
    except Exception as e:
        print("Error fetching data:", e)
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    flights = fetch_flight_data()
    return jsonify(flights)

if __name__ == '__main__':
    app.run(debug=True)
```

This app defines two main routes:
- `/`: Renders the main webpage.
- `/data`: Fetches flight data and returns it in JSON format.

### Step 3: Create the HTML Template (index.html)

Inside the `templates` folder, create `index.html`. This file will use JavaScript to call the `/data` endpoint and display the flight data.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Flight Data</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; border: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Live Flight Data</h1>
    <table id="flight-table">
        <thead>
            <tr>
                <th>ICAO24</th>
                <th>Callsign</th>
                <th>Origin Country</th>
                <th>Altitude (m)</th>
                <th>Velocity (m/s)</th>
                <th>Longitude</th>
                <th>Latitude</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>

    <script>
        async function fetchFlightData() {
            try {
                const response = await fetch('/data');
                const flights = await response.json();

                const tableBody = document.getElementById('flight-table').querySelector('tbody');
                tableBody.innerHTML = '';  // Clear existing data

                flights.forEach(flight => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${flight.icao24}</td>
                        <td>${flight.callsign}</td>
                        <td>${flight.origin_country}</td>
                        <td>${flight.altitude || 'N/A'}</td>
                        <td>${flight.velocity || 'N/A'}</td>
                        <td>${flight.longitude || 'N/A'}</td>
                        <td>${flight.latitude || 'N/A'}</td>
                    `;
                    tableBody.appendChild(row);
                });
            } catch (error) {
                console.error("Error fetching flight data:", error);
            }
        }

        // Fetch data on page load and every 15 seconds
        fetchFlightData();
        setInterval(fetchFlightData, 15000);
    </script>
</body>
</html>
```

### Step 4: Run the Application

Now you’re ready to run the Flask app.

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser. You should see a table that updates every 15 seconds with the latest ADS-B data for flights.

### Step 5: Optional Enhancements

1. **Mapping**: Use a JavaScript mapping library like **Leaflet.js** to show flight positions on a map.
2. **Filters**: Add input fields to filter flights by altitude, country, or other criteria.
3. **Error Handling**: Add better error messages if the data fetch fails.

