from task1 import CharQueue
from task2 import PriorityCharQueue
from task3 import Users


def task1():
    print('Задание 1. Символьная очередь.')
    try:
        input_capacity = int(input('Введите вместимость очереди: '))
        queue1 = CharQueue(input_capacity)
        queue1.execution()
    except ValueError:
        print('Это должно быть положительное число!')
    except AssertionError:
        print('Это должно быть положительное число!')


def task2():
    print('Задание 2. Символьная очередь с приоритетом.')
    try:
        input_capacity = int(input('Введите вместимость очереди: '))
        queue1 = PriorityCharQueue(input_capacity)
        queue1.execution()
    except ValueError:
        print('Это должно быть положительное число!')
    except AssertionError:
        print('Это должно быть положительное число!')


def task3():
    print('Задание 3. Информация о пользователях.')
    try:
        users = Users()
        users.execution()
    except Exception:
        print('Что-то пошло не так.')


def main():
    # task1()
    # task2()
    # task3()
    pass


if __name__ == '__main__':
    main()




