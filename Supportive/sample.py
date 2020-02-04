import pyfirmata
import time
from pyfirmata import INPUT, OUTPUT, PWM


print("preprating5")
board = pyfirmata.Arduino('COM4')
board.analog[1].mode = OUTPUT
board.analog[1].write(5)
time.sleep(2)





'''print("preprating3")
ob = board.get_pin('a:2:i')
print(ob.read())
print("preprating4")'''

#Analog

# Digital
'''
pinNumber = 9
pinNumber2 = 10
pinNumber3 = 12



board.digital[pinNumber3].write(1)
time.sleep(2)
board.digital[pinNumber3].write(0)
time.sleep(2)
board.digital[pinNumber3].write(1)'''