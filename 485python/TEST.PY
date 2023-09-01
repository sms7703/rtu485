import serial
from datetime import datetime
import time

req = bytes([0x7e, 0x01, 0x01, 0xD1, 0x88])
res = bytes([0x7E, 0x01, 0x02, 0x00, 0x1A, 0x00, 0xDC, 0x00, 0x96, 0x00, 0x0A, 0x00, 0xDC, 0x00, 0x96, 0x00, 0x0A, 0x03, 0xE7, 0x02, 0x58, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0x00, 0x01, 0x38, 0xA2])

def ts():
    return datetime.now()

def do():
    with serial.Serial("com2", 9600) as con:
        while True:
            if con.isOpen():
                result = con.read(5)
                print(ts(), result.hex())
                con.flushInput()
                con.flushOutput()
                time.sleep(0.1)

                if result == req:
                    con.write(res)

while True:
    try:
        do()
    except Exception as e:
        print("Exception!!")
        print(e)
