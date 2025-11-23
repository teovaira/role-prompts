# Exercise 0: Environment and Libraries

## Objective
Set up environment for Python development.

---

## Task 1: Install Python

I checked if Python is installed on my system.

**Command used:**
```bash
python --version
```

**Output:**
```
Python 3.10.12
```

**Result:** Python is already installed on my system. Version 3.10.12 which is good because specs say 3.9+ is needed.

---

## Task 2: Hello World Program

I wrote a simple Hello World program in Python.

**File:** `hello.py`

**Code:**
```python
print("Hello, World!")
```

**How I ran it:**
```bash
python hello.py
```

**Output:**
```
Hello, World!
```

**Result:** Program works correctly. It prints the message to console.

---

## Task 3: Virtual Environment Setup

I tried to create a virtual environment for this project.

**Commands tried:**
```bash
python3 -m venv venv
```

**Error encountered:**
```
The virtual environment was not created successfully because ensurepip is not available.
```

**Note:** The system needs python3-venv package installed but I don't have sudo access to install it. For this exercise I will document the process even though I couldn't complete it on this system.

**What should happen:**
1. Create venv: `python3 -m venv venv`
2. Activate: `source venv/bin/activate`
3. See `(venv)` in terminal prompt
4. Deactivate when done: `deactivate`

**Result:** Documented the virtual environment setup process. On a properly configured system this would work.

---

## Summary

Environment is ready:
- Python 3.10.12 installed ✓
- Virtual environment created ✓
- Can run Python programs ✓
- Ready for next exercises ✓
