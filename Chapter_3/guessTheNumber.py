#игра в угадывание чисел
import random
secretNumber = random.randint(1, 20)
print('Мною здумано число в интервале от 1 до 20. Попробуй его угадать.')

#6 попыток
for guessesTaken in range(1, 7):
	print('Ваш вариант:')
	guess = int(input())
	
	if guess < secretNumber:
		print('Предложенное число меньше задуманного')
	elif guess > secretNumber:
		print('Предложенное число больше задуманного')
	else:
		break #Угадал
if guess == secretNumber:
	print('Верно! Количество попыток: ' + str(guessesTaken))
else:
	print('Нет. Было задумано число ' + str(secretNumber))

