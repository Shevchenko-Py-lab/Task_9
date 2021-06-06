# тут то же самое всё, разве что, я посчитал толщину полотна не константой, исходя из условий,
# толщина полотна может быть разной

# Защищённая переменная создаётся добавлением одного знака подчёркивания перед именем переменной.
# При использовании защищённых переменных их значения могут меняться только в пределах одного и того же пакета.
import sys


class Road:
    MASS = 25  # кг/1м2
    length = 5
    width = 5
    thickness = 5

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.thickness = thickness

    def calculation(self):
        mass = (self._width * self._length * self.thickness * self.MASS) / 1000
        return mass


if __name__ == '__main__':
    _script_name, long, wide, thick = sys.argv
    calculate_mass = Road(int(long), int(wide), int(thick))

    print(calculate_mass.calculation())
