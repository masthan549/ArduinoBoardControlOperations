'''import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()

pinNumber = 9
pinNumber2 = 10
pinNumber3 = 11

time.sleep(5)
board.digital[pinNumber].write(1)
board.digital[pinNumber2].write(1)
board.digital[pinNumber3].write(1)

time.sleep(2)
board.digital[pinNumber].write(0)
board.digital[pinNumber2].write(0)
board.digital[pinNumber3].write(0)

time.sleep(2)
board.digital[pinNumber].write(1)
board.digital[pinNumber2].write(1)
board.digital[pinNumber3].write(1)

'''
import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
res = md5("CR Change Analysis_rescr24912_rescr24913.docx")
n= 2
md5 = [res[i:i+n] for i in range(0, len(res), n)]

md5_str = "["
flag = False
for indx in md5:
    if flag is False:
        md5_str = md5_str + str(indx)
        flag = True
    else:
        md5_str = md5_str +" "+ str(indx)
md5_str= md5_str+"]"

print(md5_str)