# Stwórz krotk¦ (tuple) zawieraj¡c¡ pi¦¢ cyfr: 0, 1, 2, 3, 4 oraz pi¦¢ literaªów sªownych: "pi¦¢", "sze±¢", "siedem",
# "osiem", "dziewi¦¢".
#  Wydrukuj na ekranie trzy pierwsze elementy.
#  Wydrukuj na ekranie 2 ostatnie elementy.
#  Wydrukuj co drugi element (zaczynaj¡c od drugiego).
#  Korzystaj¡c z funkcji len sprawd¹ ilo±¢ elementów w krotce oraz dªugo±¢ przedostatniego elementu.
#  Niech x oznacza nazw¦ krotki. Wykonaj:
#  x[:5] + (5, 6) + x[-3:]
#  x[:5], (5, 6), x[-3:]
#  porównaj (i wyja±nij) otrzymane wyniki
#  Dodaj pusty literaª sªowny na koniec krotki. Czy mo»esz skorzysta¢ z funkcji append (wyja±nij)?

t = (*range(5),"pięć","sześć","siedem","osiem","dziewięć")
print(t)

print(t[0:3])
print(t[-2:])
print(t[1::2])
print(len(t),len(t[-2]))

print("\n", t[:5] + (5, 6) + t[-3:])
print(t[:5], (5, 6), t[-3:])

#pierwszy wynik to lista niezagnieżdzona wszystkich podanych elementów
#drugi wynik to lista krotek z podanymi elementami

#print(t.append("")) - nie działa ponieważ krotka jest niemutowalna
