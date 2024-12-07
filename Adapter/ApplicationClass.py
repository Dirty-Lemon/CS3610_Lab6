from WeatherSensorClass import WeatherSensor

class Application:
    def __init__(self):
        self.weather = WeatherSensor()

    def Binary(self):
        return f'Aplication displays data: {self.weather.get_Weather()} \n' # from several sensors'  
   