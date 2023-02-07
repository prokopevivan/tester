n = int(input("Введите колличество монеток на столе:"))
reshka = 0
orel = 0
for i in range(n):
    storona =int(input(f"Введите какой стороной лежит {i+1} "
                       f"монетка \ n (1 - решка,0-орел):"))
    if storona > 0:
        reshka = reshka + 1
    else:
        orel = orel+1
        if reshka<orel:
            print(f"Нужно перевернуть {orel} монеты.")