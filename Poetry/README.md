Sure, let's refine the README with your additional instructions and commands:

---

# Poetry

## Overview

This project showcases basic Python functions and unit tests using the Poetry dependency manager. It includes functions for adding numbers and corresponding unit tests.

## Setup Instructions

### 1. Scoop Installation

1. Set the execution policy in PowerShell:
   ```shell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

2. Install Scoop package manager for Windows:
   ```shell
   Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
   ```

### 2. Pipx Installation

1. Install pipx using Scoop:
   ```shell
   scoop install pipx
   ```

### 3. Poetry Installation

1. Install Poetry using pipx:
   ```shell
   pipx install poetry
   ```

### 4. Project Initialization

1. Create a new project directory using Poetry:
   ```shell
   poetry new <project_name>
   ```

## Usage

1. Open the terminal where the `pyproject.toml` file is present.
2. Deactivate any existing virtual environment:
   ```shell
   conda deactivate
   ```
3. Activate the Poetry virtual environment:
   ```shell
   poetry shell
   ```

### Adding Packages

1. Install required packages using Poetry:
   ```shell
   poetry add numpy
   poetry add fastapi
   poetry add pandas
   ```

   - Poetry will automatically update the `poetry.lock` file with the added packages.
   - When sharing the project, others can install the dependencies by running `poetry install`.

## Creating and Running Scripts

1. Navigate to the package folder's parent directory.
2. Create a file named `main.py` in the package folder.
3. Write your Python code in `main.py`. For example:
   ```python
   def add_two_numbers(num1: int, num2: int):
       return num1 + num2

   def my_sum(*num: int):
       return sum(num)

   print(add_two_numbers(2, 2))
   print(my_sum(2, 3, 4))
   ```

4. Save the file.

5. Run the script from the terminal:
   ```shell
   python ./child_folder/main.py
   ```

## Writing and Running Tests

1. Create a file named `test_main.py` in the `test` folder.

2. Write your test codes in `test_main.py`. For example:
   ```python
   from ned.main import add_two_numbers

   # Writing 3 tests for one function
   def test_add_two_numbers_t1():
       assert add_two_numbers(2, 3) == 5

   def test_add_two_numbers_t2():
       assert add_two_numbers(10, 7) == 17

   def test_add_two_numbers_t3():
       assert add_two_numbers(10, 10) != 20
   ```

3. Run the tests from the terminal (where `pyproject.toml` is present):
   ```shell
   poetry run pytest
   ```

   - To run the tests with detailed output:
   ```shell
   poetry run pytest -v
   ```

---

Feel free to further customize this README according to your preferences or project requirements! Let me know if you need any more adjustments.