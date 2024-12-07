from typing import Type
from AdapterClass import AdapterBitoXML

class WeatherSystem():
    def XML(self, adaptor : Type[AdapterBitoXML])->None:
        result = adaptor.Binary() 
        print(result)