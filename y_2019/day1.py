from .common import AoCDay


class Day(AoCDay):
    def __init__(self):
        super().__init__(1)

    def _preprocess_input(self):
        self.__mass_list = [int(i) for i in self._input_data]

    def _calculate_1(self):
        return sum(self.fuel_from_mass(mass) for mass in self.__mass_list)

    def _calculate_2(self):
        return sum(self.total_fuel_from_mass(mass) for mass in self.__mass_list)

    @staticmethod
    def fuel_from_mass(mass):
        return mass // 3 - 2

    @staticmethod
    def total_fuel_from_mass(mass):
        if (w := Day.fuel_from_mass(mass)) < 0:
            return 0
        return w + Day.total_fuel_from_mass(w)
