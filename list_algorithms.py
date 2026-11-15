numbers = []
for i in range(5):                             # цикл для образования списка
    i = int(input("Введите число: "))
    numbers.append(i)

cnt = 0                                        # переменная для суммы
k = 0                                          # переменная для количества чисел
for i in range(len(numbers)):
    cnt += numbers[i]
    k += 1

sr_arifm = cnt/k                               # рассчет среднего арифметического

ma = -1000                                     # переменная для максимального значения
for i in range(len(numbers)):                  # цикл для нахождения максимального значения
    if numbers[i] > ma:
        ma = numbers[i]

n = 0
for j in range(len(numbers) - 1):              # цикл для расставления чисел по убыванию
    for i in range(len(numbers) - 1 - j):
        if numbers[i] < numbers[i+1]:
            n = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = n


print(f"Сумма: {cnt}")
print(f"Среднее арифметическое: {sr_arifm}")
print(f"Максимальное значение: {ma}")
print(f"Список по убыванию: {numbers}")
