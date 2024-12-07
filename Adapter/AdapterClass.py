
from typing import Type
from ApplicationClass import Application

class AdapterBitoXML():
    def __init__ (self, lan: Type[Application])-> None:
        lan=Application()
        self.language= lan

    def Binary(self):
        return f'Converting to XML: {self.language.Binary()} Data is now in XML'