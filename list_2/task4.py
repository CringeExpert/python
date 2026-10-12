text = input("Podaj napis: ")

result,letter1 = text[0] * 2

for i in range(1,len(text)):

    if text[i] == letter1:
        result += '$'
    else:
        result += text[i]

print(result)



