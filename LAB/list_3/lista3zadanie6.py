# Szymon Jaworski, zadanie nr 6 z listy 3

x = input("Podaj liczby oddzielone przecinkami (,): ")  #pobranie ciągu liczb od użytkownika

l = [s.strip() for s in x.split(',')]          #podział po przecinku i usunięcie spacji
ll = [int(i) for i in l]                       #konwersja stringów na liczby całkowite
print(f"{' + '.join(l)} = {sum(ll)}")          #wypisanie działania i sumy