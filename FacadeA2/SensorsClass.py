
class Sensors():  
    ##Sensors:  
    
    #both
    def voltage(self):
        #Check voltage (again during shutdown)
        return '    Check voltage \n'
    def TempPower(self):
          return '    Check the temperature in the power supply \n'
    def TempVideoCard(self):
          return '    Check the temperature in the video card \n'
    def TempRam(self):
          return '    Check the temperature in the RAM \n'
    def TempAll(self):
          return '    Check the temperature of all systems \n'
    