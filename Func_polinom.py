import random

# Функция ввода степени полинома, минимальной и максимальной границ коэффициентов
def input_parameters_fill_random_coeff_polynom():
    k = int(input('Введите степень полинома (целочисленное): '))
    min_border = int(input('Введите минимальную границу коэффициентов полинома (целочисленное, по умолчанию = 0): '))
    max_border = int(input('Введите минимальную границу коэффициентов полинома (целочисленное, по умолчанию = 100): '))
    if max_border < min_border:
        auxiliary_border = max_border
        max_border = min_border
        min_border = auxiliary_border
    coeff_polynom_list = fill_random_coeff_polynom_list(k, min_border, max_border)
    return coeff_polynom_list

# Функция рандомного формирования коэффициентов полинома заданной степени.
# Слагаемые с коэффициентами "0" в список не включаются.
# Результат - список кортежей вида: "(степень, коэффициент)", упорядоченный по убыванию степени.
def fill_random_coeff_polynom_list(k, min_border = 0, max_border = 100):
    k_val = 0
    while k_val == 0:
        k_val = random.randint(min_border, max_border)
    kort = (k, k_val)
    new_list = [kort]
    for i in range (1, k + 1):
        kort = (k - i, random.randint(min_border, max_border))
        if kort[1] != 0:
            new_list.append(kort) 
    return new_list

# Функция ввода коэффициентов полинома с терминала.
# Результат - не упорядоченный список кортежей вида: "(степень, коэффициент)".
def fill_terminal_coeff_polynom_list():
    new_list = []
    next_oper = 1
    while next_oper == 1:
        k = int(input('Введите степень элемента полинома k (целочисленное): '))
        k_val = int(input('Введите коэффициент для элемента полинома степени k (целочисленное): '))
        kor = (k, k_val)
        new_list.append(kor)
        print(new_list)
        if input('\nДля продолжения ввода полинома введите "1", \nдля завершения - любой другой символ: ') != '1':
            next_oper = 0
    return new_list

# Функция нормализации списка элементов полинома. Применяется для списков кортежей вида: "(степень, коэффициент)". 
# Производится сложение коэффициентов одинаковой степени и упорядочение кортежей по убыванию степени. 
# Слагаемые с коэффициентами "0" в список не включаются.
def coeff_polynom_list_normalization(user_list):
    k_pol = user_list[0][0]
    for i in range(1, len(user_list)):
        if user_list[i][0] > k_pol:
            k_pol = user_list[i][0]
    norm_list = []
    for i in range(k_pol, -1, -1):
        k_val = 0
        for j in range(len(user_list)):
            if user_list[j][0] == i:
                k_val += user_list[j][1]
        if k_val != 0:
            kor = (i, k_val)
            norm_list.append(kor)
    return norm_list

# Функция определения коэффициента элемента полинома
def num_list(p, a):
    if p.index(a) == 0:
        n = 1
    elif p.index(a) ==1:
        if p[0] == '-':
            n = -1
        elif p[0] == '+':
            n = 1
        else:
            n = p[0]
    else:
        n = int(p[:p.index(a)])
    return n

# Функция определения степени элемента полинома
def degree_list(p):
    if p.find('-') != -1 and p.find('+') != -1:
        ind = min(p.index('-'), p.index('+')) 
    elif p.find('-') != -1 and p.find('+') == -1:
        ind = p.index('-')
    elif p.find('-') == -1 and p.find('+') != -1:
        ind = p.index('+')
    else:
        ind = len(p)
    return ind

# Функция трансформации строки с нормализованным полиномом в список кортежей вида: "(степень, коэффициент)".
def transf_polinom_str_to_list(p):
    k_val = 0
    k = 0
    coeff_polynom = []
    kor = ()
    while len(p) > 0:
        if p.find('x^') != -1:
            k_val = num_list(p, 'x^')
            p = p[:0] + p[p.index('x^'):]
            ind = degree_list(p)
            k = int(p[2:ind])
            p = p[:0] + p[ind:]
            kor = (k, k_val)
            coeff_polynom.append(kor)
        elif p.find('x') != -1:
            k_val = num_list(p, 'x')
            p = p[:0] + p[p.index('x'):]
            ind = degree_list(p)
            k = 1
            p = p[:0] + p[1:]
            kor = (k, k_val)
            coeff_polynom.append(kor)
        else:
            k_val = int(p[:len(p)])
            k = 0
            p = p[:0] + p[len(p):]
            kor = (k, k_val)
            coeff_polynom.append(kor)    
    return coeff_polynom



