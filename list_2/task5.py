outside = input("Podaj zewnętrzny napis: ")
inside = input("Podaj środek: ")

middle = len(outside) // 2
left, right = outside[:middle], outside[middle:]

result = left + inside + right

print(result)

