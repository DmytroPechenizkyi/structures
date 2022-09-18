# Создайте класс очереди для работы с символьными
# значениями. Требуется создать реализации для операций
# над элементами:
# ■ IsEmpty —роверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение.
# ■ Enqueue — добавление элемента в очередь.
# ■ Dequeue — удаление элемента из очереди.
# ■ Show — отображение всех элементов очереди на
# экран.
# При старте приложения нужно отобразить меню
# с помощью, которого пользователь может выбрать необходимую операцию
import inspect


class CharQueue:
    __size = 0
    __capacity = 0
    __data = list()

    def __init__(self, capacity: int):
            assert capacity > 0
            self.__capacity = capacity

    def get_size(self):
        return self.__size

    def is_empty(self):
        if self.__size == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.__size == self.__capacity:
            return True
        else:
            return False

    def enqueue(self, element: str):
        try:
            assert len(element) == 1
            if self.__size < self.__capacity:
                self.__data.append(element)
                self.__size += 1
                return f'''\'{element}\' добавлен в очередь.
Размер очереди: {self.__size}.
Свободно мест: {self.__capacity - self.__size}.'''
            else:
                print('Очередь переполнена.')
        except AssertionError:
            print('Должен вводиться один символ.')

    def dequeue(self):
        if self.__size > 0:
            dequeued = self.__data.pop(0)
            self.__size -= 1
            return f'''\'{dequeued}\' удален из очереди.
Размер очереди: {self.__size}.
Свободно мест: {self.__capacity - self.__size}.'''
        else:
            return None

# Этот метод во всех заданиях нужен для того, что-бы создать список существующих созданных мной методов для отображения
# их на консоли для пользователя. Также, некоторые методы - запретные, потому что либо будут не нужны
# пользователю, либо будут портить работу программы.
    def menu(self):
        list_of_methods = inspect.getmembers(CharQueue, predicate=inspect.isfunction)
        menu = []
        banned_list = ['execution', 'menu']
        for func_tuple in list_of_methods:
            if list_of_methods.index(func_tuple) == 0:
                continue
            else:
                for element in func_tuple:
                    if element in banned_list:
                        continue
                    elif func_tuple.index(element) == 0:
                        menu.append(element)
                    else:
                        continue
        return menu

# Выводит весь возможный функционал на консоль.
    def show(self):
        print('Возможный набор функций: ')
        for element in self.menu():
            print(element)
        print('Если хотите выйти из программы - введите \'quit\'.')

# Отвечает за работу с заданием в консоли. Сдесь много условностей и исключений, поэтому мне было сложно аккуратно
# описать логику работы данного метода.
    def execution(self):
        self.show()
        while True:
            input_operation = input('Укажите операцию: ')
            if input_operation in self.menu():
                if input_operation == 'enqueue':
                    parameter = input('Введите один символ, который хотите добавить: ')
                    operation = eval(f'self.{input_operation}(\'{parameter}\')')
                    print(operation)
                else:
                    operation = eval(f'self.{input_operation}()')
                    print(operation)
            elif input_operation == 'quit':
                exit()
            else:
                print('Неверная операция.')
