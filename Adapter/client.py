from WeatherSensorClass import WeatherSensor
from AdapterClass import AdapterBitoXML
from WeatherSystemClass import WeatherSystem

start=WeatherSensor()
adaptor = AdapterBitoXML(start)
end = WeatherSystem()
(end.XML(adaptor))