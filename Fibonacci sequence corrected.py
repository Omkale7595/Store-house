def fibonacci_less_than_corrected(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

fibonacci_less_than_corrected(1019)