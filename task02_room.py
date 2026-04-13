length = 6 #Длинна
width = 4 #Ширина
height = 3.2 #Высота
S_floor = length * width #Площадь пола
S_wall = length * height * 2 + width * height * 2 #Площадь стен
V = length * width * height #Объем
Cost = S_wall * 125 #Стоимость
print(f"== ПАРАМЕТРЫ ПОМЕЩЕНИЯ ==\n"
      f"Длинна: {length}\n"
      f"Ширина: {width}\n"
      f"Высота: {height}\n"
      f"Площадь пола: {S_floor:.2f}\n"
      f"Площадь стен: {S_wall:.2f}\n"
      f"Объем: {V:.2f}\n"
      f"Стоимость: {Cost:.2f}\n")