class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    #
    # def go(self, speed):
    #     self.speed = speed
    #     return speed
    # вот тут я получил предупреждения о статиках, полез в видос с разбором, и понял, что-то
    # я не то делаю.
    # def stop(self, speed):
    #     self.speed = 0
    #     return speed
    #
    # def turn(self, direction):
    #     self._direction = direction
    #     return direction

    @staticmethod
    def go():
        print("Go")

    @staticmethod
    def stop():
        print("Car stopped")

    @staticmethod
    def turn(turn_direction):
        print(f"Car turned {turn_direction}")

    def show_speed(self):
        print(f"Speed {self.speed}")

    # class TownCar(Car):
    #     def town_car_description(self, speed_stop, turn_direction):
    #         self.speed_stop = speed_stop(self.stop)
    #         self.turn_direction = turn_direction(self.turn)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if 60 < self.speed:
            print("Speeding")

    def route(self, turn):
        super().turn
        print(f'{turn}')



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if 40 < self.speed:
            print("Speeding")


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    town_cars = TownCar(40, "Red", "Random_car", False)
    town_cars.show_speed()
    town_cars.stop()
    town_cars.turn("Left")
    print(f'Police car? {town_cars.is_police}')

if __name__ == '__main__':
    town_cars = PoliceCar(120, "Blue", "Random_car", True)
    town_cars.show_speed()
    town_cars.stop()
    town_cars.turn("Right")
    print(f'Police car? {town_cars.is_police}')

