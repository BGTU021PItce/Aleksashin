# проверяем делиться нацело или нет

print("введите значение m: ")

m = int(input())

print("Введите значение n: ")

n = int(input())

if m % n == 0:
    c = m // n
    print("Частное от деления: ", c)
elif m % n != 0:
    print("m на n нацело не делится.")