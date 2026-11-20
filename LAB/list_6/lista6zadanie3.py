# Szymon Jaworski, zadanie nr 2 z listy 6

import unittest # import biblioteki obsługującej testy jednostkowe

def addition(*args:float) -> float: #"komentarze"/adnotacje/metadane, :float dane wejściowe powinny być typu float, -> float dane wyjściowe powinny być typu float
    return sum(args)

class test_addition(unittest.TestCase):

    def test_additionRepresentableInBin(self): #Test liczb reprezentowalnych w systemie dwójkowym (liczby które da się zapisać ułamkiem 1/(2^n))
        self.assertEqual(addition(0.5,0.25),0.75) #oczekujemy równego wyniku

    def test_additionNotRepresentaleInBin(self): #Test liczb niereprezentowalnych ---||---
        self.assertAlmostEqual(addition(0.1,0.2,0.3),0.6) #Oczekujemy PRAWIE równego wyniku, domyślnie do 7 liczb po przecinku, bez biblioteki napisalibyśmy abs(a - b) < 1e-7


unittest.main()