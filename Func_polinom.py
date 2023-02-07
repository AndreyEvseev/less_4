import random

# Функция рандомного формирования коэффициентов многочлена заданной степени
def fill_random_coeff_polynom_list(k, min_border = 0, max_border = 100):
    k_val = 0
    while k_val == 0:
        k_val = random.randint(min_border, max_border)
    kort = (k, k_val)
    new_list = [kort]
    for i in range (1, k+1):
        kort = (k - i, random.randint(min_border, max_border))
        new_list.append(kort) 
    return new_list

# Функция "прореживания" ненулевых коэффициентов многочлена (рандомное обнуление).
# Только для списков кортежей "(степень, коэффициент)", отсортированных по убыванию степени и 
# содержащих коэффициенты (в т.ч. равные нулю) для всех степеней, включая 0-ую. 
def zeroing_random_coeff_polynom_list(user_list):
    max_zero = len(user_list) - 2
    num_zero = 0
    for i in range(1, len(user_list)):
        if user_list[i][1] == 0:
            num_zero += 1
    kor = user_list[0]
    result_list = []
    result_list.append(user_list[0])
    for i in range(1, len(user_list)):
        if num_zero == max_zero:
            result_list.append(user_list[i])
        else:
            if user_list[i][1] != 0:
                if random.randint(0, 1) == 0:
                    kor = (len(user_list) - 1 - i, 0)
                    result_list.append(kor)
                    num_zero += 1
                else:
                    result_list.append(user_list[i])
    return result_list

