
class PowerSupply():
    ##Power supply:
     
    def ApplyPower(self):
        return '    Apply power \n'
    
    def VideoCardPower(self):
        return '    Supply power to the video card \n'
    def RamPower(self):
        return '    Supply power to the RAM \n'
    def DRPower(self):
        return '    Supply power to the disc reader \n'
    def HDDPower(self):
        return '    Supply power to the hard drive \n'

    #for shutdown
    def StopVideoCardPower(self):
        return '    Stop powering the video card \n'
    def StopRamPower(self):
        return '    Stop powering the RAM \n'
    def StopDRPower(self):
        return '    Stop powering the disc reader \n'
    def StopHDDPower(self):
        return '    Stop powering the hard drive \n'
 
    def shutdown(self):
        return '    Shutting down the computer \n'
