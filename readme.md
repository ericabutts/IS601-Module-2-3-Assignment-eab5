# Python Calculator REPL
Advanced Object-Oriented Programming: Complete Calculator Implementation

Erica Butts
October 6, 2025
IS 601
## Overview

This project is an advanced **Python Calculator** with a REPL (Read-Eval-Print Loop) interface.  
It supports basic arithmetic operations, operation history, undo/redo functionality, logging, and flexible configuration via environment variables.  

The project is structured with modular design principles and implements several **software design patterns** to make the calculator extensible and maintainable.

---

## Features

- REPL interface: Interactive prompt to perform calculations.
- Supports basic operations: addition, subtraction, multiplication, division.
- Undo/Redo functionality for operations.
- History tracking with optional CSV persistence.
- Logging for monitoring operations and errors.
- Configurable via `.env` file or environment variables.
- Modular design for easy extension with new operations.

---

## Design Patterns

This project utilizes several well-known design patterns:

1. **Strategy Pattern**  
   - Used for operations (add, subtract, multiply, divide).  
   - Each operation implements a common interface and can be swapped at runtime.
   
2. **Observer Pattern**  
   - Used for logging observers that respond when a new operation is performed.  
   - Enables separation of core calculator logic and logging functionality.

3. **Singleton / Configuration Management**  
   - `CalculatorConfig` ensures a single source of configuration for the entire app.
   
4. **Command Pattern (Undo/Redo)**  
   - Each calculation can be treated as a command stored in history.  
   - Undo/Redo functionality is implemented by maintaining stacks of previous and future commands.

---

## Installation

Clone the repository and set up the virtual environment:

```bash
git clone https://github.com/kaw393939/module5_is601.git
cd module5_is601
python -m venv .venv        # Create virtual environment
# Activate environment:
# Windows
.venv\Scripts\activate
# Linux / Mac
source .venv/bin/activate
pip install -r requirements.txt
