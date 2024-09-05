# Assignment 2: The Business Development Person's 'Vision'

Note: This lab exercise will have a higher point total than Assignment 1 as it is much more complex!

## Intro

Your business development (BD) person has done it again. He has hit the road and pitched a vision for a new  project. He managed to get just enough funds for four weeks of development time for four to five developers.  The BD person has a dangerous understanding of technology and can pitch solutions that mostly use the technologies correctly.  He often leaves it to the devleopers to "fill in the details" and simply make stuff work.  

You are the crack development team.  You have not failed yet to implement one of his product visions - no matter how half-baked they are.  You intend to deliver once again!

In this assignment you setup the plan to deliver on your BD person's vision.  No software engineering project is successful without a plan that identifies:  1. What tasks will be worked when, 2. Milestones, 3. Who will work the tasks, and 3. An end product.

### His Vision: The AI-Backed Recipes Maker!

Look at the concept screen drawn out below.  The BD person drew out exactly what you need to build.  It's got the notes and what you need to get the job done - sort of. Your instructor understands the vision and can fill in some of the details.

![Recipe Buidler Product Visions](concept.png)

## Challenges

At this point - you might have identified some challenges and tasks.  For example:

1. UI Design - There is a web site shown in a browser.  Who can create UIs?
2. Docker - What is that?  It seems important.
3. Python Flask Container - This seems to be the web server.  Anyone have experience creating one of these?
4. Ollama Container - A quick Google search shows it allows you to run LLMs.  So - how do we connect the web server to it?
5. Message Passing - How are the messages passed back and forth?  For example, from the web browser to the server and so on.
6. Decompose Into Tasks - How do we decomposed this diagram into tasks?

## Steps to Success

### Resources:

Your instructor has provided resources to make this project easier!  You are going to need to install Docker and docker-compose on these machines.  We will do this together.  Here are instructions on how to do this in Ubuntu Jammy.  Note, for a couple of steps you might see a warning - it can be ignored:

