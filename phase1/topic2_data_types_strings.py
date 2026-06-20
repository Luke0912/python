"""
=============================================================
PHASE 1 — Topic 2: Data Types & Strings
=============================================================
Run this file with:  python3 topic2_data_types_strings.py
=============================================================
"""

# ─────────────────────────────────────────────
# SECTION 1: Numbers
# ─────────────────────────────────────────────

print("--- Numbers ---")

x: int = 10
y: int = 3

print(x / y)    # 3.3333... (true division, always float)
print(x // y)   # 3         (floor division)
print(x % y)    # 1         (modulo)
print(x ** 2)   # 100       (exponent)
print(round(x / y, 2))  # 3.33

# Underscores in big numbers (readability)
big_number = 1_000_000
print(f"One million: {big_number}")

# Float precision issue (same as JS)
print(0.1 + 0.2)              # 0.30000000000000004
print(round(0.1 + 0.2, 2))   # 0.3

# ─────────────────────────────────────────────
# SECTION 2: Booleans & Truthy/Falsy
# ─────────────────────────────────────────────

print("\n--- Booleans & Truthy/Falsy ---")

# Falsy values
falsy_values = [False, None, 0, 0.0, "", [], {}]
for val in falsy_values:
    print(f"bool({repr(val)}) = {bool(val)}")

print()

# Truthy values
truthy_values = [True, 1, -1, "hello", [0], {"key": "val"}]
for val in truthy_values:
    print(f"bool({repr(val)}) = {bool(val)}")

# Practical: checking if a value exists
print("\n--- Practical Truthy Check ---")
api_response = ""
if api_response:
    print("Got response:", api_response)
else:
    print("No response — would retry in production")

# ─────────────────────────────────────────────
# SECTION 3: String Methods
# ─────────────────────────────────────────────

print("\n--- String Methods ---")

raw_input = "  Hello, World!  "

print(raw_input.strip())          # Remove whitespace
print(raw_input.strip().lower())  # Lowercase
print(raw_input.strip().upper())  # Uppercase
print(raw_input.strip().replace("World", "Python"))
print("a,b,c".split(","))        # ['a', 'b', 'c']
print(",".join(["x", "y", "z"])) # x,y,z
print("hello".startswith("he"))   # True
print("hello".endswith("lo"))     # True
print("hello world".count("l"))   # 3

# ─────────────────────────────────────────────
# SECTION 4: String Slicing
# ─────────────────────────────────────────────

print("\n--- String Slicing ---")

s = "Hello, World!"
print(s[0])     # H
print(s[-1])    # !
print(s[0:5])   # Hello
print(s[7:])    # World!
print(s[:5])    # Hello
print(s[::-1])  # Reversed

# ─────────────────────────────────────────────
# SECTION 5: f-string Formatting
# ─────────────────────────────────────────────

print("\n--- f-string Formatting ---")

price = 19.9
rate = 0.085

print(f"Price:    ${price:.2f}")        # 2 decimal places
print(f"Tax rate: {rate:.1%}")          # percentage
print(f"{'Title':^30}")                 # centered in 30 chars
print(f"{'Left':<30}|")                # left aligned
print(f"{'Right':>30}|")               # right aligned

# ─────────────────────────────────────────────
# SECTION 6: Multiline Strings (LLM Prompts)
# ─────────────────────────────────────────────

print("\n--- Multiline Strings ---")

# This is how you'll write LLM prompts in production
system_prompt = """
You are a helpful AI assistant.
Always respond in a professional tone.
Keep answers concise and accurate.
""".strip()

print(system_prompt)
print(f"Prompt length: {len(system_prompt)} characters")

# ─────────────────────────────────────────────
# EXERCISES
# ─────────────────────────────────────────────

"""
EXERCISE 1: Number Operations
Write a function... wait, we haven't done functions yet.
Just write the code directly.

Given:
    price = 49.99
    quantity = 3
    discount_rate = 0.10  (10% discount)
    tax_rate = 0.18       (18% GST)

Calculate and print:
    1. Subtotal (price * quantity)
    2. Discount amount
    3. Price after discount
    4. Tax amount (on discounted price)
    5. Final total (after discount + tax)

Format all money values to 2 decimal places using f-strings.
Expected output format:
    Subtotal:        ₹149.97
    Discount (10%):  ₹14.99
    After discount:  ₹134.97
    Tax (18%):       ₹24.29
    Final Total:     ₹159.27
"""

# YOUR CODE HERE


"""
EXERCISE 2: Truthy/Falsy Quiz
Before running this, write your prediction as a comment.
Then run and verify.

print(bool("False"))     # ?
print(bool(""))          # ?
print(bool(0))           # ?
print(bool([]))          # ?
print(bool([0]))         # ?
print(bool(None))        # ?
print(bool(-1))          # ?
"""

# YOUR PREDICTIONS HERE (as comments):
# bool("False")  = ?
# bool("")       = ?
# bool(0)        = ?
# bool([])       = ?
# bool([0])      = ?
# bool(None)     = ?
# bool(-1)       = ?

# Now run it:
print("\n--- Exercise 2: Truthy/Falsy ---")
print(bool("False"))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool([0]))
print(bool(None))
print(bool(-1))


"""
EXERCISE 3: String Sanitizer
You're building an AI chatbot backend.
User inputs often arrive dirty — extra spaces, wrong case, etc.

Given this raw user input:
    raw = "  WHAT is machine LEARNING?  "

Write code to:
    1. Strip whitespace from both ends
    2. Convert to lowercase
    3. Capitalize only the first letter (use .capitalize())
    4. Check if the string ends with "?"
    5. Print the word count (hint: split by spaces, check the length)
    6. Build and print this final prompt string:
       User asked (N words): <cleaned question>

Expected output:
    Cleaned: What is machine learning?
    Ends with ?: True
    Word count: 4
    User asked (4 words): What is machine learning?
"""

# YOUR CODE HERE
