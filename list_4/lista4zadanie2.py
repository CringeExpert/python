# Szymon Jaworski, zadanie nr 2 z listy 4

x = int(input("Liczba: "))                          #wczytanie liczby


ans = ["parzysta","nieparzysta"]                    #lista odpowiedzi indeksowana resztą
print(f"Liczba {x} jest {ans[x%2]}")                #wersja bez if