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

Let's run our first Docker container.  This is the beauty of Docker - it is simple to run application environments:

https://hub.docker.com/r/ollama/ollama

Now, let's move onto Step 5, Substep 2.  We will do more exercises with Docker in class.  But you need to have confidence you can use these technologies!

## Assignment 2 Tasks

Task deliverables will be submitted to D2L.  A Dropbox will be created for each team once team membership has been decided.

### Task 1: Create a GitHub Project

- Someone from your team must create a private GitHub repository.
- It must be named:  CSC395_Team#  where # is your teams number.
- Invite the other team members and the instructor as collaborators.
- You do not need to restrict the project to only accept pull requests initially.  We may add that later!

### Task 2: Create the Tickets

You will have two weeks of development time to create a prototype that implements the prodcut vision.  The two weeks will begin the day Assignment 1 is due (September 17, 2024).  You schedule should have multiple milestones and tasks assigned to them.  For Task 2 you should perform the following activites.

1. **Discuss the Vision**:
   - Your team needs to discuss what the vision means and how to implement it in code.
2. **Create the Tickets**:
   - Break down the project into manageable tasks and create GitHub issues (tickets) for each.
3. **Organize into Milestones**:
   - Add the tickets to two one-week sprints.
4. **First Week Milestone**:
   - Minimally, ensure the first week ends with a milestone that represents a significant progress checkpoint.
5. **Final Project Milestone**:
   - Minimally, the second week should culminate with the final product ready for review.

### Task 3: Create Written Project Plan

   - Create a professional document that explains the architecture, the development plan, how the work will proceed, and how progress will be measured.
   - The minimally required sections of the plan are included at bottom.
   
### Task 4: Create a Kickoff Brief

**Kickoff Presentation**:
   - Prepare a five-minute (timed!) kickoff presentation.
   - One person from the team will describe the project plan, challenges, team roles, and expected outcomes.
   - The plan will be presented in class on Septemebr 17.  Each team will present its plan.  Expect questions along the way - as though the BD person were in the room.

### Task 5: Archive of Communicaiton and Research Acitivites
   - A Discord room has been created for each team.  The team must use this room and show demonstrable proof teammates communicated often on the progress of the project.  It is a common practice for development efforts to have chat rooms where chats themselves become important documentation archives.
   - You will end up using a chat agent to find information and answer questions and develop code examples.  This is perfectly fine.  However, you must do the following:
   - Each team member must obtain an account with ChatGPT OpenAI
   - They must create a chat session named discordusername_Assignment2
   - Any discussions relative to this project should occur in that chat session
   - The URL to the chat session must be supplied to the instructor.  It should be included in both the Project Plan and the (eventual) final report updated with all the content.


The software engineering community (and every other discipline!) is at an inflection point in history.  There will be the way work was performed before LLMs (legacy workflow systems) and the way it was performed after LLMs.  Eveyrone is learning how to use this technology.  Students need to walk a fine line where they (hoepfully) learn from the LLM and not have it simply provide answers for which they have no understanding.  The instructor wants to help guide students on how to use technologies like ChatGPT effectively, so they are able to answer questions but also learn the crtical skills they need.


## Project Plan Template

Below is a template for the project plan.  It has been filled in with some example content for your review.  Your plan must:

- Be 11 point font, Times New Roman.
- Spacing can be 1.5
- Must have a footer filled in with Team name, Project Plan, and page number.
- Must have a cover page that includes 

  **Team Name**
  
  **Project Plan for Recipe Maker**

  **Date Submitted**

  **POC: email address of a team member**

Here are the sections the plan must have. Section 5 must have a professional diagram of the components of your system.

## 1. Objective

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
- **Collaboration Tools**: Use GitHub Issues and Project Boards to track tasks and progress. Communication via Discord or email as needed.

## 11. OpenAI ChatGPT URLs
- This should contain a listing of the chat rooms each team member has used to assist in development of this project.


## Scoring Rubric
### Scoring Rubric for Assignment 2

| **Item**                                             | **Hi Points**                                   | **Med Points**                                   | **Low Points**                                   | **Points Awarded** |
|------------------------------------------------------|----------------------------------------------------|----------------------------------------------------|----------------------------------------------------|-------------------|
| **Task 1: GitHub Project Setup**                     | Repo is private, all members and instructor invited; repo properly named as required | Repo created, but naming or member invitation is incomplete | Repo created, but major issues like incorrect privacy setting or missing collaborators |                   |
| **Task 2: Tickets and Milestones**                   | All tasks created as GitHub tickets, organized into two clear sprints with proper milestones for progress and completion | Some tasks created, but missing key tickets or unclear milestones | Minimal tickets or milestones created, unstructured approach to task management |                   |
| **Task 3: Written Project Plan**                     | Detailed, professional plan explaining architecture, tasks, team roles, and progress metrics | Some sections present but lacking detail, missing key parts of architecture or plan | Incomplete, unclear project plan missing key components or vague approach |                   |
| **Task 4: Kickoff Brief Presentation**               | Well-prepared, timed 5-minute presentation covering all key aspects (plan, challenges, roles); questions handled effectively | Some parts presented well but lacking depth or clarity on key points | Incomplete presentation, poor timing or unclear plan, missing key elements |                   |
| **Task 5: Communication Archive**                    | Regular communication in Discord, comprehensive chat archive submitted, all team members use ChatGPT sessions | Communication occurred but inconsistently or missing some team members’ participation | Minimal communication or missing proof of chat archives, lack of involvement from multiple team members |                   |

### Total Points for Each Task

| **Task**                                | **Hi Points (Max)** | **Med Points** | **Low Points** |
|-----------------------------------------|---------------------|----------------|----------------|
| Task 1: GitHub Project Setup            | 5                   | 3              | 1              |
| Task 2: Tickets and Milestones          | 10                   | 5              | 2              |
| Task 3: Written Project Plan            | 10                   | 5              | 2              |
| Task 4: Kickoff Brief Presentation      | 5                   | 3              | 1              |
| Task 5: Communication Archive           | 5                   | 3              | 1              |
