numbers = []

for i in range(100,401):
    number = ''

    for j in str(i):

        if int(j) % 2 == 0:
            number += j
            
        else: 
            number = None
            break

    numbers.append(number) if number else None

print(numbers)