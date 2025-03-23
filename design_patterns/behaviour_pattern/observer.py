class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class WeatherStation(Observable):

    def __init__(self):
        super().__init__()
        self.temperature = None

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

class Observer:
    def update(self, observable):
        pass


class PhoneDisplay(Observer):
    def update(self, observable):
        if isinstance(observable, WeatherStation):
            temperature = observable.temperature
            print(f"{type(self).__name__} : Temperature is {temperature} degrees Celsius")

class TVDisplay(Observer):
    def update(self, observable):
        if isinstance(observable, WeatherStation):
            temperature = observable.temperature
            print(f"{type(self).__name__} : Temperature is {temperature} degrees Celsius")

class PCDisplay(Observer):
    def update(self, observable):
        if isinstance(observable, WeatherStation):
            temperature = observable.temperature
            print(f"{type(self).__name__} : Temperature is {temperature} degrees Celsius")


# Observable object
weather_station = WeatherStation()

# Observer objects
phone_display = PhoneDisplay()
tv_display = TVDisplay()
pc_display = PCDisplay()

# adding subscription
displays = [phone_display, tv_display, pc_display]
for display in displays:
    weather_station.add_observer(display)

# Observers getting notified with the change in observable
weather_station.set_temperature(25)
