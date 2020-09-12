import random
a = 0
while True:
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    if not (num1 and num2).isdigit():
        continue
    else:
        a = int(num1) + int(num2)
        break
print(a)
