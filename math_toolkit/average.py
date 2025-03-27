def average(numbers):
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)

# print(average([1,2,3,4,5]))