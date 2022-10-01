#date: 30.09.2022
#Списки и кортежи
#Список - это знаяение, которое представляет собой коллекцию значений, образующих упорядоченную последовательность [элемент списка]
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
#доступ через индексы
print(spam[1])
print('Hello ' + spam[3])
#Элементы списков могут ыбть списками
sp = [['cat', 'bat', 'rat', 'elephant'], [10, 20, 30, 40, 50]]
print(sp[0][1]) #output: bat
#отрицательные индексы
print(spam[-1])
print(spam[-2])
#Получение части списка с помощью среза. Срезы позволяют получать сразу несколько значений в виде нового списка
print(spam[1:3]) #срез второе число конец среза, но не включается
#сокращенная запись среза, отсутсвие первого знаяения - с 0 элемента, отсутсвие второго - допоследнего
print(spam[:2])
print(spam[1:])
print(spam[:])
#длина списка len()
print(len(spam))
#изменение значений списка с помощью индексов
spam[1] = 'fox'
spam[3] = 12345
print(spam)
#конкатенация и репликация списков, выполняется так же как и в строках 
#[1, 2, 3] + ['a', 'b', 'c'] -> [1, 2, 3,'a', 'b', 'c']
#[1, 2, 3] * 3 -> [1, 2, 3, 1, 2, 3, 1, 2, 3]
#Удаление значений с помощью инструкции del(), можно удалять и простые переменные
del spam[2]
print(spam)

#date: 01.10.2022
#Работа со списками 
#allMyCats.py добовление элементов списка с помщью клавиатуры
#for in list
print()
print('for  и список')
supplines = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplines)):
    print('Index ' + str(i) + ' in supplines is: ' + supplines[i])
#in, not in
#myPets.py

#Груповое присваивание, число перменных должно совпадать с длиной списка
print()
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size, color, disposition)

#Комбинированные операторы присваивания +-*/%
spamm = 25
print(spamm)
spamm += 1
print(spamm)
#можно использовать комбинированные операторы присваивания для конкатенации и репликации строк
print()
spammm = 'Hello'
spammm += ' world'
print(spammm)
bacon = ['Zophie']
bacon *= 5
print(bacon)

#Методы




