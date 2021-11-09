



"""
This function utilzes negative indexing to find the n value of the fibonacci sequence
"""
def fib_finder(n):
    
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence
upper_bounds = int(input("How many fibonacci numbers would you like the program to calculate? "))
fib_sequence = fib_finder(upper_bounds)
user_value = int(input("What fibonacci number would you like to know? (0 based indexing) "))
print(fib_sequence[user_value])
