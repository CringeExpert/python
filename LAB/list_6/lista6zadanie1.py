# Szymon Jaworski, zadanie nr 1 z listy 6

import unittest # import biblioteki obsługującej testy jednostkowe

def sorted_asc(lst): # definicja funkcji
    return lst == sorted(lst) 
#Wartość logiczna,
#posortowana lista ->       True
#nieposortowana lista ->    False

class sortTest(unittest.TestCase): #Klasa testu jednostkowego, argument pozwala na przekazanie metod z unittest.TestCase

    #self to odwołanie do stworzonego obiektu

    def test_sorted(self): #przypadek posortowanej listy -> zakładamy True
        self.assertTrue(sorted_asc([1,2,3,4]))

    def test_not_sorted(self): #przypadek nieposortowanej listy -> zakładamy False
        self.assertFalse(sorted_asc([1,2,3,2])) 

unittest.main() #wywołanie metody przeprowadzającej test jednostkowy