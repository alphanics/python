#!/usr/bin/env python
import signal
import sys
import socket


# 설정값
HOST = '127.0.0.1'
PORT = 9999


# 소켓 객체 생성
# 주소 체계 : IPv4(AF_INET),
# 소켓 타입 : TCP(SOCK_STREAM), UDP(SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('1. 서버 socket 생성: ', server_socket)

# 포트사용중(10048) 에러 해결
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('2. 서버 socket 옵션설정')

# bind 함수
# 포트 연결
# PORT : 1-65535 숫자 사용
server_socket.bind((HOST, PORT))
print('3. 서버 socket bind()', HOST, PORT)

# listen 함수
server_socket.listen()
print('4. 서버 socket listen()')


# accept 함수
client_socket, addr = server_socket.accept()
print('4. 서버 socket accept()')

# 접속한 클라이언트 주소.
print('5. 클라이언트 접속 확인 : ', addr)

# 무한루프
while True:
    # { while
    # 수신대기
    data = client_socket.recv(1024)
    print('6. 데이터 수신 ', addr, data)

    # 빈문자열 : 중지
    if not data:
        print('x. 클라이언트 접속 종료')
        break

    # 수신받은 문자열을 출력합니다.
    print('받은 데이터 ', addr, data.decode())

    # 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코)
    client_socket.sendall(data)
    print('7. 데이터 송신 ', data)
    # while}


# 소켓 종료
client_socket.close()
server_socket.close()
print('tcpserver.py 종료')
