"""4. Үстел ойыны үшін 1-ден N-ге дейінгі сандары бар карталар пайдаланылады.Бір карта жоғалады. Қалған карталардың сандарын білу арқылы оны табыңыз.
N саны берілген, содан кейін N − 1 қалған карталардың саны (1-ден N-ге дейінгі әртүрлі сандар). Бағдарлама жоғалған картаның нөмірін көрсетуі керек.
Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.
Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя."""

import random

n = int(input('N: '))
a = random.randrange(1, n)
sum1 = 0

while n > 0:
    sum1 += n
    n -= 1
sum1 -= sum1 - a
print(str(sum1))
