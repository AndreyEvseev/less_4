import random

def fill_number_list(n, border1, border2): 
    if border1 < border2:
        min_bord, max_bord = border1, border2
    else:
        min_bord, max_bord = border2, border1
    new_list = [random.randint(min_bord, max_bord)]
    for i in range(1, n):
        new_list.append(random.randint(min_bord, max_bord))
        i += 1
    return new_list

def unique_values_list(user_list):
    new_list = [user_list[0]]
    for i in range(1, len(user_list)):
        for j in range(len(new_list)):
            if user_list[i] == new_list[j]:
                break
            elif j == len(new_list)-1:
                new_list.append(user_list[i])
    return new_list

n = int(input('Количество элементов списка: '))
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
source_list = fill_number_list(n, b1, b2)
unique_list = unique_values_list(source_list)
unique_list.sort()
print(f'Исходный список: {source_list} ->')
print(f'Список неповторяющихся элементов: {unique_list}')
