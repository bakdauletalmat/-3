"""3. Екі бүтін А және В саны берілген, A>B. А-дан В-ға дейінгі барлық тақ сандарды кему ретімен басып шығарыңыз. Бұл тапсырмада if операторынсыз орындай аласыз.
Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if."""


num_1 = int(input())
num_2 = int(input())
for i in range(num_1 - (num_1 + 1) % 2, num_2 - num_2 % 2, -2): 
    print(i, end=' ')
