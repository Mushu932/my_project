number = int(input("Введите число: "))

if number < 2:
    print("Число не является простым")
else:
    for d in range(2, number):
        if number % d == 0:
            print(f"Число {number} не простое, делится на {d}")
            break
    else:
        print(f"Число {number} простое")
        