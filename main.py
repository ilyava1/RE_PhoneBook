import re_service
import base_service
import json
import time
import csv


if __name__ == '__main__':
    with open('config.json', 'r', encoding='utf-8-sig') as f:
        config = json.load(f)
    # читаем адресную книгу в формате CSV в список contacts_list
    with open(config['broken_phone_book_file'], 'r',
              encoding = 'utf-8-sig') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
        my_count = 0
        for record in contacts_list:
             if my_count == 0:
                 # Вывод строки, содержащей заголовки для столбцов
                 print()
                 print('Исходный файл содержит столбцы:')
                 for column in record:
                     print(f'   {column}, ', end='')
                 my_count += 1
                 print()
                 print('Содержание записей о контактах:')
             else:
                 # Вывод строк
                 print(f'{my_count}. {record}')
                 my_count += 1
        print()
        input('Нажмите Enter чтобы продолжить ')

    smart_contacts_list = [] # Объявляем будущий итоговый список
    fieldnames = contacts_list.pop(0) # Извлекаем имена полей

    # Запускаем цикл по списку контактов
    for i in range(0, my_count-1):
        # Находим и вычленяем фамилию, имя и отчество
        lfs_string = (contacts_list[i][0] + ' ' + contacts_list[i][1] + ' '
                      + contacts_list[i][2]+ ' ')

        # Определяем шаблон поиска и передаем данные в функцию поиска фамилии
        pattern = r'[а-яёА-ЯЁ]*\s'
        lastname,  lfs_string = re_service.search_for_string(pattern,
                                                             lfs_string)
        smart_contacts_list.append([lastname])

        # Аналогично с именем, паттерн тот же
        firstname, lfs_string = re_service.search_for_string(pattern,
                                                             lfs_string)
        smart_contacts_list[i].append(firstname)

        # Аналогично с отчеством, паттерн тот же
        surname, lfs_string = re_service.search_for_string(pattern,
                                                           lfs_string)
        smart_contacts_list[i].append(surname)

        # Добавляем в результатный список организацию:
        smart_contacts_list[i].append(contacts_list[i][3])

        # Добавляем в результатный список должность:
        smart_contacts_list[i].append(contacts_list[i][4])

        # Добавляем в результатный список телефон:
        phone_string = contacts_list[i][5]
        smart_phone = re_service.phone_transform(phone_string)
        smart_contacts_list[i].append(smart_phone)

        # Добавляем в результатный список емейл:
        smart_contacts_list[i].append(contacts_list[i][6])

    # Ищем и сливаем дубли контактов
    count = 0
    # Пока не закончаться дубли повторяем цикл
    while True:
        # Получаем индексы дублей в списке контактов через спец. функцию
        i,j = base_service.find_duples(smart_contacts_list)
        # Если получены отрицательные индексы, значит дубли
        # закончились и пора покидать цикл
        if i == j == -1:
            break
        else:
            # Если индексы не отрицательные, значит вызываем функцию
            # для слияния дублей
            smart_contacts_list = base_service.merge_duples(
                smart_contacts_list, i, j)
            # Считаем кол-во слитых дублей для статистики
            count += 1

    print()
    if count > 0:
        print(f'Т.о. объединены {count} пары дублирующих контактов')
        print()
        time.sleep(2)
    print('Результирующий список: ')
    count = 1
    for contact in smart_contacts_list:
        print(f'{count}. {contact}')
        time.sleep(1)
        count += 1
    print()

    # записываем в адресную книгу обработанный список контактов
    with open(config['smart_phone_book_file'], 'w',
              encoding = 'utf-8-sig') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(fieldnames)
        for contact in smart_contacts_list:
            datawriter.writerow(contact)

    print("Результирующий список контактов записан в файл 'phonebook.csv'")
    print()
