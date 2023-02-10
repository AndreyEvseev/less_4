from Func_polinom import fill_random_coeff_polynom_list as cp
from Func_file import writing_file_md_txt as wrf

k = int(input('Задайте натуральную степень полинома k: '))
coeff_polynom = cp(k)
print(f'Сгенерирован список коэффициентов полинома степени {k}:\n'\
      f'{coeff_polynom}')
my_file = 'Polinom4.md'
in_out_sign = 'out'
wrf(in_out_sign, coeff_polynom, my_file)
if in_out_sign == 'in':
    file_address = 'File_input/' + my_file
elif in_out_sign == 'out':
    file_address = 'File_output/' + my_file
print(f'Сформированный полином записан в файл: {file_address}\n')