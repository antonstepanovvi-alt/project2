materials = {
    "Стекло": 600,
    "Железобетон": 1500,
    "Газобетон": 1000,
    "Керамзитобетон": 1200,
    "Стекловата": 700
}
print ("Список:", materials)

#Обновляем список:
materials["Кирпич"] = 1100
materials["Дерево"] = 900
print ("Обновленный список:", materials)

#Скидка
materials["Кирпич"] *= 1.10

#Удаляем
del materials["Стекло"]

print("Итог:", materials)
print("Средняя цена:", sum(materials.values()) / len(materials))