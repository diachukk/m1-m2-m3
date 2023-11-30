'''
Потрібно порахувати суму чисел від a до b. 
Програма запитує два числа і виводить результат - одне число.


TODO input:
2
4
TODO output:
9
'''

a=int(input("a:"))
b=int(input("b:"))

step=1 if a<=b else -1

result=0

for number in range(a,b+step,step):
    result+=number

print(f"сума чисел від {a} до {b}:{result}")