import sys


class Worker:
    def __init__(self, name, surname, position, income):
        # self.name = "Default"
        # self.surname = "Default"
        # self.position = "Default"
        # self._income = "Default"
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name}, {self.surname}, {self.position}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


if __name__ == '__main__':
    dict_income = {"wage": int(input("enter wage ")), "bonus": int(input("enter bonus "))}
    # dict_income = {"wage": 100, "bonus": 15}
    _script_name, inp_name, inp_surname, inp_position = sys.argv
    full_record = Position(inp_name, inp_surname, inp_position, dict_income)
    # full_record = Position("Vasya", "Pupkin", "Manager", dict_income)

    print(f'{full_record.get_full_name()}, доход {full_record.get_total_income()} денег')
