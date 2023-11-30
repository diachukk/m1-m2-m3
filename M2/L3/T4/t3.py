'''
Введіть два цілих числа a і b (при цьому a ≤ b). 
Виведіть в стовпчик всі числа від a до b включно.
'''

a=int(input("a:"))
b=int(input("b:"))

if(a<=b):
    for number in range(a,b+1):
        print(number)