sum_ = 0
cnt = 0
n = int(input("Введите число: "))

while n != 0:
    sum_ += n
    cnt += 1
    n = int(input("Введите число: "))

print(f"Сумма равна {sum_}")
print(f"Количество введённых чисел равно {cnt}")