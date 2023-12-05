import serial, time
from datetime import datetime

req = [0x7e, 0x01, 0x01, 0xD1, 0x88]
res = [0x7E,0x01,0x02,0x00,0x29,0x00,0xDC,0x00,0x96,0x00,0x0A,0x00,0x00,0x00,0x07,0x00,0x00,0x00,0x00,0x03,0xC9,0xF2,0x12,0x00,0x00,0x00,0x00,0x00,0x00,0x2D,0xC6,0x02,0x01,0x86,0x01,0x86,0x00,0xAA,0x00,0xAA,0x00,0x00,0x02,0x9E,0x00,0x01,0x12,0xC6]

def ts():
    return datetime.fromtimestamp(time.time())

def do():
    con = serial.Serial("com12", "9600")

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
    