[https://chatgpt.com/share/7fa3ec8e-9646-4e72-ba0a-09d7b780ec0d](https://chatgpt.com/share/c7bbf674-261b-47cf-ae9c-ba177684f1c8)

Stop at Step 5, Substep 2 please!

Let's run our first Docker container:

https://hub.docker.com/r/ollama/ollama

Now, let's move onto Step 5, Substep 2.  We will do more exercises with Docker in class.  But you need to have confidence you can use these technologies!

## Assignment 2 Tasks

### Section: Create a GitHub Project

1. **Make it Private**: 
   - Someone from your team must create a private GitHub repository.
   - It must be named:  CSC395_Team#  where # is your teams number.
   - Invite the other team members and the instructor as collaborators.
   - You do not need to restrict the project to only accept pull requests initially.  We may add that later!

### Section: Create the Tickets

1. **Discuss the Vision**:
   - Your team needs to discuss what the vision means and how to implement it in code.
2. **Create the Tickets**:
   - Break down the project into manageable tasks and create GitHub issues (tickets) for each.
3. **Organize into Milestones**:
   - Add the tickets to two one-week sprints.
4. **First Week Milestone**:
   - Ensure the first week ends with a milestone that represents a significant progress checkpoint.
5. **Final Project Milestone**:
   - The second week should culminate with the final product ready for review.

### Section: Project Plan

1. **Document the Plan**:
   - Create a document that explains the architecture, the development plan, how the work will proceed, and how progress will be measured.

### Section: Kickoff and Conclusion Brief

1. **Kickoff Presentation**:
   - Prepare a five-minute kickoff presentation.
   - One person from the team will describe the project plan, challenges, team roles, and expected outcomes.
2. **Conclusion Brief**:
   - Prepare a conclusion brief that demos the final product and lists the challenges overcome along the way.

### Section: Docker

1. **Dockerize the Solution**:
   - Ensure the solution runs as a Docker container.
   - Provide a `docker-compose.yml` that will build the environment and allow the Instructor to run the application easily.
  
# Project Plan: Team Collaboration Dashboard

## 1. Project Overview
- **Project Name**: *Team Collaboration Dashboard*
- **Objective**: Develop a web application that allows users to generate AI-assisted meeting notes, summaries, or brainstorming ideas using the Ollama API. The application will be built using Flask, Dockerized for deployment, and integrated with the Ollama API for AI-driven features.

## 2. Scope
- **In Scope**:
  - Develop a Flask-based web application.
  - Create a user-friendly UI for inputting text and viewing AI-generated content.
  - Integrate the Ollama API for text generation and summarization.
  - Dockerize the application using Docker and `docker-compose`.
  - Store session data in a lightweight database (e.g., SQLite).
  - Implement basic testing to ensure functionality.
  
- **Out of Scope**:
  - Advanced AI features beyond basic text generation and summarization.
  - Deployment to a production environment (unless added as a stretch goal).
  - User authentication and multi-user support (unless specifically required).

## 3. Timeline and Milestones
- **Week 1**:
  - **Milestone 1**: Complete Flask backend setup, including API integration and basic routes.
  - **Milestone 2**: Dockerize the Flask application and ensure it runs successfully in a container.
  
- **Week 2**:
  - **Milestone 3**: Develop and connect the UI to the Flask backend.
  - **Milestone 4**: Complete testing, documentation, and prepare a demo of the final product.
  - **Final Milestone**: Deliver a fully functional Dockerized application that can be run and tested by the instructor.

## 4. Team Roles and Responsibilities
- **Project Manager**: Oversees the project, coordinates between team members, and ensures milestones are met.
- **Backend Developer(s)**: Responsible for setting up the Flask server, integrating the Ollama API, and managing the database.
- **Frontend Developer(s)**: Develops the user interface and ensures seamless interaction with the backend.
- **DevOps Engineer**: Handles Dockerization, ensuring the application is containerized and can be easily deployed using `docker-compose`.
- **Tester**: Writes and executes test cases to ensure the application functions correctly, both in development and within Docker.
- **Presenter**: Prepares and delivers the kickoff presentation and the final project demo.

## 5. Architecture
- **Flask Backend**:
  - Routes for handling user input, interacting with Ollama API, and managing session data.
  
- **Frontend UI**:
  - Simple web interface (HTML/CSS/JS) for user interaction.
  
- **Database**:
  - SQLite for storing session data.
  
- **Docker**:
  - `Dockerfile` for creating the Flask application image.
  - `docker-compose.yml` for orchestrating the Flask service and any dependencies.

## 6. Development Workflow
- **Version Control**: Use Git and GitHub for version control. Each team member should work on separate branches and submit pull requests for review.
- **Code Reviews**: Implement code reviews before merging changes into the main branch.
- **Continuous Integration**: Optionally, set up a CI pipeline (using GitHub Actions) to automate testing of the application on each commit.
- **Testing**: Develop test cases for both the backend (e.g., API integration) and frontend (e.g., UI functionality). Ensure tests run successfully within the Docker container.

## 7. Risk Management
- **Risk 1**: API changes or limitations with Ollama may impact development.
  - **Mitigation**: Keep the API integration modular so alternative APIs can be used if necessary.
  
- **Risk 2**: Docker setup issues could delay deployment.
  - **Mitigation**: Test Docker setup early in the project timeline and ensure everyone has a basic understanding of Docker.

## 8. Success Criteria
- A fully functional, Dockerized Flask application that can:
  - Accept user input through the UI.
  - Generate and display AI-driven content using the Ollama API.
  - Run seamlessly in a Docker container with no issues during setup or operation.
  
- Successful presentation of the project plan, challenges faced, and final product.

## 9. Deliverables
- **Codebase**: Complete source code in a GitHub repository.
- **Docker Files**: `Dockerfile` and `docker-compose.yml` for easy deployment.
- **Documentation**: README with setup instructions, API documentation (if applicable), and any other relevant details.
- **Presentation**: A five-minute kickoff presentation and a final demo showing the project in action.

## 10. Communication Plan
- **Regular Meetings**: Weekly check-ins to discuss progress, challenges, and next steps.
- **Collaboration Tools**: Use GitHub Issues and Project Boards to track tasks and progress. Communication via Slack, Teams, or email as needed.

## Scoring Rubric

| Item                                      | Hi Points                                         | Med Points                               | Low Points                               |
|-------------------------------------------|---------------------------------------------------|------------------------------------------|------------------------------------------|
| Tasks Created and Assigned to Milestones     | All tasks are clearly defined and appropriately assigned to milestones. | Most tasks are defined and assigned to milestones, but some lack clarity or are not properly aligned with milestones. | Few tasks are defined, and there is minimal alignment with milestones. |
| GitHub Project Created with Collaborators Invited | GitHub project is created, and all team members, including the instructor, are successfully invited as collaborators. | GitHub project is created, but some collaborators are missing or not invited promptly. | GitHub project is created, but most collaborators are missing, or there was significant delay in inviting them. |
| GitHub Landing Page Has Project Plan Listed Out | The project plan is thoroughly detailed on the GitHub landing page, including objectives, milestones, and team roles. | The project plan is present but lacks some details or clarity in objectives, milestones, or roles. | The project plan is poorly detailed or missing critical information on the GitHub landing page. |
| Delivery of Project Kickoff Presentation  | The kickoff presentation is well-prepared, clearly presented, and covers all aspects of the project, including challenges and roles. | The presentation is delivered but may lack some detail, clarity, or coverage of challenges and roles. | The presentation is poorly prepared, lacks detail, or fails to adequately cover the project scope. |

