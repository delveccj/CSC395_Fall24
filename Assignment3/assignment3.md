# Assignment 3: Sprinting to Success!

## Objective

Your team will have two weeks to complete this assignment. It takes you through two, one-week sprints.  Final delivery of the product happens on October 1!  Here is what your team will need to do.

## Requirements


### **Item 1: Ticket Management**


In this task, your team will be using **GitHub Issues** to manage tickets and track the progress of your project. It is crucial that each ticket created has a **direct connection** to the code being committed. This means that when you work on a task from a ticket, the related code commits should include references to the ticket number (e.g., by mentioning `#ticket-number` in the commit message). 

Your team must demonstrate that:
1. **All team members have contributed** by working on at least one ticket.
2. **Each ticket** worked on has associated code commits that clearly trace back to the issue in GitHub.
3. **Effective use of GitHub issues**: Tickets should be well-defined, with clear descriptions of tasks and acceptance criteria.

You will need to:
- Create well-structured tickets with detailed descriptions.
- Ensure each commit related to a ticket references the ticket number.
- Use GitHub's issue-closing syntax (e.g., `Fixes #ticket-number`) when you complete a task to automatically close the ticket once the work is merged.

Your ability to manage tickets effectively will demonstrate how well you can handle project management and collaboration in a real-world software development scenario.

---

#### **Rubric for Ticket Management** (Total: 15 points)

| Criteria                                  | High (5 points)               | Medium (3 points)               | Low (1 point)                 |
|-------------------------------------------|-------------------------------|---------------------------------|-------------------------------|
| **Ticket Creation & Detail**              | Tickets are well-defined with clear descriptions, acceptance criteria, and assigned to specific team members. | Some tickets are detailed, but others lack clarity or assignment. | Tickets are poorly defined, lacking detail or assignment. |
| **Commit Traceability to Tickets**        | Every code commit is directly linked to a ticket, using the proper GitHub syntax (`#ticket-number`). | Some commits are linked to tickets, but not consistently across all tickets. | Few to no commits are linked to tickets, with poor traceability. |
| **Team Collaboration**                    | All team members have worked on tickets, and the contributions are balanced among the team. | Most team members have worked on tickets, but there are slight imbalances in contributions. | Only a few team members contributed, and contributions are uneven. |
| **Closing of Issues via Commits**         | Issues are consistently closed using the correct GitHub syntax (e.g., `Fixes #ticket-number`). | Issues are closed, but not always using proper GitHub syntax or with some inconsistency. | Issues are rarely closed via commits, with minimal usage of closing syntax. |

---

### **Item 2: Unit Testing and Error Handling**

In this task, your team will focus on writing **unit tests** to validate that your code works as expected, especially when it handles errors and edge cases. Unit tests ensure that each piece of your code (functions, modules) works independently, and they are a critical part of professional software development.

To organize your code:
1. **Create a directory structure** that separates your **live code** from your **test code**. 
   - **Example Directory Structure**:
     ```
     /project-root
       /src          (contains your main code)
       /tests        (contains your unit tests)
     ```
   - This structure helps in keeping your code organized and allows for easy testing.

2. **Focus on key test cases** to cover both normal and failure conditions:
   - **Test Case 1**: What happens if the **JSON input** does not match the expected format? Write a test that provides malformed or incomplete JSON and ensures that your code handles this gracefully (e.g., by returning an error message instead of crashing).
   - **Test Case 2**: What if the **response from the Ollama API** contains junk data or is not as expected? Create a test to simulate receiving incorrect data and validate that your code detects and handles this properly.
   - **Test Case 3**: What happens if the **Ollama client fails to connect**? Your code should be resilient to connection failures, providing a meaningful error message instead of crashing.

3. **Write tests** for these cases, focusing on both **successful scenarios** (where the code works as expected) and **error handling** (where something goes wrong).

