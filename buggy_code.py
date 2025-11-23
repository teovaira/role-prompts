# Buggy code for Exercise 2
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# Test
result = calculate_average([10, 20, 30])
print(result)
