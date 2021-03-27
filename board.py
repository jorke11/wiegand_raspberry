import RPi.GPIO as IO
import time

<<<<<<< HEAD
class BOARD:
    
    def shutdown(self,pin):
        IO.setwarnings(False)
        IO.setmode(IO.BOARD)
        IO.setup(pin, IO.OUT)
        IO.output(pin, IO.LOW)


=======


class BOARD:
>>>>>>> 9a2b325974ad9898b48e49174c0c788cfb31d455
    def activateRelay(self,pin,delay):
        IO.setwarnings(False)
        IO.setmode(IO.BOARD)
        IO.setup(pin, IO.OUT)

        print("ACTIVE RELAY")
        IO.output(pin, IO.HIGH)
        time.sleep(delay)
        print("INACTIVE RELAY")
        IO.output(pin, IO.LOW)
        time.sleep(delay)
        