4. Use a **test framework** like **`unittest`** in Python. Example template to get started:

   ```python
   import unittest
   from src.ollama_client import OllamaClient  # Import the actual class you're testing

   class TestOllamaClient(unittest.TestCase):
       def test_valid_json_input(self):
           # Example of a test case for valid input
           result = OllamaClient().process_input(valid_json)
           self.assertEqual(result, expected_output)

       def test_invalid_json_input(self):
           # Example of handling invalid JSON input
           with self.assertRaises(ValueError):
               OllamaClient().process_input(invalid_json)

       def test_ollama_connection_failure(self):
           # Simulate the client failing to connect
           result = OllamaClient().connect()
           self.assertEqual(result, 'Connection Failed')

   if __name__ == '__main__':
       unittest.main()
   ```

You will need to:
- Create comprehensive unit tests for **successful execution** and **error handling**.
- Ensure that **all critical scenarios** are covered (like JSON validation, handling failed API calls, etc.).
- Show the output of the test suite to demonstrate passing or failing tests.

---

#### **Rubric for Unit Testing** (Total: 20 points)

| Criteria                                   | High (5 points)                | Medium (3 points)              | Low (1 point)                   |
|--------------------------------------------|---------------------------------|--------------------------------|---------------------------------|
| **Directory Structure & Organization**     | Code and test files are well-organized in separate directories with clear structure. | Code and tests are separated but not consistently organized. | No clear separation between live code and tests; disorganized structure. |
| **Comprehensive Test Coverage**            | Tests cover all critical scenarios (successful cases and failures) comprehensively. | Tests cover some critical scenarios, but important edge cases are missing. | Minimal or no test coverage, with few critical scenarios tested. |
| **Error Handling in Tests**                | Error cases (e.g., invalid JSON, connection failures) are handled gracefully and tested thoroughly. | Some error cases are tested, but coverage is incomplete or insufficient. | Little to no testing of error cases; code may crash in real scenarios. |
| **Use of Python Test Framework (`unittest`)** | Tests are written using Python’s `unittest` framework or similar, with proper assertions and structure. | Tests use the framework but lack structure or completeness (e.g., missing assertions). | Tests do not use a formal framework or are poorly structured, making them hard to evaluate. |
| **Test Output & Results**                  | All tests run successfully with clear output demonstrating both passing and failing cases as expected. | Tests run but may have unclear output or partial success/failure. | Tests fail or do not run properly, with unclear or missing output. |

---

### **Item 3: Baby Integration Test**

In this task, you will write a **simple automated integration test** to ensure that the full system works together as expected. This test will simulate sending a request to your Flask server, which will then call the Ollama API to process the data and return a result. The goal is to prove that all parts of the system (Flask server, Ollama client, and response handling) are functioning properly.

Here’s what you need to do:
1. **Set up the test** to make a **POST request** to your Flask server.
2. Ensure the server processes the request by passing it to the **Ollama API** and returns a valid response.
3. The test should assert that:
   - The **server receives the request** and forwards it correctly to the Ollama client.
   - The **Ollama API responds** with the expected data.
   - The **server’s response** to the client matches the processed data from Ollama.

Use a Python testing library such as `unittest` or `pytest` to automate this test.

Here’s a baby example to get you started:

```python
import unittest
import json
from flask import Flask, jsonify
import requests

class TestIntegration(unittest.TestCase):
    
    def test_integration_with_server(self):
        # Setup test client for your Flask app (assuming it runs on localhost:5000)
        url = 'http://localhost:5000/process'  # Your Flask server endpoint
        headers = {'Content-Type': 'application/json'}
        
        # Simulate sending a JSON payload to the server
        payload = {
            "input": "Tell me a recipe for chocolate cake."
        }
        
        # Send POST request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Check the response status
        self.assertEqual(response.status_code, 200)

        # Assuming your server returns a processed recipe from Ollama
        expected_response = "Here's a great recipe for chocolate cake using cocoa powder and sugar."
        self.assertIn(expected_response, response.text)  # Check that the response contains expected text

if __name__ == '__main__':
    unittest.main()
```

