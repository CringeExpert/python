x = input("Podaj liczby oddzielone przecinkami (,): ")

l = x.split(',')
ll = [int(x) for x in l]
print(" + ".join(l), " = ", sum(ll))
