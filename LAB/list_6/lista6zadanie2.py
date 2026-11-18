# Szymon Jaworski, zadanie nr 2 z listy 6

import unittest # import biblioteki obsługującej testy jednostkowe

def isPalindrome(string) -> bool: #definicja funkcji, -> to taki "komentarz" adnotacja typu - jaki typ danych ma być na wyjściu
    string = str(string) #zamiana na string
    return string == string[::-1] #Porównanie stringa z jego odwrotnością

class test_isPalindrome(unittest.TestCase): #klasa testu jednostkowego

    def test_int(self): 
        self.assertTrue([isPalindrome(202)]) #Poprawne działanie na l. całk.

    def test_float(self):
        self.assertTrue([isPalindrome(21.12)]) #Poprawne działanie na l. ułamkowych.
    
    def test_string(self): 
        self.assertTrue([isPalindrome("OllO")]) #Poprawne działanie na stringu (taka sama wielkość liter)

    def test_stringNotCaseSensitive(self):
            self.assertTrue([isPalindrome("Ollo")]) #Poprawne działanie na stringu (inna wielkość liter, program ma nie uwzględniać wielkości liter)

    def test_list(self):
        self.assertTrue([isPalindrome(["1","O",3,"O",1])]) #Poprawne działanie na liście z różnych typem danych
    
unittest.main() #wywołanie metody przeprowadzającej test jednostkowy