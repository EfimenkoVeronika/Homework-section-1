import random

class NotImplementedException(Exception):
    ...

class ValueException(Exception):
    ...


def hacking():

    while True:

        print("Хорошо, там как раз должно быть открыто, за дверью стоит сейф!")

        s = input("Какой код от сейфа (1-20)?")

        if not s.isdigit():
            raise ValueException('Нужно было ввести число!')

        s = int(s)

        win = random.randint(1, 20)

        if s == win:
            print("Удача, деньги у вас в кармане!")
        else:
            print(f"Сейф не открылся,код {win},сработала сигнализация!")

        repeat = input('Повторите попытку? (да/нет)')

        if repeat.strip().lower() == 'нет':
            break

def window():
    raise NotImplementedException("Разбивать окно будет громко!")

def ventilation():
    raise NotImplementedException("Вентиляционная система не выходит к комнате с сейфом!")

print("Вечер добрый, напарник!")

enter = input("Готов ограбить этот банк и стать самым богатым (да/нет)?")

if 'да' == enter:
    print("Давай сделаем это!")

elif 'нет' == enter:
    print("Мы же так долго готовились к этому ограблению!")

choose = input("Как попадем в здание банка: через запасной вход (1), через окно (2), через вентиляцию (3)")

try:
    if '1' == choose:
        hacking()
    elif '2' == choose:
        window()
    elif '3' == choose:
        ventilation()

except NotImplementedException as err:
    print(f'Не работает: {err}')

except ValueException as err:
    print(f'Нет, всё-таки нужно число!А вы ввели "{s}", получено исключение: {err}')

print('Бежим!')
