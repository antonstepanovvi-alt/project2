student_name = "Степанов Антон" #ФИО
group_number = 52501 #Номер группы
project_name = "ЖК Город звёзд" #Название объекта
floors = 25 #Этажность
height = 3.1 #Высота
is_residential = True #Тип
construction_year = 2026 #год постройки

total_height = floors * height

print(f"== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ==\n"
      f"Составитель: {student_name}\n"
      f"Группа: {group_number}\n"
      f"Объект: {project_name}\n"
      f"Этажность: {floors} этажей\n"
      f"Высота: {total_height} м\n"
      f"Тип: {'Жилой' if is_residential else 'Нежилой'}\n"
      f"Год постройки: {construction_year}")

# Реальный жк в новосаратовке, я там кваритру купил
# ( правда про высоту потолков наврал, там 2.6 натяжной,2.8 плита, сама плита хз но наверно 300.
# По этому и 3.1