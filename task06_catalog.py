materials = ["Стекло","Железобетон","Газобетон","Керамзитобетон","Стекловата"]
print ("Список:", materials)
print ("Первый элемент:", materials[0])
print ("Последний элемент:", materials[-1]) #последний элемент
print ("Средние элементы", materials[1:4])

materials.extend(["Кирпич","Дерево"]) #Добавляем 2 элемента

print ("Обновленный список:", materials)

del materials[1] #Удаляем элемент номер 2

print ("Итоговый список (без 2 эл):", materials)
print ("Длинна списка:", len(materials))
