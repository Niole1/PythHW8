# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска 
# определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и
# удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных


# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла


def show_data():
    "Выводит информацию из справочника"
    with open('data.txt', 'r', encoding='utf-8') as f:
        book = f.read()#.split('\n')
    return book

def add_data():
    "Добавляет информацию в справочник"
    fio = input("Введите ФИО: ")
    tel_number = input("Введите номер телефона: ")

    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(f" \n{fio} | {tel_number}")
        print("Успешно")
    

def find_data():
    "Осуществляет поиск по справочнику"
    with open('data.txt', 'r', encoding='utf-8') as f:
        book = f.read().split('\n')
        temp = input('Что необходимо найти?: ')
        for i in book:
            if temp in i:
                print(i)


def delete_person(name):
    "Удаляет данные"
    persons = add_data()
    with open("data.txt", "w", encoding="utf8" ) as f:
        for person in persons:
            if name != person:
                f.write(person)

def change_person(new_name, old_name):
    "Изменяет данные"
    persons = add_data()
    with open("data.txt", "w", encoding="utf8" ) as f:
        for person in persons:
            if  old_name != person:
                f.write(person)
            else:
                f.write(new_name + "\n")



while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        add_data()
    elif mode == '3':
        name = input('Кого удаляем?: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('Кого хотим переименовать?: ')
        new_name = input('Как хотим его назвать?: ')
        change_person(new_name,old_name)
    elif mode == '5':
        break
    else:
        print('No mode')
