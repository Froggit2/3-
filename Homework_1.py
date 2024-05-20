class Car:
    prise = 1000000
    def horse_powers(self, engine):
        self.engine = 1000
        print('Лошадиные силы:', engine)

class Nissan(Car):
    prise = 1500000
    def horse_powers(self, engine):
        engine = 2500
        print('Лошадиные силы:', engine)


class Kia(Car):
    prise = 2000000
    def horse_powers(self, engine):
        engine = 5000
        print('Лошадиные силы:', engine)

Mashina_3 = Kia()
Mashina_2 = Nissan()

Mashina_2.horse_powers(0)
Mashina_3.horse_powers(0)