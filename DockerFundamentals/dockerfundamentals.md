### **Docker and Flask Tutorial for Students**

**Tips**

If you get permission denied when you try to run docker, please do the following.

1. Run this command:

```bash
sudo usermod -aG docker $USER
```

2. Restart the machine and login.  It should work! 

---

### **Goal:**
This tutorial will walk students through the basics of using Docker to containerize a simple **Flask web server**. By the end, students will understand the difference between Docker **images** and **containers**, and how to use Docker Compose to manage multi-container applications.

---

### **Step 1: Create a Simple Flask Web Server**

#### 1.1 Flask Code Setup

Students will start by creating a basic **Flask** web server that serves an HTML file.

1. **Create a project directory**:


   ```bash
   mkdir flask_docker_tutorial
   cd flask_docker_tutorial
   ```

2. **Create the Python script** (`app.py`):


   ```python
   # app.py
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

3. **Create the HTML file** (`templates/index.html`):

Note, for this to work, you need to create the templates directory and then create the file index.html within it.

   ```html
   <!-- templates/index.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Flask in Docker</title>
   </head>
   <body>
       <h1>Hello, Docker!</h1>
   </body>
   </html>
   ```

4. **Install Flask** locally to test:

You first need to understand what versions of python and pip you have installed.  Run these commands:

   ```bash
   ls -al /usr/bin/python*
   ls -al /usr/bin/pip*
   ```
If you do not have pip installed you will need to install it.  Like so:

   ```bash
   sudo apt install pip
   ```
   
Run this command again to verify pip was installed:

   ```bash
   ls -al /usr/bing/pip*
   ```

pip is used to install libraries for use by your python interpreter.  Flask will require a 3rd party library that is not included in the base Python intallation. So, you will need to install it.

You may see multiple distributions of pip and python.  You need to choose the ones that will match.  For example:

   ```bash
   pip3.10 and python3.10 match versions
   ``` 

You will then need to install the libary and run the Flask server.  Note once again, my versions of pip and python match - both are 3.10.

   ```bash
   pip3.10 install flask
   python3.10 app.py
   ```

   Visit `http://localhost:5000` to see "Hello, Docker!" displayed in the browser.

---

### **Step 2: Create a Dockerfile**

Next, students will containerize the Flask app by creating a **Dockerfile**.

1. **Create a Dockerfile** in the project directory:

Literally create a file named Dockerfile and copy and past the contents below into it.

   ```bash
   nano Dockerfile
   ```
It is a special file called a Dockerfile that is like a blueprint or set of instructions that tells docker how to build the container.  Here are the contents of the file.  You will create a docker container that deploys your Flask server.


   ```Dockerfile
   # Use an official Python runtime as a base image
   FROM python:3.9-slim

   # Set the working directory
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app

   # Install Flask
   RUN pip install flask

   # Expose the port on which the Flask app will run
   EXPOSE 5000

   # Define the command to run the app
   CMD ["python", "app.py"]
   ```

---

### **Step 3: Build and Run the Docker Container**

Students will now build the Docker image and run it as a container.

1. **Build the Docker image**:

First, let's see what images exist currently.  Run:

   ```bash
   docker images
   ```

Now perform the build.

   ```bash
   docker build -t flask-docker-app .
   ```

See what images exist.  Run:

   ```bash
   docker images
   ```
   
You should see the name associated with the tag (the -t option).  Run this command next:


   ```bash
   docker build -t whatever .
   ```

See what images exist.  Run:

   ```bash
   docker images
   ```

See what is happening there?  You get another image with a different name.  Note the amount of space that it is using!  Also, remember, images are similar to an exectubale (like a Windows EXE) at rest.  The docker build creates these excubtales.  But they are not running yet.

You need to know how to remove images as well.  You do it like so:

   ```bash
   docker rmi <image_id_or_name>
   ```

Specifically:

   ```bash
   docker rmi whatever
   ```
   
2. **Run the Docker container**:

Now it is time to run our container!  Before you do this, make sure if the Flask container is running from the python3.10 command earlier it is stopped!  Two applications cannot use the same port.  

   ```bash
   docker run -d -p 5000:5000 flask-docker-app
   ```

3. **Explanation**:
   - **-d**: Runs the container in detached mode (in the background).
   - **-p 5000:5000**: Maps port 5000 on the Docker container to port 5000 on your machine. This allows the web app to be accessed from `localhost:5000`.
   - Students should understand that this creates **two networks**: one between their machine and the container, and another inside the Docker container itself.

Awesome!  Nothing sort of happened though.  How can I tell the container is running?  Or what containers I do have running?  Issue this command:

   ```bash
   docker ps
   ```

Once a container is running, you can stop it with the following:

   ```bash
   docker stop <container_name_or_id>
   ```

Stop the container.  Then run this to see all the running and stopped containers.

   ```bash
   docker ps -a
   ```

The beauty of Docker is that you can run the same image multiple times as different containers - this is really what it is used for.  More advanced systems will save the state of containers when they are shut down - it becomes very involved.

Of course you can remove containers as well.  The container, however, needs to be stopped first.  The command is:

   ```bash
   docker rm <container_name_or_id>
   ```


---
### **Step 4: Understand Docker Images vs Containers**

Here’s a helpful analogy:

- **Docker Image**: Think of an image as a **program at rest** (like an EXE file). It's a snapshot of the application and its environment, but it isn't doing anything by itself.

- **Docker Container**: This is the **running instance** of the image, much like an **EXE being executed**. When you run an image, you create a container, which is an active, running instance of that image.

