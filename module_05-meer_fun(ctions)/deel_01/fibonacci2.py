def fibonacciBerekenen(n, fibonacci=[0, 1]):
    if n <= 2:
        return fibonacci
    
    return fibonacciBerekenen(n-1, fibonacci + [fibonacci[-1] + fibonacci[-2]])

print(fibonacciBerekenen(10))

