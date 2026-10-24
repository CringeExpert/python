import string

vowels = ('a','A','e','E','i','I','o','O','u','U','y','Y')

letters = string.ascii_letters;

for l in letters:
    if l in vowels:
        print(f"{l} jest samogłoską")
    else:
        print(f"{l} jest współgoską")


