import random

class NotImplementedException(Exception):
    ...

class Robber:
    def __init__(self, name, noise=None, money=None, strength=None, luck=None):
        self.name = name
        self.noise = noise
        self.money = money
        self.strength = strength
        self.luck = luck

    def __str__(self):
        return f'Грабитель: имя= {self.name}: шум={self.noise}: деньги={self.money}: сила={self.strength}: удача={self.luck}'

    def hack_safe(self):
        while True:
           s = input("Какой код от сейфа (1-20)?")
           s = int(s)
           win = random.randint(1, 20)

           if s == win or random.randint(1, 20) <= self.luck:
              print("Удача, деньги у вас в кармане!")
              self.money += random.randint(1000, 5000)
              return True
           else:
              print(f"Сейф не открылся, код {win}, сработала сигнализация!")
              self.money += 5
              if self.noise >= 10:
                print("Слишком много шума! Охрана бежит!")
                return False

           repeat = input("Повторите попытку: да/нет")
           if repeat.strip().lower() != 'да':
            return False

def main():
    print("Вечер добрый, напарник!")

    enter = input("Готов ограбить этот банк и стать самым богатым (да/нет)? ")

    if enter.strip().lower() == 'да':
        print("Давай сделаем это!")

    elif enter.strip().lower() == 'нет':
        print("Мы же так долго готовились к этому ограблению!")

    choose = input("Как попадем в здание банка: через запасной вход (1), через окно (2), через вентиляцию (3)")

    try:
        if choose == '1':
           robber = Robber("Алексей", 11, 0, 5,11)
           print(robber)
           robber.hack_safe()

        elif choose == '2':
            raise NotImplementedException ("Разбивать окно будет громко!")

        elif choose == '3':
            raise NotImplementedException("Вентиляционная система не выходит к комнате с сейфом! Сработала сигнализация!")

    except NotImplementedException as err:
        print(f'Не сработало! {err}')

    print('Бежим!')


if __name__ == "__main__":
    main()
