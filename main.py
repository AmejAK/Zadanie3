def szukaj(lista, liczba):
    for i in range(len(lista)):
        if lista[i] == liczba:
            print("Znaleziono")
    print("Nie znaleziono")

import time
from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]

start=time.time()
szukaj(long_list,-1)
stop=time.time()
print(stop-start)