from Func_polinom import fill_random_coeff_polynom_list as cp

# Функция для записи полинома в файлы типов .md и .txt
def writing_file_md_txt(user_list, user_file):
    if user_file[-3:len(user_file)] == '.md':
        simb = '$'
    elif user_file[-4:len(user_file)] == '.txt':
        simb = ''
    else:
        print('Не определён тип файла. Распознаются типы: .md и txt')
    k = user_list[0][0]
    user_file = 'File_output/' + user_file
    with open(user_file, 'w', encoding='utf-8') as pol:
        if user_list[0][1] == 1:
            pol.write(f'{simb}x^{k}')
        else:
            pol.write(f'{simb}{user_list[0][1]}x^{k}')
        for i in range(1,k+1):
            if user_list[i][1] != 0:
                if user_list[i][1] > 0:
                    pol.write('+')
                if user_list[i][1] != 1:
                    pol.write(f'{user_list[i][1]}')
                if i != k and i != k - 1:
                    pol.write(f'x^{k - i}')
                elif i == k-1:
                    pol.write('x')
        pol.write(f'=0{simb}')



# k = 9
# user_list = coeff_polynom = cp(k)
# print(user_list)
# user_file = 'Polinom_4.txt'
# writing_file_md_txt(user_list, user_file)


