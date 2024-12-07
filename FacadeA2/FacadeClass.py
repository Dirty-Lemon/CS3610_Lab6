
from VideoCardClass import VideoCard
from RAMClass import RAM
from HDDClass  import HDD
from ODRClass import ODR
from PowerSupplyClass import PowerSupply
from SensorsClass import Sensors
from typing import Type
import random

class Facade:
    """
    subsystem order
    1.Video card​ 
    2. RAM​
    3. HDD​
    4. Optical disc reader​
    5. Power supply​
    6. Sensors
    """

    def __init__(self, subsystem1: Type[VideoCard]=None, subsystem2: Type[RAM]=None, subsystem3: Type[HDD]=None, subsystem4: Type[ODR]=None, subsystem5: Type[PowerSupply]=None, subsystem6: Type[Sensors]=None)-> None:
        self.__subsystem1=subsystem1 if subsystem1 else VideoCard()
        self.__subsystem2=subsystem2 if subsystem2 else RAM()
        self.__subsystem3=subsystem3 if subsystem3 else HDD()
        self.__subsystem4=subsystem4 if subsystem4 else ODR()
        self.__subsystem5=subsystem5 if subsystem5 else PowerSupply()
        self.__subsystem6=subsystem6 if subsystem6 else Sensors()

    def BeginWork(self):
        result="\nTurning on the computer: \n"
        result+="".join([
            self.__subsystem1.launch(), self.__subsystem1.launch(), self.__subsystem1.DisplayRam(), self.__subsystem1.DisplayToDisk(), self.__subsystem1.connection(), self.__subsystem1.output(),
            self.__subsystem2.launch(), self.__subsystem2.memoryA(),
            self.__subsystem3.launch(), self.__subsystem3.boot(),
            self.__subsystem4.startup(), self.__subsystem4.checking(),
            self.__subsystem5.ApplyPower(), self.__subsystem5.VideoCardPower(),self.__subsystem5.RamPower(),self.__subsystem5.DRPower(),self.__subsystem5.HDDPower(),
            self.__subsystem6.voltage(),self.__subsystem6.TempPower(),self.__subsystem6.TempVideoCard(),self.__subsystem6.TempRam(),self.__subsystem6.TempAll(),
        ])
        if random.random() < 0.1: #70 percent chance of succesfully loading
            print (f"{result}")
        else: print ("\n Device was loaded unsuccessfully: the loading progress was interrupted")
        return None

    def EndWork(self):
        result="\nShutting down the computer: \n"
        result+="".join([
            self.__subsystem1.DisplayFarewell(), self.__subsystem2.memoryA(), self.__subsystem2.memoryC(), self.__subsystem4.ReturnToOri(),
            self.__subsystem5.StopVideoCardPower(), self.__subsystem5.StopDRPower(), self.__subsystem5.StopHDDPower(),self.__subsystem5.shutdown(), self.__subsystem6.voltage()])
        print (f"{result}")
        return None