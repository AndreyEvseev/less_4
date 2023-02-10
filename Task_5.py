import os.path

from Func_file import choice_path_file as pf, writing_file_md_txt as wrf, read_file as rf
from Func_polinom import input_parameters_fill_random_coeff_polynom as ipp, transf_polinom_str_to_list as tsl 
#, fill_random_coeff_polynom_list as frp
from Func_polinom import  fill_terminal_coeff_polynom_list as ftp, coeff_polynom_list_normalization as cpn

def validation_action_number(num_act, course_action):
    if int(num_act) not in course_action:
        print(f'Введён некорректный номер варианта формирования полинома: {num_act}')
        return False
    else:
        return True

def choice_option_fill_list():
    print('Полином не задан. Выберите доступный номер варианта формирования полинома:\n'
          f'{messege_action}')
    num_correct = False
    num_act = ''
    while not num_correct:
        num_act = input(f'Введите выбранный номер варианта формирования полинома: ')
        num_correct = validation_action_number(num_act, course_action)
    if num_act == '1':
        incom_list = ipp()
    else:
        incom_list = cpn(ftp())
    return incom_list

def transform_polinom(user_polynom):
    result_polynom = user_polynom.replace('$', '').replace('**', '^').replace(' ', '')[:-2]
    return result_polynom

incom_file1, incom_file2 = 'Polinom_5_1.txt', 'Polinom_5_2.txt'
in_out_sign = 'in'
course_action = [1, 2]
messege_action = ('    1. Генерация случайных коэффициентов полинома заданной степени.\n'
                  '    2. Ввод коэффициентов полинома через терминал.')

print('\nЗадача сложения двух полиномов, записанных в текстовых файлах.\n')
if not os.path.isfile(pf(in_out_sign, incom_file1)):
    incom_list1 = choice_option_fill_list()
    wrf(in_out_sign, incom_list1, incom_file1)
if not os.path.isfile(pf(in_out_sign, incom_file2)):
    incom_list2 = choice_option_fill_list()
    wrf(in_out_sign, incom_list2, incom_file2)
print('Полиномы заданы корректно.'
        '\nРешаем задачу сложения двух полиномов, записанных в текстовых файлах.\n')
polinom1 = transform_polinom(rf(pf(in_out_sign, incom_file1)))
polinom2 = transform_polinom(rf(pf(in_out_sign, incom_file2)))
trans_polin1 = tsl(polinom1)
trans_polin2 = tsl(polinom2)
auxiliary_polinom = []
for i in range(len(trans_polin1)):
    auxiliary_polinom.append(trans_polin1[i])
for i in range(len(trans_polin2)):
    auxiliary_polinom.append(trans_polin2[i])
sum_polinom = cpn(auxiliary_polinom)

sum_file = 'Polinom_sum.md'
in_out_sign = 'out'
wrf(in_out_sign, sum_polinom, sum_file)
if in_out_sign == 'in':
    file_address = 'File_input/' + sum_file
elif in_out_sign == 'out':
    file_address = 'File_output/' + sum_file
print(f'Сформированный полином записан в файл: {file_address}\n')
