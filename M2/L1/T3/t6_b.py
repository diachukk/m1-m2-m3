'''
Програма радить, що робити далі. 
Вона може надрукувати один з трьох рядків - "Вчитися!", "Грати!", "Гуляти!", 
Запитуючи, чи зроблені уроки і гарна погода.


Напишіть програму: спочатку задається питання, чи зроблені уроки. 
Якщо відповідь "так", то програма запитує, чи гарна погода. 
Якщо на питання про уроки ми отримали відповідь "ні", потрібно надрукувати "Вчитися!". 
Якщо на питання про хорошу погоду отримана відповідь "так", програма друкує "Гуляти!",
Інакше (значить, погода погана) - друкує "Грати!".
'''

isHomeWorck=input("чи зроблені уроки?").lower()=="так"
isGoodWeather=False
if(isHomeWorck):
    isGoodWeather=input("чи гарна погода?").lower()=="так"
else:
    print("Вчитися!")

if(isHomeWorck and isGoodWeather):
    print("Гуляти!")
elif(isHomeWorck and not isGoodWeather):
    print("Грати!")