'''
Змініть минулу програму так, щоб вона тривала до тих пір, 
поки не буде дана правильна відповідь. 
Для цього умова має бути не в умовному операторі, а в циклі while.
'''

answer="8x"

answerInput=""

while answerInput!=answer:
    answerInput=input("(4x^2)'=")
    if(answer==answerInput):
        print("Вітаю ви відповіли правельно")
    else:
        print("Мені шкода ви невгадали")