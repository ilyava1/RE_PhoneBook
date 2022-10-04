import time


def find_duples(smart_contacts_list):
    """
    Функция поиска дублей в телефонном справочнике.

    Дублирующими считаются такие записи контактов, у которых совпадает
    Имя, Фамилия и Отчество (либо Отчество в одом из контактов не указано).
    Если дубли найдены, функция возвращает их индексы. Если дубли не найдены,
    функция возвращает -1 в качестве индексов.

    :param smart_contacts_list: список - телефонный справочник
    :return: индексы элементов справочника являющихся дублями одного контакта
    """
    for i in range(len(smart_contacts_list) - 1):
        if (i + 1) <= len(smart_contacts_list) - 1:
            for j in range(i + 1, len(smart_contacts_list)):
                if ((smart_contacts_list[i][0] == smart_contacts_list[j][0])
                and (smart_contacts_list[i][1] == smart_contacts_list[j][1])
                and ((smart_contacts_list[i][2] == smart_contacts_list[j][2])
                    or (smart_contacts_list[i][2] == ''
                    or smart_contacts_list[j][2] == ''))):
                        return i,j
    i = j = -1

    return i,j


def merge_duples(smart_contacts_list,i,j):
    """
    Функция слияния двух дублирующих записей о контактах в одну.

    Из двух записей о контакте путем объединения информации функция создает
    третью запись. При этом за основу берется первая запись, а если какой-то
    атрибут первой записи пустой, то берется этот же атрибут из второй записи.
    Созданный объединенный контакт дописывается в конец телефонного справоч-
    ника, а преждние дублирующие записи удаляются.

    :param smart_contacts_list: список - телефонный справочник
    :param i: индекс первого дубля
    :param j: индекс второго дубля
    :return: список - телефонный справочник, с одним контактом
    вместо двух дублирующих
    """
    print()
    print('Найдены дубли:')
    print(f'1. {smart_contacts_list[i]}')
    print(f'2. {smart_contacts_list[j]}')
    time.sleep(2)
    merged_contact = []
    for y in range(len(smart_contacts_list[i])):
        if smart_contacts_list[i][y] != '':
            merged_contact.append(smart_contacts_list[i][y])
        else:
            merged_contact.append(smart_contacts_list[j][y])
    print('Сформирован объединенный контакт:')
    print(f'3. {merged_contact}')
    time.sleep(2)

    smart_contacts_list.append(merged_contact)
    smart_contacts_list.remove(smart_contacts_list[i])
    smart_contacts_list.remove(smart_contacts_list[j-1])

    return smart_contacts_list
