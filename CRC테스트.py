def crc16(data):
    crc = 0xFFFF
    
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    
    # 상위 하위 비트 스왑
    return [(crc >> 8), (crc & 0xFF)]

# 데이터 입력
data = [0x7E,0x01,0x08,0x00,0x26,   #0026 총길이 38자
                0x00,0xDC,
                0x00,0x96,
                0x00,0x00,0x00,0x0a,
                0x00,0xdc,
                0x00,0xdc,
                0x00,0xdc,
                0x00,0x96,
                0x00,0x96,
                0x00,0x96,
                0x00,0x00,0x00,0x0a,
                0x03,0xE7,
                0x02,0x58,
                0x00,0x00,0x00,0x00,0x00,0xFF,0xFF,0xFF,
                0x00,0x00]
#여기서 나온 값은 스왑해서 사용해야함 예시 결과값 01 02 나오면 crc칸에 02 01 넣어야함
# Calculate CRC16
crc_result = crc16(data)
hex_result = [hex(value) for value in crc_result]

# Print the CRC result
print("CRC16(10진): ", crc_result)
print("CRC16(16진): ", hex_result)
