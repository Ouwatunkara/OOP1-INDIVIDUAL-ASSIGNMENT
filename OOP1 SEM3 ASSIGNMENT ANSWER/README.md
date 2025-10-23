# Mini Library Management System

This is an individual assignment for the Object-Oriented Programming 1 module, implementing a Mini Library Management System using fundamental Python data structures (lists, dictionaries, tuples) and functions, without using any classes or OOP concepts.

## Instructions to Run the Code

To run the system demonstration, ensure **Python 3.x** (e.g., Python 3.12) is installed on your machine.

1.  **Navigate** to the `library/` directory.
2.  **Run the demonstration script** from your console/terminal:
    ```bash
    python demo.py
    ```
    This script will initialize the system and perform a sequence of CRUD (Create, Read, Update, Delete) and Borrow/Return operations, printing the system's state after key actions.

3.  **To run the unit tests**, execute the `tests.py` file:
    ```bash
    python tests.py
    ```
    This will run a series of assert statements to validate the functionality, including edge cases like borrowing an unavailable book or deleting a member with outstanding loans. Any failed test will raise an `AssertionError`.