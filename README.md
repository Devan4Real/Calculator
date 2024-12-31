# Advanced Calculator Program

This repository contains a Python-based calculator capable of evaluating complex mathematical expressions. The program employs structured parsing, supports operator precedence, and handles nested parentheses. It provides an intuitive way to perform arithmetic operations and evaluate expressions using custom functions.

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
  - [Expression Parsing](#expression-parsing)
  - [Operator Precedence](#operator-precedence)
  - [Evaluation Workflow](#evaluation-workflow)
- [Supported Operators](#supported-operators)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Future Enhancements](#future-enhancements)
- [Acknowledgements](#acknowledgements)

## Features
- **Arithmetic Operations**: Supports addition, subtraction, multiplication, division, modulo, and exponentiation.
- **Nested Expressions**: Handles expressions with multiple levels of parentheses.
- **Custom Operator Keywords**: Accepts both symbolic operators (e.g., `+`, `-`) and keyword equivalents (e.g., `add`, `sub`).
- **Error Handling**: Detects and reports invalid inputs, mismatched parentheses, and division by zero.
- **Dynamic Parsing**: Converts infix expressions into structured, evaluable formats.

## How It Works

### Expression Parsing
The program begins by parsing a given input string into a structured list of operators and operands. It uses:
- `get_next`: Extracts the next numeric or operator token from the string.
- `parse`: Processes nested parentheses and transforms the input into a structured representation.

### Operator Precedence
Operator precedence is enforced during parsing by reordering the structured list. This ensures that operations like multiplication and division are evaluated before addition and subtraction. Functions like `struct` manage this precedence.

### Evaluation Workflow
1. **Input Parsing**: Converts a string expression (e.g., `"3 + (2 * 4)"`) into a structured format.
2. **Expression Evaluation**: The structured format is passed to `eval`, which resolves it recursively.
3. **Result Calculation**: The `calc` function computes individual operations, ensuring validity and handling errors.

## Supported Operators
| Operator | Keyword Equivalent | Description        |
|----------|---------------------|--------------------|
| `+`      | `add`              | Addition           |
| `-`      | `sub`              | Subtraction        |
| `*`      | `mul`              | Multiplication     |
| `/`      | `div`              | Division           |
| `%`      | `mod`              | Modulo             |
| `^`      | `pow`              | Exponentiation     |

## Usage
### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/advanced-calculator.git
   ```
2. Run the program in a terminal:
   ```bash
   python calculator.py
   ```
3. Enter mathematical expressions directly, or type `q` or `quit` to exit.

### Example Inputs
```plaintext
> 3 + 5
8

> 2 * (3 + 4)
14

> pow(2, 3) - 5
3
```

## Code Structure

- **`calc(operator, num1, num2)`**: Performs basic arithmetic operations.
- **`eval(expression)`**: Recursively evaluates a structured list of operators and operands.
- **`struct(lst)`**: Ensures operator precedence and groups sub-expressions.
- **`get_next(s, index)`**: Extracts the next token (number or operator) from a string.
- **`parse(s)`**: Converts a raw string into a structured list.
- **`pre_parse(s)`**: Validates parentheses in the input string.
- **`coordinate(s)`**: Combines parsing, validation, and evaluation to compute the final result.

## Future Enhancements
- **Function Support**: Extend the calculator to include functions like `sin`, `cos`, and `log`.
- **Fractional Output**: Provide results as fractions where applicable.
- **GUI Interface**: Create a graphical interface for easier interaction.
- **Improved Error Messages**: Make error messages more descriptive for better debugging.

## Acknowledgements
This calculator is inspired by foundational concepts in computer science, including parsing and recursive evaluation. Special thanks to the Python community for its robust libraries and support.
