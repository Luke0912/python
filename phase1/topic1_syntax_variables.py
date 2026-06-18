"""
=============================================================
PHASE 1 — Topic 1: Python Syntax & Variables
=============================================================
Run this file with:  python3 topic1_syntax_variables.py
=============================================================
"""

# ─────────────────────────────────────────────
# SECTION 1: Basic Variables
# ─────────────────────────────────────────────

name: str = "Shubham"        # string
age: int = 25                # integer
height: float = 5.11         # float
is_active: bool = True       # boolean (capital T!)
nothing = None               # None (equivalent to null)

print("--- Basic Variables ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Active: {is_active}")
print(f"Nothing: {nothing}")

# ─────────────────────────────────────────────
# SECTION 2: Type Checking
# ─────────────────────────────────────────────

print("\n--- Type Checking ---")
print(type(name))             # <class 'str'>
print(type(age))              # <class 'int'>
print(isinstance(age, int))   # True
print(isinstance(name, int))  # False

# ─────────────────────────────────────────────
# SECTION 3: String Interpolation (f-strings)
# ─────────────────────────────────────────────

print("\n--- f-strings ---")
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)

# Expressions inside f-strings
print(f"Next year you'll be {age + 1}")
print(f"Name uppercase: {name.upper()}")

# ─────────────────────────────────────────────
# SECTION 4: Multiple Assignment
# ─────────────────────────────────────────────

print("\n--- Multiple Assignment ---")
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Swap without temp variable
x, y = y, x
print(f"After swap: x={x}, y={y}")

# ─────────────────────────────────────────────
# SECTION 5: Constants (convention)
# ─────────────────────────────────────────────

MAX_RETRIES = 3
API_BASE_URL = "https://api.example.com"
DEBUG_MODE = False

print("\n--- Constants ---")
print(f"Max Retries: {MAX_RETRIES}")
print(f"API URL: {API_BASE_URL}")

# ─────────────────────────────────────────────
# SECTION 6: Dynamic Typing (Python gotcha)
# ─────────────────────────────────────────────

print("\n--- Dynamic Typing ---")
value = 42
print(f"value is: {value}, type: {type(value)}")

value = "now I'm a string"  # totally legal in Python
print(f"value is: {value}, type: {type(value)}")

# Type hints don't enforce — they're just hints for devs and tools
score: int = 100
score = "oops"  # Python won't crash, but mypy would warn you

# ─────────────────────────────────────────────
# EXERCISES (complete below)
# ─────────────────────────────────────────────

"""
EXERCISE 1:
Create variables for a user profile:
  - username (string)
  - followers (integer)
  - rating (float)
  - is_verified (boolean)

Then print a formatted summary using an f-string like:
  "@alice has 1500 followers, rating 4.8, verified: True"
"""

# YOUR CODE HERE


"""
EXERCISE 2:
Create two variables: a = 5, b = 10
Without using a third variable, swap their values.
Print them before and after the swap.
"""

# YOUR CODE HERE


"""
EXERCISE 3:
What is the output of this code? Answer in a comment, then run it to verify.

x = 10
y = "20"
print(x + int(y))
print(str(x) + y)
print(type(x + int(y)))
"""

# YOUR PREDICTION HERE (comment):
# Run it and see if you were right:
x = 10
y = "20"
print(x + int(y))
print(str(x) + y)
print(type(x + int(y)))
