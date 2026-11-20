#Szymon Jaworski, 367072, Grupa 1
#Zadanie 1
import cmath

z = complex(input("Podaj liczbę zespoloną np. (3+4j): "))

z_modul = abs(z)
z_faza = cmath.phase(z)


wynik = cmath.exp(cmath.pi*cmath.sqrt(z))
wynik_real = wynik.real
wynik_imag = wynik.imag

print(f"{'Część rzeczywista: ':<20} {wynik.real}\n{'Część urojona: ':<20} {wynik.imag}")
