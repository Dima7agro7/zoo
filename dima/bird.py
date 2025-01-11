from dima.animal import Animal


class Bird(Animal):
    def __init__(self,name, age, wing_span  = 'Большой'):
        super().__init__(name, age)
        self.wing_span  = wing_span

    def make_sound(self):
        return 'чириканье'