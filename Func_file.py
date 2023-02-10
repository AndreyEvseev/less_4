
# Функция определения служебного символа для допустимых типов файлов
def choice_simb(user_file):
    if user_file[-3:len(user_file)] == '.md':
        simb = '$'
    elif user_file[-4:len(user_file)] == '.txt':
        simb = ''
    else:
        print('Не определён тип файла. Распознаются типы: .md и txt')
    return simb

# Функция определения пути к файлу 
def choice_path_file(in_out_sign, user_file):
    if in_out_sign == 'in':
        path_file = 'File_input/' + user_file
    elif in_out_sign == 'out':
        path_file = 'File_output/' + user_file
    else:
        print(f"Некорректный признак входящего-исходящего файла: {in_out_sign}.\n"\
              "Допустимые значения: 'in'(входящий) или 'out'(исходящий)")
    return path_file

# Функция для записи полинома в файлы типов .md и .txt
def writing_file_md_txt(in_out_sign, user_list, user_file):
    simb = choice_simb(user_file)
    k = user_list[0][0]
    path_file = choice_path_file(in_out_sign, user_file)
    with open(path_file, 'w', encoding='utf-8') as pol:
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


# Функция присваивания строке содержимого текстового файла
def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as pol:
        result = pol.read()
        return result

