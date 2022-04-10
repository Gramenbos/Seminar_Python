import complex
import rational


def enter():
    """ Функция предназначена для ввода пользователем значений для выполнения с ними математических действий.
        Первый этап запроса типа вводимых данных:
        1 - комплексные числа
        2 - рациональные числа
        3 - завершение работы функции
        второй этап запрос ввода первого значения, ввод второго значения, ввод знака действия."""
    print('Выберите тип вводимых данных: ', '1 - Комплексные числа ',
          '2 - Рациональные числа', '3 - Завершение работы с модулем', sep='\n')

    number_type = int(input())
    if number_type == 1:
        num1 = input('Введите первое число: ')
        num2 = input('Введите второе число: ')
        sign = input('Введите знак действия: ')
        print(complex.count(num1, num2, sign))
        enter()
    elif number_type == 2:
        num3 = input('Введите первое число: ')
        num4 = input('Введите второе число: ')
        sign1 = input('Введите знак действия: ')
        print(rational.calc(num3, num4, sign1))
        enter()
    elif number_type == 3:
        print('До новых встреч!!!!')
        exit()
    else:
        print('Неверный ввод, повторите выбор или нажмите 3 для выхода!')
        enter()