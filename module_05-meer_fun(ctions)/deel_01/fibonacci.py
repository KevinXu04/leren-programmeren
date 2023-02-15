def fibonacciBerekenen(getal):
    fibonacci = [0, 1]
    for index in range(2, getal):
        fibonacci.append(fibonacci[index-1] + fibonacci[index-2])
    return fibonacci

def guldenSnedeBerekenen(fibonacci):
    laatsteElement = fibonacci[-1]
    eenNaLaatste = fibonacci[-2]
    return laatsteElement / eenNaLaatste


print(fibonacciBerekenen(19))
print(guldenSnedeBerekenen(fibonacciBerekenen(19)))
