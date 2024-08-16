# Assignment 5: Individual CI/CD Pipeline Setup and Docker Deployment

## Objective

In this assignment, you will take the project your group developed and make it your own. You will clone the project into your personal GitHub space, set up a CI/CD pipeline using GitHub Actions, run the tests, and push the final Docker container to DockerHub. This assignment will give you practical experience with continuous integration, continuous deployment, and Docker.

## Requirements

### 1. Clone the Project into Your Personal Space

- **Clone the Repository**:
  1. Go to your group's GitHub repository.
  2. Fork the repository to create a copy under your personal GitHub account.
  3. Clone the forked repository to your local machine:
     ```bash
     git clone https://github.com/YourUsername/YourRepositoryName.git
     ```

- **Rename the Project**:
  1. After cloning the repository, rename it locally and on GitHub to reflect that it is now your personal project.
  2. Update any references to the old project name within the code, `README.md`, and other documentation files.

- **Push the Renamed Project to GitHub**:
  1. Update the remote URL if you renamed the repository:
     ```bash
     git remote set-url origin https://github.com/YourUsername/NewRepositoryName.git
     ```
  2. Push the renamed repository back to GitHub:
     ```bash
     git push origin main
     ```

### 2. Hook Up a CI/CD Pipeline in GitHub

- **Set Up GitHub Actions**:
  1. Go to your renamed repository on GitHub.
  2. Navigate to the **"Actions"** tab.
  3. Click on **"Set up a workflow yourself"** or select a pre-built workflow template to get started.
  4. Create a new `.github/workflows/ci.yml` file in your repository.

- **Basic CI/CD Workflow**:
  1. Define a basic workflow that runs whenever you push changes to the `main` branch:
     ```yaml
     name: CI/CD Pipeline

     on:
       push:
         branches:
           - main

     jobs:
       build:
         runs-on: ubuntu-latest
         
         steps:
           - name: Checkout code
             uses: actions/checkout@v3

           - name: Set up Python
             uses: actions/setup-python@v4
             with:
               python-version: '3.x'

           - name: Install dependencies
             run: |
               python -m pip install --upgrade pip
               pip install -r requirements.txt

           - name: Run tests
             run: |
               pytest
     ```

### 3. Establish an Action

- **Make a Change to Trigger the Workflow**:
  1. Make a small, innocuous change in the code or `README.md` file to trigger the CI/CD pipeline.
  2. Commit your changes with a message like `"Test CI/CD pipeline"` and push to GitHub.
     ```bash
     git add .
     git commit -m "Test CI/CD pipeline"
     git push origin main
     ```

### 4. Run Tests and Ensure They Pass

- **Verify Tests Run in the Pipeline**:
  1. Monitor the **"Actions"** tab on GitHub to see if your workflow runs successfully.
  2. Ensure that the tests defined in your project pass within the CI pipeline.
  3. If any tests fail, debug the issues, fix them, and push the changes to re-run the pipeline.

### 5. Push the Docker Container to DockerHub

- **DockerHub Setup**:
  1. Ensure you have a DockerHub account. If you don't, create one at [DockerHub](https://hub.docker.com/).
  2. Create a new repository in DockerHub where you will push your Docker image.

- **Docker Build and Push**:
  1. Log in to DockerHub from your command line:
     ```bash
     docker login
     ```
  2. Build the Docker image from your project:
     ```bash
     docker build -t yourusername/yourimage:latest .
     ```
  3. Tag the Docker image (if necessary):
     ```bash
     docker tag yourimage:latest yourusername/yourimage:latest
     ```
  4. Push the Docker image to DockerHub:
     ```bash
     docker push yourusername/yourimage:latest
     ```

- **Update CI/CD Pipeline to Automate Docker Push** (Optional):
  1. Optionally, update your CI/CD pipeline to automatically build and push the Docker image to DockerHub after tests pass:
     ```yaml
     jobs:
       build:
         runs-on: ubuntu-latest
         
         steps:
           - name: Checkout code
             uses: actions/checkout@v3

           - name: Set up Python
             uses: actions/setup-python@v4
             with:
               python-version: '3.x'

           - name: Install dependencies
             run: |
               python -m pip install --upgrade pip
               pip install -r requirements.txt

           - name: Run tests
             run: |
               pytest

           - name: Build Docker image
             run: docker build -t yourusername/yourimage:latest .

           - name: Push Docker image to DockerHub
             env:
               DOCKERHUB_USERNAME: ${{ secrets.DOCKERHUB_USERNAME }}
               DOCKERHUB_PASSWORD: ${{ secrets.DOCKERHUB_PASSWORD }}
             run: |
               echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin
               docker push yourusername/yourimage:latest
     ```
  2. Add your DockerHub credentials to GitHub Secrets (`DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD`) for secure access during the CI/CD process.

## Deliverables

1. **Cloned and Renamed Repository**:
   - The repository should be cloned, renamed, and pushed to your personal GitHub space.

2. **CI/CD Pipeline**:
   - A functional CI/CD pipeline that runs tests whenever changes are pushed to the `main` branch.

3. **Passing Tests**:
   - All tests should pass in the CI/CD pipeline.

4. **Docker Image on DockerHub**:
   - A Docker image of your project should be successfully pushed to DockerHub and available in your personal DockerHub repository.

## Grading Rubric

| Item                                  | Hi Points                                                      | Med Points                                                   | Low Points                                                   |
|---------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Repository Cloning and Renaming       | Repository is correctly cloned, renamed, and pushed to GitHub with all references updated. | Repository is cloned and renamed, but some references or files are not updated correctly. | Repository is cloned but not renamed properly, or issues are present with the push to GitHub. |
| CI/CD Pipeline Setup                  | CI/CD pipeline is correctly set up, runs on each push, and tests are passing. | CI/CD pipeline is set up but may have issues with execution or test coverage. | CI/CD pipeline is poorly set up, with failing tests or improper configuration. |
| Docker Image Push to DockerHub        | Docker image is successfully built and pushed to DockerHub, and is accessible. | Docker image is built but may have issues with tagging or pushing to DockerHub. | Docker image is not successfully built or pushed to DockerHub, or is inaccessible. |
