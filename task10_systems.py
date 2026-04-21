#Это работа, где вместе используются словари, цикл, условия, изменение данных.
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}
#Это словарь (в Python dict). Представим его как папку с карточками:
#Название карточки = материал ("Кирпич", "Цемент" и т.д.)
#Внутри карточки = три числа: сколько лежит, сколько стоит одна штука, и минимальный безопасный остаток (если упадёт ниже → пора закупать).
print("=" * 80)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 80)

print("\nМатериал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 80)

total_cost = 0
most_expensive = None
max_price = 0
critical_items = []
#«Обход всех карточек» (цикл for)
#строка ниже говорит: «Возьми каждую карточку из папки warehouse по очереди. Название карточки назови material, а её содержимое — data».
for material, data in warehouse.items():
    quantity = data["quantity"]  # Вытаскиваем кол-во материала из словоря
    price = data["price"]  # Вытаскиваем Цену
    min_qty = data["min_quantity"]  # Вытаскиваем мин кол-во
    cost = quantity * price  # Общая стоимость

    total_cost += cost  # добавляем стоимость материала к общей сумме

    # Является ли материал самым дорогим
    if price > max_price:
        max_price = price
        most_expensive = material

    is_critical = quantity < min_qty  # Критический ли остаток

    # Добавляет мат в список критич остаков
    if is_critical:
        critical_items.append({
            "material": material,
            "quantity": quantity,
            "min": min_qty
        })

    # Формируем строку для вывода
    line = f"{material} | {quantity} | {price:.2f} | {min_qty} | {cost:.2f}"  # f"..." — это шаблон для вывода. 2f-это две после запятой
#Если материал в зоне риска, к строке добавляется слово КРИТИЧ!. Потом строка сразу печатается на экране.

    # Предупреждение
    if is_critical:
        line += " КРИТИЧ!"

    print(line)

print("\n" + "=" * 80)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_cost:.2f} руб")
print(f"Самый дорогой: {most_expensive} ({max_price:.2f} руб)")

# Проверяем есть ли критические остатки
if critical_items:
    print(f"\n КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
    for item in critical_items:
        print(f"  - {item['material']}: {item['quantity']} < {item['min']}")

print("\n=== ВЫДАЧА МАТЕРИАЛА ===")

material_to_issue = "Цемент"
quantity_to_issue = 25

# Есть ли такой материал на складе
if material_to_issue in warehouse:
    current_qty = warehouse[material_to_issue]["quantity"]

    # Достаточно ли материала на складе
    if current_qty >= quantity_to_issue:

        warehouse[material_to_issue]["quantity"] -= quantity_to_issue  # Уменьшает кол-во мат на складе
        new_qty = warehouse[material_to_issue]["quantity"]  # Новое кол-во

        print(f" Выдано {quantity_to_issue} единиц '{material_to_issue}'")
        print(f" Остаток: {current_qty} → {new_qty}")
    else:
        print(f" Недостаточно '{material_to_issue}' на складе!")
        print(f" Требуется: {quantity_to_issue}, есть: {current_qty}")
else:
    print(f" Материал '{material_to_issue}' не найден!")

#здесь используется вложенный словарь
#цикл проходит по всем материалам
#стоимость позиции считается как количество * цена
#если остаток меньше минимального, позиция считается критической
#при выдаче количество уменьшается
#словарь {}
#Хранит данные в парах ключ: значение
#Папка с именованными карточками
#for ... in ...
#Проходит по всем элементам коллекции
#Конвейер, где берут по одной коробке и обрабатывают
#if / else
#Выполняет код только если условие истинно
#Светофор: если зелёный → едь, иначе → стой
#+= и -=
#Быстро прибавляют или вычитают значение
#f"{...}"
#Подставляет переменные прямо в текст
