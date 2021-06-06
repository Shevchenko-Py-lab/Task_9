class Stationery:
    def __init__(self, title):
        self.title = title
        print(title)

    @staticmethod
    def draw():
        print("Запуск отрисовки")


class Pen(Stationery):

    @staticmethod
    def draw():
        print("Синие штрихи")

    # staticmethod, работало при вызове нормально, потом я с несколькими экземплярами
    # начал прооверку, в окне вывода появился None, и только потом draw, поэтому переписал
    # статиком

    # def draw(self):
    #     self.draw = "Синие штрихи"
    #     return self.draw


class Pencil(Stationery):

    @staticmethod
    def draw():
        print("Серые штрихи")

    # def draw(self):
    #     self.draw = "Серые штрихи"


class Handle(Stationery):

    @staticmethod
    def draw():
        print("Чёрные штрихи, не отстираешь потом")

    # def draw(self):
    #     self.draw = "Чёрные штрихи, не отстираешь потом"


if __name__ == "__main__":
    check_stationary = Stationery("Канцтовар")
    check_stationary.draw()
    check_this = Pen("Ручка")
    check_this.draw()
    check_last = Handle("Маркер")
    check_last.draw()
