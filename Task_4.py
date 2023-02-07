from Func_polinom import fill_random_coeff_polynom_list as cp
from Func_polinom import zeroing_random_coeff_polynom_list as zer
from Func_file import writing_file_md_txt as wrf

k = int(input('Задайте натуральную степень многочлена k: '))
coeff_polynom = cp(k)
mess_zeroing = 'При желании обнулить несколько коэффициентов сгенерированного многочлена (рандомно), введите 1, ' \
                'в противном случае введите любой другой символ: '
if input(mess_zeroing) == '1':
    coeff_polynom = zer(coeff_polynom)
my_file = 'Polinom4.md'
wrf(coeff_polynom, my_file)
