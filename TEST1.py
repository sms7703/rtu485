import socket
import ssl

HOST = '119.205.235.142'
PORT = 10443

# 소켓 생성 및 SSL 래핑
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(sock)

# 서버 연결
ssl_sock.connect((HOST, PORT))

# 데이터 전송
ssl_sock.sendall(b'GET / HTTP/1.1\r\nHost: 119.205.235.142\r\n\r\n')

# 응답 수신 및 출력
data = ssl_sock.recv(1024)
print(data.decode())

# 소켓 종료
ssl_sock.close()








import requests

url = "https://<IP 주소>:<포트 번호>"
data = {"key1": "value1", "key2": "value2"} # 보내고자 하는 데이터를 딕셔너리 형태로 정의합니다.

response = requests.post(url, data=data)

print(response.text)