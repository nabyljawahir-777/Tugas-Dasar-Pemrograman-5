numbers = [9, 100, 101, 88, 3, 7]
largest1 = numbers[0]
largest2 = numbers[0]
for i in numbers:
    if (i > largest1):
        largest2 = largest1
        largest1 = i
    elif ( i > largest2 ):
        largest2 = i
print(f"The Second Largest: {largest2}")