max_of_three = lambda a, b, c: max(a, b, c)
print(max_of_three(5, 12, 9))  

celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 68.0, 86.0, 104.0]

