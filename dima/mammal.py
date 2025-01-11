from dima.animal import Animal


class Mammal(Animal):
    def __init__(self, name, age, fur_color = 'Черный'):
        super().__init__(name, age)

        self.fur_color = fur_color

    def make_sound(self):
        return 'Рычание'