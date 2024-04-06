import os

FILE_PATH = r"c:\Users\ProNout\Desktop\Учеба_2022 (Разработчик_IT)\2024\03\Знакомство с языком программирования Python\Pyton_Home_Job\Python_Seminar8\PhoneBook\bd.txt"

def read_bd():
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
    return list(enumerate(lines))

def print_records(records):
    numerated_records=list(enumerate(records))
    for record in numerated_records:
        print(f'{record[0]+1}. {record[1][1].replace(";", ": ").strip()}')

def print_record(record):
    print(f'{record[1].replace(";", ": ").strip()}')

def print_bd():
    bd=read_bd()
    os.system('cls')
    print_records(bd)

def find_records():
    os.system('cls')
    str=input('Информация для поиска: ')
    bd=read_bd()
    result = []
    for record in bd:
        if str.lower() in record[1].lower():
            result.append(record)
    return result

def find_n_print():
    records=find_records()
    os.system('cls')
    print_records(records)

def add_record():
    os.system('cls')
    name=input('Введите имя: ')
    phone=input('Введите телефон: ')
    with open(FILE_PATH, 'a') as f:
        f.write(f'\n{name};{phone}')

def save_bd(bd):
    with open(FILE_PATH, 'w') as f:
        for record in bd:
            f.write(record[1])

def del_record():
    bd=read_bd()
    os.system('cls')
    print_records(bd)
    num=int(input('Введите номер записи для удаления: '))
    bd.pop(num-1)
    bd[-1]=bd[-1][0],bd[-1][1].strip()
    save_bd(bd)

def edit_record():
    bd=read_bd()
    os.system('cls')
    print_records(bd)
    num=int(input('Введите номер записи для редактирования: '))
    os.system('cls')
    print(f'Запись для редактирования:')
    print_record(bd[num-1])
    name,phone=bd[num-1][1].split(';')
    option=int(input('\n1. Удалить\n2. Имя\n3. Телефон\nУкажите какое поле редактируем: '))
    if option==2:
        name=input('Введите новое имя: ')
    if option==3:        
        phone=input('Введите новый телефон: ')
    bd[num-1] = bd[num-1][0],f'{name};{phone}\n' if num<len(bd) else  f'{name};{phone}'
    if option==1:
        bd.pop(num-1)
        bd[-1]=bd[-1][0],bd[-1][1].strip()
    save_bd(bd)

def import_data():
    inputfile = "import.txt"
    importfile = open(inputfile, mode='r', encoding='ANSI')
 #   name=input('Введите имя: ')
#    phone=input('Введите телефон: ')
    with open(FILE_PATH, 'a') as f:
        f.write(f'\n{importfile.read()}')

def menu():
    while True:
        os.system('cls')
        print('Телефонный справочник. \nВыберите действие:')
        print('\n1. Показать все контакты')
        print('2. Показать контакт')
        print('3. Создать контакт')
        print('4. Удалить контакт')
        print('5. Обновить контакт')
        print('6. Импорт')
        print('0. Выйти из справочника')
        input_num = int(input('Введите номер пункта меню: '))
        if input_num == 1:
            print_bd()
        elif input_num == 2:
            find_n_print()
        elif input_num == 3:
            add_record()
        elif input_num == 4:
            del_record()
        elif input_num == 5:
            edit_record()
        elif input_num == 6:
            import_data()
        elif input_num == 0:
            break    
        input('Нажмите Enter для продолжения...')
menu()