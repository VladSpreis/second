from time import sleep


class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        for i in range(0, 3):
            if i == 0:
                print(f" TrafficLight is switching!")
                sleep(2)
                print(f" TrafficLight in position: {TrafficLight.__color[i]}")
                sleep(7)
            elif i == 1:
                print(f" TrafficLight in position: {TrafficLight.__color[i]}")
                sleep(2)
            elif i == 2:
                print(f" TrafficLight in position: {TrafficLight.__color[i]}")
                sleep(6)


TrafficLight = TrafficLight()
TrafficLight.running()