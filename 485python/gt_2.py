import serial, time
from datetime import datetime


req = [0x7e, 0x03, 0x03, 0x51, 0x29]
res = [0x7E,0x03,0x04,0x00,0x10,0x01,0x86,0x01,0x86,0x00,0x00,0x02,0x94,0x00,0x00,0x00,0x00,0x00,0x12,0xD6,0x80,0xC6,0x39]

def ts():
    return datetime.fromtimestamp(time.time())

def do():
    con = serial.Serial("com9", "9600")

    while True:
        if(con.isOpen()):
            result = con.read(5)
            print(ts(), result.hex())
            con.flushInput()
            con.flushOutput()
            time.sleep(0.1)
            
            if(len(result)==5):
                correct = True
                for i in range(0, 5):
                    if(req[i]!=result[i]):
                        correct=False
                        break

                if(correct):
                    con.write(res)
        else:
            con.open()

while True:
    try :
        do()
    except Exception as e:
        print("Exception!!")
        print(e)
    
