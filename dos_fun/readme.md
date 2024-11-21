## **1. Flask Server with Diagnostics**
Here’s a Flask server with an endpoint that logs response times and the server's resource state.

### Flask Server Code:
```python
import logging
from flask import Flask, jsonify, request
import time
import psutil  # To monitor CPU and memory usage

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def home():
    start_time = time.time()  # Track response time

    # Example processing (could add heavier computations here)
    response = jsonify({"message": "Welcome to the server!"})
    
    # Calculate response time
    response_time = time.time() - start_time

    # Log diagnostics
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    logging.info(f"Response Time: {response_time:.4f}s | CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
    
    return response

@app.route('/status')
def status():
    """Endpoint to check server status."""
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    return jsonify({
        "status": "Server is running",
        "cpu_usage": f"{cpu_usage}%",
        "memory_usage": f"{memory_usage}%"
    })

@app.route('/heavy')
def heavy():
    start_time = time.time()  # Track start time
    
    # Simulate heavy computation
    result = sum(i * i for i in range(10**6))
    
    # Get client IP address
    client_ip = request.remote_addr

    # Calculate diagnostics
    response_time = time.time() - start_time
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    
    # Log diagnostics with client IP
    app.logger.info(
        f"/heavy - Response Time: {response_time:.4f}s | CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Client IP: {client_ip}"
    )
    
    # Return diagnostics, computation result, and client IP
    return jsonify({
        "message": f"Heavy computation done for client at {client_ip}",
        "client_ip": client_ip,
        "result": result,
        "response_time": f"{response_time:.4f} seconds",
        "cpu_usage": f"{cpu_usage}%",
        "memory_usage": f"{memory_usage}%"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Features:
1. **Response Time Logging**:
   - Logs how long each request takes to process.
2. **Resource Monitoring**:
   - Logs CPU and memory usage using the `psutil` library.
3. **Status Endpoint**:
   - Provides current server stats (`/status`).
3. **Heavy Endpoint**:
   - Provides current server stats under a a bit of load (`/heavy`).

---

## **2. DDOS Script**
You need to come up with a client that can DDos that server above!  You are free to use whatever you would like.  Hit a roadblock?  Ask ChatGPT or 
Microsoft Copilot for some help in creating a script.  You have the whole class helping you - 20+ people!

---

## **Game Mechanics**
1. **Objective for Students**:
   - Create their own attack scripts to bring down the server or maximize stress without crashing it.
   - Analyze server logs and diagnostics to learn about resource bottlenecks.
2. **Instructor's Role**:
   - Monitor Flask logs to observe response times, CPU, and memory usage.
   - Encourage students to optimize their scripts for maximum effect.

---

### **Example Gameplay Rules**:
- **Win Condition**: The student whose script slows down the server the most (e.g., response times spike or the server crashes) wins.
- **Post-Attack Discussion**:
  - How did different strategies affect the server?
  - How can we design systems to withstand such attacks (e.g., rate limiting, auto-scaling)?

---
