list1 = ["Анна", "Борис", "Виктор", "Галина", "Дмитрий", "Анна"]
list2 = ["Борис", "Елена", "Виктор", "Жанна", "Игорь"]

set1 = set(list1)
set2 = set(list2)

unification = set1 & set2

only_first = set1 - set2

print(f"Общие имена: {unification}")
print(f"Только в первом списке: {only_first}")
