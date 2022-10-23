import re
from my_decorators import my_decor_decorator

my_log_path = "C:/TEMP_Decorator_logs/"


@my_decor_decorator(my_log_path)
def search_for_string(pattern, base_string):
    """
    Функция поиска строки по шаблону (регулярному выражению).

    Функция находит первое вхождение искомой строки, удаляет найденную строку
    из исходной строки и возвращает обе строки - найденную и модифицированную
    исходную

    :param pattern: шаблон - рег. выражение
    :param base_string: строка в которой производится поиск
    :return: найденная строка и модифицированная исходная
    """
    searh_result = re.match(pattern, base_string, flags=0)
    if searh_result != None:
        searh_result_string = searh_result.group()
        base_string = re.sub(searh_result_string, '', base_string, count=1,
                             flags=0)
        result_string = searh_result.group()[:-1]
    else:
        result_string = ''
    print(end='')
    return result_string, base_string

@my_decor_decorator(my_log_path)
def phone_transform(phone_string):
    """
    Функция трансформации телефонного номера в формат +7(999)999-99-99.

    :param phone_string: исходная строка для форматирования
    :return: результатная строка в требуемом формате
    """
    # Получаем телефонный номер
    pattern_phone = r'(\+7|8)\s*\((\d+)\)\s*(\d+)(\s|-)(\d\d)(\s|-)(\d\d)'
    phone = re.match(pattern_phone, phone_string)
    # Получаем добавочный телефонный номер
    pattern_internal_phone = '(доб\.\s\d*)'
    int_phone = re.search(pattern_internal_phone, phone_string)
    if phone != None:
        # Выполняем преобразование тел номера к шаблону: +7(999)999-99-99
        substitution = r'+7(\2)\3-\5-\7'
        new_phone = re.sub(pattern_phone, substitution, phone.group())
        if int_phone != None:
            smart_phone = new_phone + ', ' + int_phone.group()
        else:
            smart_phone = new_phone
    else:
        smart_phone = ''

    return smart_phone
