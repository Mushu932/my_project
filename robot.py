robot_name = "R2-D2"
robot_version = 1.0

print("Привет! Меня зовут", robot_name)
print("Версия:", robot_version)

battery_level = 87
wheels = 4

print("Заряд батареи:", battery_level, "%")
print("Количество колёс:", wheels)

if battery_level >50:
    print("Робот полон сил и готов к работе!")
else:
    print("Роботу нужно зарядиться.")

user_name = input("Как вас зовут? ")

print(f"{user_name}, добро пожаловать в мир робототехники!")
print("Я готов помочь вам учиться!")