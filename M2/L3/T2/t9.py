'''
А тепер перед Вами програма робота-маляра: 
програма запитує колір, яким треба намалювати лінію. 
Зараз робот вміє малювати тільки червону лінію, 
навчіть його малювати також синю (blue) і зелену (green) лінії.
'''

from turtle import *
colors={
    "синій":"blue",
    "зелений":"green",
    "червоний":"red"
}
turtle_color = input("Який колір використовувати?")
if(turtle_color in colors):
    color(colors[turtle_color])
forward(100)
exitonclick()
