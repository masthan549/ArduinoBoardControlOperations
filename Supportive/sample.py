import pyfirmata
import time


print("preprating5")
board = pyfirmata.Arduino('COM4')

print("preprating3")
it = pyfirmata.util.Iterator(board)
it.start()



print("preprating2")
#ob = board.get_pin('a:2:o')
#ob.read()

board.analog[2].write(1)
#Read anf write (dig to Analog)
ob = board.get_pin('a:2:i')
while True:
    board.digital[9].write(1)
    time.sleep(2)
    print(ob.read())
    time.sleep(2)
    board.digital[9].write(0)
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