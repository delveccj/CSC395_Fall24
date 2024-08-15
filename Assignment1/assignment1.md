# Assignment 1: Getting Familiar with Git

## Section: Intro Exercises

1. **Create a Project**:
   - Create a new project on GitHub.
   - Set the project to **Private**.
   - Invite me as a collaborator (GitHub username: `delveccj`).
   - Add a `README.md` file to the project and make it look **pretty**.

## Section: Adding Content

1. **Add a License**:
   - Add a license to your project. You can choose an appropriate open-source license (e.g., MIT, GPL).

2. **Add a Python File**:
   - Create a Python file named `tokens.py`.
   - In this file, write a function named `readandcount` that reads in a text file and counts the number of tokens (words).

3. **Commit Your Changes**:
   - Commit your changes with the message: `"First commit for CSC 395"`.

4. **Push to GitHub**:
   - Push your commit to the GitHub repository.

## Section: Tests and .gitignore

1. **Create a Test**:
   - Create a test that reads in a file containing the Gettysburg Address.
   
2. **Add the Gettysburg Address**:
   - Create a file named `gettysburgaddress.txt` and paste the content of the Gettysburg Address into it.

3. **Test Token Count**:
   - Use the `readandcount` function to count the tokens in the Gettysburg Address and ensure the test passes.

4. **Capture the Test Result**:
   - Take a screenshot of the passing test and place it in a folder named `images`.

5. **Update `.gitignore`**:
   - Add the `gettysburgaddress.txt` file to your `.gitignore` to ensure it is not pushed to GitHub.

6. **Commit and Push**:
   - Add the `images` directory to your Git repository.
   - Push your changes to GitHub.

## Section: Branch Creation

1. **Create a New Branch**:
   - Create a branch named `branch1`.

2. **Switch to the New Branch**:
   - Switch to the newly created `branch1`.

3. **Augment the `tokens.py` File**:
   - Modify `tokens.py` to add a new function that turns the token counts into a dictionary.

4. **Create a Supporting Test**:
   - Write a test using the Gettysburg Address to count the occurrences of the words `"in"` and `"we"`.

5. **Commit and Push**:
   - Commit the changes and push them to the `branch1` branch on GitHub.

## Section: Merge Branch

1. **Create a Pull Request**:
   - Create a pull request to merge `branch1` into `main`.

2. **Merge the Pull Request**:
   - Merge the pull request into the `main` branch.
