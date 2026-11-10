def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def binomial_coefficient(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))


def pascal(n):
    for i in range(0,n+1):
        tab = []
        for j in range(0,i+1):
            tab.append(str(binomial_coefficient(i,j)))
        print("{:^100}".format(' '.join(tab)))

pascal(5)