- **Note**: Adjust the `url` to match the route in your Flask server that handles requests to the Ollama API. 

In this example:
- The test **sends a request** with a JSON payload to the server.
- It then **checks the status code** to ensure the request was successful.
- Finally, it **verifies the response** contains the correct processed result (which in your case will be something from Ollama).

### **Rubric for Integration Test** (Total: 10 points)

| Criteria                                     | High (5 points)                           | Medium (3 points)                       | Low (1 point)                          |
|----------------------------------------------|-------------------------------------------|-----------------------------------------|----------------------------------------|
| **Setup and Execution of Test**              | Test correctly sets up a POST request to the Flask server and executes it. | Test is set up but has minor issues in execution or setup. | Test does not properly execute or setup is incorrect. |
| **Correct Handling of Request/Response**     | Test verifies the request is handled by the server and checks the response accurately. | Test checks request/response, but not all aspects are verified. | Minimal or no verification of the request/response. |
| **Automation of Test**                       | Test is fully automated and can be run using `unittest` or `pytest` without manual intervention. | Test is automated but requires some manual setup. | Test is not automated, requiring full manual input. |

---

This **baby integration test** introduces you to testing full-system functionality, ensuring their Flask server and Ollama client are working together as expected. It's simple, automated, and serves as an introduction to more complex integration testing in the future.

### **Item 4: Retrospective Meeting (End of Sprint 1)**

At the end of Sprint 1, your team will participate in a **10-minute retrospective meeting** with the instructor. The goal of this meeting is to reflect on your team’s progress, discuss what’s working well, what challenges you've faced, and how you plan to improve for Sprint 2. This is a critical part of the **agile process**, allowing teams to continuously improve.

**During the meeting, be prepared to discuss:**
1. **What's going well?**
   - What parts of the project are on track and succeeding?
   - Any specific tools, workflows, or team practices that are helping achieve your goals?
   
2. **What challenges have you faced?**
   - What blockers or obstacles have slowed the team down?
   - Are there any technical or collaboration issues that need to be addressed?

3. **What can be improved for Sprint 2?**
   - Identify changes to improve workflow or communication.
   - Plan adjustments that will help tackle remaining tasks more efficiently.

After the meeting, the team is responsible for **documenting the key takeaways**. You must submit a short summary of the discussion, outlining the main points, feedback, and any changes planned for Sprint 2. This summary should be added to your GitHub repository as a **Markdown file** titled `RetrospectiveMeetingNotes.md`.

---

#### **Rubric for Retrospective Meeting** (Total: 15 points)

| Criteria                                  | High (5 points)                                                                 | Medium (3 points)                                                            | Low (1 point)                                                               |
|-------------------------------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Reflection on Progress**                | Team provides a thorough and honest reflection on what is working well in the project. | Team provides some reflection but lacks depth or detail in certain areas.    | Team provides minimal reflection with little insight into progress.          |
| **Identification of Challenges**          | Challenges are clearly identified, with details on specific blockers or areas of difficulty. | Challenges are mentioned, but without much detail or insight.                | Little to no mention of challenges or blockers hindering progress.           |
| **Proposed Solutions for Improvement**    | Team offers thoughtful strategies for improving workflow and addressing challenges in Sprint 2. | Some improvements are suggested, but they are vague or lack concrete plans.  | No clear plan for improvement is proposed, or the team seems unprepared.     |
| **Engagement and Participation**          | All team members contribute to the discussion, showing a clear understanding of the project’s status. | Most team members contribute, but participation is uneven.                   | One or two team members dominate the discussion, or participation is lacking.|
| **Summary Submission (RetrospectiveMeetingNotes.md)** | A clear, concise, and well-organized summary of the retrospective is written and added to the repository as a `RetrospectiveMeetingNotes.md` file. | A summary is submitted but lacks clarity, detail, or organization.           | No summary is submitted, or the submission is incomplete or disorganized.    |

