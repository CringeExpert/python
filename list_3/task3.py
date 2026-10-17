# Stwórz obiekt typu str, który przechowuje tekst ±lubowania studenta:
# slubowanie = """
# wst¦puj¡c do wspólnoty akademickiej Uniwersytetu Wrocªawskiego, ±lubuj¦ uroczy±cie:
# - zdobywa¢ wiedz¦ i umiej¦tno±ci,
# - post¦powa¢ zgodnie z prawem, tradycj¡ i dobrymi obyczajami akademickimi,
# - dba¢ o dobre imi¦ Uniwersytetu Wrocªawskiego i godno±¢ studenta.
# """
#  Popraw zmienn¡ slubowanie, aby tekst zaczynaª si¦ wielk¡ liter¡.
#  Korzystaj¡c z funkcji count sprawd¹, ile razy wyst¦puje spójnik i.
#  Korzystaj¡c z funkcji count sprawd¹, ile razy wyst¦puje litera i.
#  Korzystaj¡c z in sprawd¹, czy sªowo Uniwersytet wyst¦puje w tek±cie.
#  Korzystaj¡c z funkcji str.split:(a) stwórz list¦ wyrazów wyst¦puj¡cych w tek±cie (30 sªów => 30 elementów),
# (b) stwórz list¦, której ka»dy element odpowiada jednej linijce tekstu (4 linie => 4 elementy)

slubowanie = '''wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
- zdobywać wiedzę i umiejętności,
- postępowa¢ zgodnie z prawem, tradycji i dobrymi obyczajami akademickimi,
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.'''

slubowanie2 = slubowanie[0].upper() + slubowanie[1:]


print(slubowanie2)
print(slubowanie2.count(" i "))
print(slubowanie2.count("i"))
print("Uniwersytet" in slubowanie2)

words = slubowanie2.split(" ")
print(len(words), words)

rows = slubowanie2.split("\n")
print(len(rows),rows)
