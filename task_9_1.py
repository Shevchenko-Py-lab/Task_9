import time


class TrafficLight:

    # атрибут класса
    def __init__(self):
        self.colour = None

    # метод класса
    def light_running(self):
        self.__colour = 'Red'
        yield self.__colour
        time.sleep(7)
        self.__colour = 'Yellow'
        yield self.__colour
        time.sleep(2)
        self.__colour = 'Green'
        yield self.__colour
        time.sleep(5)


if __name__ == '__main__':
    traffic_light = TrafficLight()  # экземпляр

    lights_order = []

    for light in traffic_light.light_running():
        lights_order.append(light)
        print(lights_order)
    print("Success")

    assert (lights_order == ['Red', 'Yellow', 'Green']), "Error. Check class method"
