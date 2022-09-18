# Необходимо разработать приложение, которое позволит сохранять информацию о логинах пользователей и их
# паролях. Каждому пользователю соответствует пара логин — пароль. При старте приложение отображается меню:
# ■ Добавить нового пользователя
# ■ Удалить существующего пользователя
# ■ Проверить существует ли пользователь
# ■ Изменить логин существующего пользователя
# ■ Изменить пароль существующего пользователя
# Для реализации задания обязательно используйте
# одну из структур данных. При выборе руководствуйтесь
# постановкой задачи.
import inspect


class Users:
    __login = str
    __password = str
    __list_of_users = list()

# В конструкторе нам ничего не нужно. Все операции и довавления пользователей делаем через методы. Тоесть, у меня
# программа не хранит кучу объектов, а сам объект является таким хранилищем. Не знаю насколько это правильно, но я
# сделал подобным образом.
    def __init__(self):
        pass

    def show_list(self):
        return self.__list_of_users

    def add_user(self, login: str, password: str):
        try:
            assert login.isalnum()
            assert len(password) >= 8
            self.__login = login
            self.__password = password
            user_info = {'login': self.__login, 'password': self.__password}
            self.__list_of_users.append(user_info)
            return f'''Пользователь добавлен.
Логин: {user_info['login']}.
Пароль: {user_info['password']}.'''
        except AssertionError:
            print('Логин должен состоять только из букв и цифр, а пароль должен иметь не менее 8 символов.')

    def remove_user(self, login: str):
        for user_info in self.__list_of_users:
            if user_info['login'] == login:
                self.__list_of_users.remove(user_info)
                return f'''Пользователь удален.
Логин: {user_info['login']}.
Пароль: {user_info['password']}.'''
            else:
                print('Неверный логин')

    def does_exist(self, login: str):
        for user_info in self.__list_of_users:
            if user_info['login'] == login:
                return True
        return False

    def change_login(self, login: str, new_login: str):
        for user_info in self.__list_of_users:
            if user_info['login'] == login:
                user_info['login'] = new_login
                return f'{login} изменен на {new_login}.'
        return 'Неверный логин.'

    def change_password(self, login: str, new_password: str):
        for user_info in self.__list_of_users:
            if user_info['login'] == login:
                old_password = user_info['password']
                user_info['password'] = new_password
                return f'У пользователя {login} старый пароль {old_password} изменен на {new_password}.'
        return 'Неверный логин.'

# Этот метод во всех заданиях нужен для того, что-бы создать список существующих созданных мной методов для отображения
# их на консоли для пользователя. Также, некоторые методы - запретные, потому что либо будут не нужны
# пользователю, либо будут портить работу программы.
    def menu(self):
        list_of_methods = inspect.getmembers(Users, predicate=inspect.isfunction)
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
                parameter = ''
                without_parameters = ['show', 'show_list']
                if input_operation in without_parameters:
                    operation = eval(f'self.{input_operation}()')
                    print(operation)
                    continue
                try:
                    parameter = input('Введите логин: ')
                    operation = eval(f'self.{input_operation}(\'{parameter}\')')
                    print(operation)
                except TypeError:
                    password_functions = ['change_password', 'add_user']
                    if input_operation in password_functions:
                        parameter_password = input('Введите пароль: ')
                        operation = eval(f'self.{input_operation}(\'{parameter}\', \'{parameter_password}\')')
                        print(operation)
                    else:
                        parameter_login = input('Введите логин: ')
                        operation = eval(f'self.{input_operation}(\'{parameter}\', \'{parameter_login}\')')
                        print(operation)
            elif input_operation == 'quit':
                exit()
            else:
                print('Неверная операция.')
