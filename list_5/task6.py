def harmonic_series(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1/i
    return sum

print(harmonic_series(2))