products = {"ноутбук": 75000, "смартфон": 45000, "наушники": 8000, "клавиатура": 3500}

max_price = -100
max_product = ""
total_price = 0

for product, price in products.items():
    total_price += price

    if price > max_price:
        max_price = price
        max_product = product


print(f"Самый дорогой товар: {max_product} - {max_price} руб.")
print(f"Общая стоимость всех товаров: {total_price} руб.")