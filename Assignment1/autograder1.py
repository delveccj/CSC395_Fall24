import os
import subprocess
from git import Repo

# Path to the cloned student's repository
REPO_PATH = "/path/to/student/repo"

# Expected files and directories
expected_files = [
    "README.md",
    "LICENSE",
    "tokens.py",
    "tests/test_tokens.py",
    ".gitignore",
    "images/screenshot.png",
]

def check_file_exists(file_path):
    return os.path.isfile(file_path)

def check_directory_exists(dir_path):
    return os.path.isdir(dir_path)

def check_commit_message(repo, expected_message):
    for commit in repo.iter_commits():
        if expected_message in commit.message:
            return True
    return False

def check_function_in_file(file_path, function_name):
    with open(file_path, 'r') as file:
        content = file.read()
        return f"def {function_name}(" in content

def check_branch_exists(repo, branch_name):
    return branch_name in [branch.name for branch in repo.branches]

def check_test_result(repo_path):
    result = subprocess.run(
        ["pytest"], cwd=repo_path, capture_output=True, text=True
    )
    return "passed" in result.stdout

def grade_assignment(repo_path):
    score = 0
    total = 10  # Total points available

    # Initialize Git repository object
    repo = Repo(repo_path)

    # Check for README.md and its content
    if check_file_exists(os.path.join(repo_path, "README.md")):
        score += 1

    # Check for LICENSE
    if check_file_exists(os.path.join(repo_path, "LICENSE")):
        score += 1

    # Check for tokens.py and its functions
    tokens_path = os.path.join(repo_path, "tokens.py")
    if check_file_exists(tokens_path):
        if check_function_in_file(tokens_path, "readandcount"):
            score += 2
        if check_function_in_file(tokens_path, "readandcount_as_dict"):
            score += 2

    # Check for test files
    if check_file_exists(os.path.join(repo_path, "tests/test_tokens.py")):
        score += 1

    # Check for .gitignore
    if check_file_exists(os.path.join(repo_path, ".gitignore")):
        score += 1

    # Check for the images directory and screenshot
    if check_directory_exists(os.path.join(repo_path, "images")) and check_file_exists(os.path.join(repo_path, "images/screenshot.png")):
        score += 1

    # Check for branch creation and existence
    if check_branch_exists(repo, "branch1"):
        score += 1

    # Check if the student made the correct commit
    if check_commit_message(repo, "First commit for CSC 395"):
        score += 1

    # Check if tests passed
    if check_test_result(repo_path):
        score += 1

    return score, total

# Run the grading script
score, total = grade_assignment(REPO_PATH)
print(f"Score: {score}/{total}")
