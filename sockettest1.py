"""
import socket
#1번째 방법
with socket.socket() as s:	 #close를 해주지 않아도 자동으로 닫음
    
    addr=("119.205.235.142",10443) 	#도메인 주소, 포트, 443web
    
    s.connect(addr)		#통신 시작
    
    s.send("GET \n".encode()) 	#GET 메서드, 네트워크로 데이터를 보내려면 encoding을 해주어야함
    
    data=s.recv(1024)		#데이터 1024byte만큼 받기
    
    print(data.decode())
    
    """
    
    