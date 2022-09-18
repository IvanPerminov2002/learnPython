#lesson2
#True and False всегда с большой буквы
# ==  != 
#and or - работают всегда с 2-мя булевыми значениями или выражениями
#not - воздействует только на одно булево выражение, следовательно является унарным
#>>> (4<5) and (5<6)
#True
'''приоритет 1. not, 2. and, 3. or
           if else
if name == 'Alice':
   print('Hi, Alice')
else:
   print('Hello, stranger.')

           elif -  помещается только после инструкции if или другой инструкции elif. проверяется лишь в том
случае, если все предыдущие условия оказались ложными, а если оно истинно, то остальные блоки elifпропустятся и выполнится блок else 
if name == 'Alice':
   print('Hi, Alice')
elif age < 12:
    print('You are not Alice.')
else:
   print('Hello, stranger.')
############'''
#
"""
"""

#инструкция while - цикл выполняется до тех пор пока выполняется указанное условие 
#для выхода из бесконечного цикла можно оспользовать ctrl + c
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

#break - условие выхода из цикла
'''
while True:
    print('Please type your name.')
    name = input(0
    if name == 'you name':
        break
print('Thank you!')
'''

#continue
'''когда программа достигает инструкции continue, управление немедленно передается в начало цикла, где
условие вычисляется заново'''
while True:
    print('Who are you?')
    name =  input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

#for
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

print('')
total = 0;
for num in range(101):
    total = total + num
print(total)

print('')
for i in range(12,16):# выведет 12 13 14 15
    print(i)


print('')
for i in range(0, 10, 2):# выведет 0 2 4 6 8 можно range(5, -1, -1)
    print(i)
print('')
#Импортирование модулей, набор модулей называется стандартной библиотекой
import random
for i in range(5):
    print(random.randint(1, 10))
print('')

#randit возвращает случайное число в диапозоне



#преждевременное прекращение выполнения программы 
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')






#round() - округление
#abs() - модуль
#Задание 9. Написать программу, при вводе значения 1 - Hello, 2 -Howdy, при другом - Greetings


print('Enter number:')
spam = input()
if spam == '1':
    print('Hello')
elif spam == '2':
    print('Howdy')
else:
    print('Greetings')

