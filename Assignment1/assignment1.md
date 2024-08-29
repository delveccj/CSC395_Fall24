# Assignment 1: Getting Familiar with Git

You will need to create a text document you submit to D2L to complete this assignment.

## Section 1: Intro Exercises

1. **Create a Project**:
   - Create a new project on GitHub.
   - Set the project to **Private**.
   - Add a `README.md` file to the project.
   - Add a .gitignore and make the template be Python.
   - Add a license to your project.
   - Create the project.
   - Invite me as a collaborator (GitHub username: `delveccj`).

## Section 2: Configure git and gh

1. Open a terminal.
2. Install git if if is not installed.  Here are the steps:

```
sudo apt update
sudo apt install git
```
3. Set your GitHub id and email:
```
git config --global user.name "Your Github User Name"
git config --global user.email "your.email@example.com"
```
4. Install gh if it is not installed.  Here are the steps:
```
sudo apt update
sudo apt install gh
```
5. Login to GitHub via gh
```
gh auth login
```
There are two ways to do this.  You will need to figure out which one you want to use.

6. Confirm gh login

Type the following command:
```
gh auth status
```
Copy and paste the output into the text file you will submit to D2L

## Section 3: Cloning the Project

From the terminal, clone the project.  You should clone using SSH.  Like so
```
git clone git@github.com:yourusername/yourrepository.git
```
Do an ```ls``` and then ```cd``` into the directory.  Make certain the contents of the git repo you created are there.

## Section 4: Editing Content

1. Edit the ```README.md``` markdown file.
2. Add the following to it and have the markup be bold faced

**My Intro Github Project**

**Your Name**

**Date Completed: Date**

3.  Do a ```git add README.md```
4.  Do a ```git commit -m "My first commit"```
5.  Do a ```git push```.  You may need to set the remote origin for this to work! It will be something like this: ```git remote add origin git@github.com:yourusername/yourrepository.git```

## Section 4: Add a Python File**:

1. Create a Python file named `tokens.py`.
2. In this file, write a function named `readandcount` that reads in a text file and counts the number of tokens (words).
3. Run the command ```git status```.  Copy and paste the output into the text file you will submit to D2L.  It should show the file is Untracked.
4. Add the file and then commit it.
5. Run the command ```git status```.  Copy and paste the output into the text file you will submit to D2L.  It should show there is nothing to commit.
6. Perform a ```git push```

This super easy lab is now over!  But remember - its week one and this is a small lab.
