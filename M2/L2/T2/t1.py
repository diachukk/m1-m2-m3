'''
Виправте помилки. Програма повинна загадувати загадку і повідомляти, чи підходить відповідь.

'''
question = " на базарі не знайдеш, на вагах не вивезеш."
answer = input("Відгадай загадку" + question)
if answer == "сон":
    print("Вгадали!")
else:
    print("Ні... Спробуйте ще раз!")
