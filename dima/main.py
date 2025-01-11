from dima.bird import Bird
from dima.mammal import Mammal


beaver = Mammal('Бобер',28,'Коричневый')
print(beaver.fur_color)
print(beaver.name)
print(beaver.age)
print(beaver.make_sound())

bird1 = Bird('Семён',1337,'120 метров')
print(bird1.wing_span)
print(bird1.name)
print(bird1.age)
print(bird1.make_sound())