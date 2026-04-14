number1 = int(input("masukan angka1: "))
number2 = int(input("masukan angka2: "))
number3 = int(input("masukan angka3: "))
if (number3 < number1 > number2):
    print("angka1 lebih besar")
elif (number3 < number2 > number1):
    print("angka2 lebih besar")
elif (number1 < number3 > number2):
    print("angka3 lebih besar")
elif (number3 == number1 > number2):
    print("angka 1 dan 3 lebih besar")
elif (number3 == number2 > number1):
    print("angka 2 dan 3 lebih besar")
elif (number1 == number2 > number3):
    print("angka 1 dan 2 lebih besar")
elif (number1 == number2 == number3):
    print("nilai sama")