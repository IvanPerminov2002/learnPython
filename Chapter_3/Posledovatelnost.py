#Последователность Коллатца всегда завершается 1
def collatz(number):
	if number % 2 == 0:
		number = number // 2
		print(number)
	else:
		number = 3 * number + 1
		print(number)
	return number

print()
print('Введите число:')
while True:
	try:
		num = int(input())
		break
	except ValueError:
		print('Error: Invalid Argument, use argement type int')

while num != 1:
	num = collatz(num)
