"""1. Екі бүтін А және В саны берілген (А ≤ B бар). А-дан В-ға дейінгі барлық сандарды басып шығарыңыз.
Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно."""

import random

num_1 = random.randint(1, 10)
num_2 = random.randint(num_1, 20)

while num_1 <= num_2:
    print(str(num_1))
    num_1 += 1
