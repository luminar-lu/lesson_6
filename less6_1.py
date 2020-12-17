class TrafficLight:
    __color = "red"
    def running(self = "a"):
        for i in range(3):
            for i in range(7, 0, -1):
                print(f"{TrafficLight.__color}  light. {i} seconds left")
            TrafficLight.__color = "yellow"
            for i in range(2, 0, -1):
                print(f"{TrafficLight.__color}  light. {i} seconds left")
            TrafficLight.__color = "green"
            for i in range(7, 0, -1):
                print(f"{TrafficLight.__color}  light. {i} seconds left")
            TrafficLight.__color = "yellow"
            for i in range(2, 0, -1):
                print(f"{TrafficLight.__color}  light. {i} seconds left")
        return(self)
TrafficLight.running()
# возможно я не понял задание, или тему классов впринципе,
# но вроде как это та же функция, но с другим синтаксисом.

