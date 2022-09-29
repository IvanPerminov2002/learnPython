def spam():
	 global eggs
	 eggs = 'spam' #Это глобальная переменная
	 
def bacon():
	eggs = 'bacon' #это локальная переменная
	
def ham():
	print(eggs) #Это глобальная переменная

eggs = 42 #Это глобальная переменная
spam()
print(eggs)

