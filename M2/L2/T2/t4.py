'''
Напишіть програму, яка три рази задає питання і 
три рази каже однакові фрази на відповіді «так» і «ні».
Приклади питань написані в програмі нагорі. 
Відповіді повинні бути або "Чудово! 
Ви талант!" (На відповідь "так") або 
"Ви можете навчитися, якщо захочете!"
'''

# Поставте три питання, наприклад:
# "Ви вмієте грати на піаніно?"
# "Ви вмієте грати в футбол?"
# "Ви вмієте грати в футбол?"
# запам'ятовуйте відповіді в змінну:
# Answer = input ()


questions=["Ви вмієте грати на піаніно?","Ви вмієте грати в футбол?","Ви вмієте програмувати на Python?"]

for question in questions:
    answer =input(question)
    if answer == "так":
        print("Чудово! Ти талант!")
    else:
        print("Ти можеш навчитися, якщо захочеш!")
