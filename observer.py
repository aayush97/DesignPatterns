from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()
    
    def get_temperature(self):
        return self.temperature
    
    def get_humidity(self):
        return self.humidity
    
    def get_pressure(self):
        return self.pressure

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
    
    # other WeatherData methods here
        
class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")

class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperatures = []
        self.humidities = []
        self.pressures = []
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self.temperatures.append(self.weather_data.get_temperature())
        self.humidities.append(self.weather_data.get_humidity())
        self.pressures.append(self.weather_data.get_pressure())
        self.display()

    def display(self):
        print(f"Average temperature: {sum(self.temperatures)/len(self.temperatures)}")
        print(f"Average humidity: {sum(self.humidities)/len(self.humidities)}")
        print(f"Average pressure: {sum(self.pressures)/len(self.pressures)}")

class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.current_pressure = 29.92
        self.last_pressure = None
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self):
        self.last_pressure = self.current_pressure
        self.current_pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        print("Forecast: ", end="")
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        elif self.current_pressure < self.last_pressure:
            print("Watch out for cooler, rainy weather")

if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)
    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)