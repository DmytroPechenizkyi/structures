# Задание 2
# Создайте класс очереди с приоритетами для работы
# с символьными значениями.
# Требуется создать реализации для операций над элементами очереди:
# ■ IsEmpty — проверка очереди на пустоту.
# ■ IsFull — проверка очереди на заполнение.
# ■ InsertWithPriority — добавление элемента c приоритетом в очередь.
# ■ PullHighestPriorityElement — удаление элемента с самым высоким приоритетом из очереди.
# ■ Peek — возврат самого большого по приоритету элемента. Обращаем ваше внимание, что элемент не
# удаляется из очереди.
# ■ Show — отображение всех элементов очереди на экран.
# При показе элемента также необходимо отображать
# приоритет.
# При старте приложения нужно отобразить меню
# с помощью, которого пользователь может выбрать необходимую операцию
import inspect


class PriorityCharQueue:
    __data = list()
    __size = 0
    __priority = list()
    __capacity = 0

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

    def insert_with_priority(self, element: str, priority: int):
        try:
            assert len(element) == 1
            if self.__size < self.__capacity:
                self.__data.append(element)
                self.__priority.append(priority)
                self.__size += 1
                return f'''\'{element}\' добавлен в очередь.
Приоритет в очереди: {priority}.
Размер очереди: {self.__size}.
Свободно мест: {self.__capacity - self.__size}.'''
            else:
                print('Очередь переполнена.')
        except AssertionError:
            print('Должен вводиться один символ.')
        except ValueError:
            print('В качестве приоритета должно вводиться число.')

    def pull_highest_priority_element(self):
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            pulled_out = self.__data.pop(index_max_priority)
            self.__priority.pop(index_max_priority)
            self.__size -= 1
            return f'''\'{pulled_out}\' удален из очереди.
Приоритет в очереди: {max_priority}.
Размер очереди: {self.__size}.
Свободно мест: {self.__capacity - self.__size}.'''
        else:
            return None

    def peek(self):
        if self.__size > 0:
            max_priority = max(self.__priority)
            index_max_priority = self.__priority.index(max_priority)
            for element in self.__data:
                element_index = self.__data.index(element)
                if element_index == index_max_priority:
                    return element
        else:
            return None

# Этот метод во всех заданиях нужен для того, что-бы создать список существующих созданных мной методов для отображения
# их на консоли для пользователя. Также, некоторые методы - запретные, потому что либо будут не нужны
# пользователю, либо будут портить работу программы.
    def menu(self):
        list_of_methods = inspect.getmembers(PriorityCharQueue, predicate=inspect.isfunction)
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
                if input_operation == 'insert_with_priority':
                    character = input('Введите один символ, который хотите добавить: ')
                    priority = int(input('Введите приоритет символа в очереди: '))
                    operation = eval(f'self.{input_operation}(\'{character}\', {priority})')
                    print(operation)
                else:
                    operation = eval(f'self.{input_operation}()')
                    print(operation)
            elif input_operation == 'quit':
                exit()
            else:
                print('Неверная операция.')