---

This rubric adds accountability by requiring the team to document their reflection in a **Markdown file**, ensuring that they critically assess their progress and have a tangible record of their retrospective discussion. This will help them solidify what they've learned and keep track of improvements going forward.

### **Item 5: Final Presentation Meeting**

In the **final presentation meeting**, your team will showcase the outcome of your project, highlighting what worked, what didn’t, and the lessons learned throughout the development process. This is an opportunity to demonstrate the final product to the class and instructor, provide insights into your team’s journey, and reflect on how you overcame challenges.

Your presentation must include:
1. **Project Overview & Goals**:
   - Begin by recapping the project's goal (The AI-Backed Recipe Maker), and provide a brief overview of the project scope.

2. **Data Flow or System Architecture Diagram (In README.md)**:
   - Include a **basic data flow diagram** in your presentation and project’s `README.md` file. This diagram should illustrate how data moves through your system—from user input, through the Flask server, to the Ollama API, and back to the user.
   - The `README.md` should also contain clear instructions for how to **run the project**, including any dependencies (e.g., Docker, Python libraries) and setup steps.

3. **What Worked & What Didn’t**:
   - Discuss the features or aspects of the project that went smoothly.
   - Talk about what didn’t work as planned and any obstacles the team faced, including technical, team collaboration, or time management challenges.

4. **Lessons Learned**:
   - Each team member should briefly share a key takeaway from the project—whether it's a new technical skill, a lesson in teamwork, or overcoming specific challenges.

5. **Live Demo**:
   - Demonstrate the **working prototype** of the system, showcasing the key functionality (e.g., the web UI, communication with Ollama, results generated from user input).
   - Highlight any major features or components the team is proud of.

6. **Slides**:
   - Create and present a set of **slides** summarizing each section: project overview, data flow, successes/challenges, lessons learned, and demo summary.

---

#### **Rubric for Final Presentation Meeting** (Total: 20 points)

| Criteria                                   | High (5 points)                                                              | Medium (3 points)                                                            | Low (1 point)                                                                |
|--------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Project Overview & Goals**               | Clear, concise, and engaging explanation of the project’s goals and purpose.  | Adequate explanation, but lacks clarity or engagement.                       | Minimal or unclear explanation of the project’s goals.                       |
| **Data Flow Diagram & README.md**          | The README.md includes a well-structured data flow diagram and clear instructions to run the project. | README.md is present but lacks clarity in the data flow or setup instructions. | README.md is missing or poorly written, with incomplete or confusing instructions. |
| **What Worked & What Didn’t**              | Detailed explanation of successes and challenges, with insight into team’s problem-solving. | Covers successes and challenges but lacks depth or reflection.               | Little to no discussion of what worked and what didn’t; minimal reflection.   |
| **Lessons Learned**                        | Each team member shares thoughtful and meaningful lessons from the project.   | Some team members provide lessons learned, but contributions are uneven.     | Minimal or no discussion of lessons learned; lacks personal insights.         |
| **Live Demo**                              | The demo is smooth, engaging, and demonstrates the key features and functionality of the project. | The demo is functional but lacks engagement or is incomplete in showing key features. | The demo is incomplete or fails to show key functionality.                   |
| **Slides & Presentation Quality**          | Slides are well-designed, clear, and support the presentation. The presentation is organized and engaging. | Slides are present but could be improved in design or clarity. Presentation is somewhat disorganized. | Slides are missing or poorly done, and the presentation is disorganized or incomplete. |

---

This rubric ensures that the final presentation reflects the team’s effort throughout the project and highlights their ability to deliver a working solution, reflect on the process, and effectively communicate their results. Including the **data flow diagram** and **README.md** helps reinforce the importance of documentation, while the **live demo** ensures that you have a tangible, functional product to showcase.
