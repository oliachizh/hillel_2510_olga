# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = []
for quote in alice_in_wonderland:
    if quote == "'":
        single_quotes += "'"
print(f"Кількість одинарних лапок:, {len(single_quotes)}\n")


# task 03 == Виведіть змінну alice_in_wonderland на друк
print(f"Текст із alice_in_wonderland:\n\n{alice_in_wonderland}\n")

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total = black_sea_area + azov_sea_area
print(f"Разом площа складає {total} км2\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
store_nums = 3
total_items = 375291
total_items_store_1_and_2 = 250449
total_items_store_3 = total_items - total_items_store_1_and_2
total_items_store_2 = 222950 - total_items_store_3
total_items_store_1 = total_items_store_1_and_2 - total_items_store_2

print(f"На складі 1 - {total_items_store_1} товарів,\n"
      f"На складі 2 - {total_items_store_2} товарів,\n"
      f"На складі 3 - {total_items_store_3} товарів.\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_pay = 1179
total_months = 18
total_price = month_pay * total_months
print(f"Вартість комп’ютера - {total_price} грн\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019%8
print(f"остача від діленя чисел: a) 8019 : 8 - {a}")
b = 9907%9
print(f"остача від діленя чисел: b) 9907 : 9 - {b}")
c = 2789%5
print(f"остача від діленя чисел: c) 2789 : 5  - {c}")
d = 7248%6
print(f"остача від діленя чисел: d) 7248 : 6  - {d}")
e = 7128%5
print(f"остача від діленя чисел: e) 7128 : 5  - {e}")
f = 19224%9
print(f"остача від діленя чисел: f) 19224 : 9  - {f}")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_price = 274
big_pizza_nums = 4
medium_pizza_price = 218
medium_pizza_nums = 2
juice_price = 35
juice_nums = 4
cake_price = 350
cake_nums = 1
water_price = 21
water_nums = 3
total_money = (cake_price*cake_nums)+(juice_price*juice_nums)+(big_pizza_price*big_pizza_nums)+(medium_pizza_price*medium_pizza_nums)
print(f"\nгрошей знадобиться - {total_money} грн\n")
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_nums = 232
photo_per_page = 8
page_numbers = photo_nums / photo_per_page
print(f"{int(page_numbers)} сторінок знадобиться Ігорю, щоб вклеїти всі фото\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_consumption_per_100km = 9
fuel_tank_volume = 48

total_fuel_needed = (distance / 100) * fuel_consumption_per_100km
print(f"Загальна кількість бензину, необхідного для подорожі: {total_fuel_needed} літрів\n")
charging_count = total_fuel_needed / fuel_tank_volume
print(f"Кількість зупинок на заправку: {int(charging_count)}")
