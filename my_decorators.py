import datetime
import os


def my_decor_decorator(log_path):

    def my_decorator(some_function):
        """
        Функция-декорflake8 main.pyfатор
        Он записывает в файл дату и время вызова функции, имя функции,
        аргументы, с которыми вызвалась и возвращаемое значение.
        :param some_function: декорируемая функция
        :return:
        """

        def arrange_function(*args):

            # with open('config.json', 'r') as cf:
            #     config = json.load(cf)

            if not os.path.isdir(log_path):
                os.mkdir(log_path)

            with open(log_path + 'PhoneBook_decorator_log.txt', 'a',
                      encoding='cp1251') as f:
                f.write(str(datetime.datetime.now().strftime('%y-%b-%d '
                                                             '%H:%M:%S'))
                        + ' | ')
                f.write('Function: ' + some_function.__name__ + ' |')
                doc_str = some_function.__doc__.split('\n')[1]
                f.write('Description: ' + doc_str + ' | ')
                if len(args) > 0:
                    f.write('Arguments: ')
                    for argument in args:
                        f.write(str(argument) + '; ')
                    f.write('| ')
                result = some_function(*args)
                if type(result) == tuple:
                    f.write('Result: ')
                    for element in result:
                        f.write(str(element) + '; ')
                    f.write('\n')
                else:
                    f.write('Result: ' + result + '\n')
            return result

        return arrange_function

    return my_decorator
