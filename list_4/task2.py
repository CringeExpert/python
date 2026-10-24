x = 3

if (x % 2 == 0):
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')

ans = ["parzysta","nieparzysta"]
print(f"Liczba {x} jest {ans[x%2]}")