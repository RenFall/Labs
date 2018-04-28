# -*- coding: utf-8 -*- 
mas = ['Тетрадь', 'Ручка', 'Карандаш', 'Книга']

t = mas.pop(1)
b = mas.pop()
print(mas)
print([t, b])

#mas.insert(1, 'Pen')
#mas.append('Book')

mas.insert(0, 'Линейка')
mas.append('Блокнот')
print(mas)
input('Press Enter to continue...')  
