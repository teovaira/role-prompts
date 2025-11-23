# Exercise 2: Role-Based Mentoring and Feedback

## Objective
Use role-based prompts for personalized feedback.

---

## The Code

I wrote a simple Python function that has a bug:

**File:** `buggy_code.py`

```python
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Test
result = calculate_average([10, 20, 30])
print(result)
```

**The Bug:** This function will crash if you pass an empty list because it tries to divide by zero.

---

## Prompt to AI Mentor

**My prompt:**
```
Act as a coding mentor reviewing this code. Provide corrections and explain improvements.

Here is the code:

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

result = calculate_average([10, 20, 30])
print(result)
```

---

## AI Mentor Response

**Model Output:**
```
Great job on writing this function! I can see you understand the basic logic of calculating an average. However, there's an important issue we need to address.

**The Problem:**
Your function will crash if someone passes an empty list. Try running:
calculate_average([])

You'll get a ZeroDivisionError because len(numbers) is 0.

**How to Fix It:**
Add a check at the beginning of your function:

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  # or return None, depending on what makes sense
    
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

**Additional Improvements:**

1. You could use Python's built-in sum() function instead of the loop:
   total = sum(numbers)
   
   This is more "Pythonic" and cleaner.

2. Consider what should happen with an empty list. Should it return 0? None? Or raise a meaningful error? Think about what makes sense for your use case.

3. You could add a docstring to explain what the function does:
   """Calculate the average of a list of numbers."""

**Improved Version:**

def calculate_average(numbers):
    """Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Average as float, or 0 if list is empty
    """
    if not numbers:  # More Pythonic than len(numbers) == 0
        return 0
    
    return sum(numbers) / len(numbers)

Keep practicing! The logic was correct, you just needed to think about edge cases. This is something all developers need to learn.
```

---

## Analysis

**How the mentor role influenced the feedback:**

1. **Encouraging tone:** Started with "Great job" instead of just pointing out the error.
2. **Educational approach:** Explained WHY the bug happens, not just HOW to fix it.
3. **Step-by-step guidance:** Showed the problem, then the fix, then improvements.
4. **Multiple suggestions:** Gave several ways to improve, not just one fix.
5. **Pythonic advice:** Taught me about Python best practices like using the built-in sum().
6. **Positive ending:** Encouraged me to keep practicing.

**Brief Analysis:**
The mentor role transforms AI from a code-fixing tool into a teacher ready to educate by using encouraging language, explaining the WHY behind every correction, and providing multiple improvement suggestions rather than just outputting corrected code, proving how role instructions shape both the depth and the pedagogical approach of technical feedback.
