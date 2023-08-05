# Refactor - AI-Based Code Refactor Tool

Refactor is an AI-based code refactor tool designed to assist developers in automatically improving the quality of their Python code. The tool uses natural language processing and machine learning techniques to suggest code refactoring options, helping developers write cleaner, more maintainable, and efficient code.

## Features

- AI-powered Code Refactoring: Leverage the power of deep learning to get suggestions for code improvements and refactoring.
- Syntax-Aware Refactoring: The tool understands Python syntax and ensures that suggested refactorings are valid and maintain the code's correctness.
- User-Friendly Interface: Intuitive command-line interface for ease of use and quick integration into existing workflows.

## Requirements

- Python 3.x
- TensorFlow (Install using `pip install tensorflow`)

## Installation

- Clone this repository to your local machine:

```bash
git clone https://github.com/Hybried8/Refactor.git
cd Refactor
```
- Install requirements
```
pip install -r requirements.txt
```
## Usage
- Run the tool and provide your Python code for refactoring:
```
python refactor.py
```
- Enter your Python code when prompted, and the tool will suggest refactoring options based on the AI model.
- Review the suggestions and apply the desired refactorings to your code.

## Example Usage
```
# Sample Python code before refactoring
def calculate_area(radius):
    pi = 3.14
    return pi * radius * radius

# AI Suggested Refactoring:
def calculate_area(radius):
    return 3.14 * radius * radius
```
