class Animal:
    def __init__(self, name = 'Животное', age = 10):
        self.name = name
        self.age = age

    def make_sound(self):
        return 'Я издаю звук!'