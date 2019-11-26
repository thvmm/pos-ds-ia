from random import randint

# Objetivo: Criar uma lista com 10 numeros aleatorios
# Exemplo 1: usando FOR
mylist = []
for i in range(10):
    number = randint(0,10)
    mylist.append(number)
print("Lista Aleatoria:", mylist)

# Exemplo 2: utilizando WHILE
mylist = []
i = 0
while i < 10:
    number = randint(0,10)
    mylist.append(number)
    i += 1
print("Lista Aleatoria:", mylist)

# Exemplo 3: utilizando Compreensão de Listas
mylist = [randint(0,10) for i in range(10)]
print("Lista Aleatoria:", mylist)

# Objetivo: Computer o cubo de cada numero
mylists = [[1,3],[4,5,9],[1,2,3]]
avgs = []

# Exemplo 1: simples
for sublist  in mylists:
    total = sum(sublist)
    average = total / len(sublist)
    avgs.append(average)
print("Lista com medias:", avgs)

# Exemplo 2: utilizando getAverage e FOR
def getAverage(sublist):
    total = sum(sublist)
    average = total / len(sublist)
    return average

avgs = []
for sublist in mylists:
    result = getAverage(sublist)
    avgs.append(result)
print("Lista com medias:", avgs)

# Exemplo 3: utilizando getAverage map
avgs = list(map(getAverage, mylists))
print("Lista com medias:", avgs)

# Exemplo 4: utilizando map e lambda
avgs = list(map(lambda sublist: sum(sublist) / len(sublist), mylists))
print("Lista com medias:", avgs)