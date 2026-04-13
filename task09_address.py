import re  # Нужен для работы с выражениями

addresses = [
    "  г. Улан-Удэ, ул. Ленина, д.     15  ",
    "г.Уфа,ул.Академика константинова,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 190  "
]

print("=== СРАВНЕНИЕ ===")

for i, address in enumerate(addresses, 1):
    original = address

    address = address.strip()  # Удаляем пробелы

    address = re.sub(r'(г\.|ул\.|д\.)(?!\s)', r'\1 ', address)  # Добавляем пробел после этих сокращений

    address = re.sub(r',\s*', ', ', address)  # Пробелы после запятых

    address = re.sub(r'\s+', ' ', address)  # Заменяем множесвенные пробелы

    address = address.strip()  # Убирает пробелы по краям

    print(f"#{i}")
    print(f"ДО: '{original}'")
    print(f"ПОСЛЕ: '{address}'")
    print()
