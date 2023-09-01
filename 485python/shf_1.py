import serial, time
from datetime import datetime

req = [0x7e, 0x01, 0x01, 0xD1, 0x88]
res = [0x7E,0x01,0x02,0x00,0x16,0x03,0x48,0x02,0xA8,0x02,0xB2,0x02,0x20,0x00,0x00,0x02,0x9B,0x00,0x00,0x00,0x00,0x00,0x00,0x02,0x9A,0x00,0x01,0xCB,0xC7]

def ts():
    return datetime.fromtimestamp(time.time())


def do():
    con = serial.Serial("com5", "9600")

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
    
