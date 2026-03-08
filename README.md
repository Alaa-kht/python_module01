*This project has been created as part of the 42 curriculum by aalkhati.*

# CodeCultivation – Object-Oriented Garden Systems (Plant Types)

## Description
This project is part of the 42 Python curriculum and focuses on **object-oriented programming (OOP)** using Python.

The goal of this exercise is to model a garden system that supports **different types of plants**—flowers, trees, and vegetables—while sharing common characteristics through inheritance.  
Each plant type extends a base `Plant` class and adds its own specific attributes and behaviors.

This project introduces and reinforces:
- Class inheritance
- Code reuse with `super()`
- Encapsulation of shared behavior
- Clean and maintainable object-oriented design

---

## Instructions

### Requirements
- Python 3
- Authorized functions: `print()`, `range()`, `super()`
- Follow the structure and naming conventions required by the subject

### Execution
Run the program from the project directory:

```bash
python3 ft_plant_types.py
Expected behavior
The program:

Creates multiple plant objects of different types

Displays their information in an organized format

Demonstrates each plant’s unique behavior (blooming, producing shade, nutritional value)

Algorithms and Design Choices
Base Class (Plant)
The Plant class contains attributes common to all plants:

name

height

age

This avoids code duplication and centralizes shared behavior.

Inheritance
Specialized classes (Flower, Tree, Vegetable) inherit from Plant using super().__init__():

Flower adds a color attribute and a bloom() behavior

Tree adds trunk_diameter and can produce_shade()

Vegetable adds harvest_season and nutritional_value

Each subclass extends the base class while preserving shared logic.

Design Rationale
This design mirrors real-life biological hierarchies:

All plants share fundamental traits

Each type has specialized characteristics

Changes to common behavior require modification in only one place

This approach improves scalability, readability, and maintainability.

Resources
References
Python Official Documentation
https://docs.python.org/3/

Python Classes and Inheritance
https://docs.python.org/3/tutorial/classes.html

Object-Oriented Programming Concepts
https://realpython.com/python3-object-oriented-programming/

AI Usage
AI tools  were used for:

Clarifying object-oriented programming concepts

Reviewing inheritance structure and code organization

Author
Login: aalkhati

