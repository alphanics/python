import socket


# 서버 주소
HOST = '127.0.0.1'
# 서버 포트
PORT = 9999


# 소켓 생성
# 주소 체계 : IPv4
# 소켓 타입 : TCP(SOCK_STREAM), UDP(SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('1. 클라이언트 소켓 생성', client_socket)

# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
client_socket.connect((HOST, PORT))
print('2. 서버 접속', HOST, PORT)

for idx in range(1, 11):
    # 메시지 전송
    client_socket.sendall('안녕'.encode())
    print('3. SEND')
    # 메시지 수신
    data = client_socket.recv(1024)
    print('4. RECV', repr(data.decode()))

for idx in range(1, 11):
    # 메시지 전송
    SendBytes = bytearray()
    SendBytes.append(123)
    SendBytes.append(125)
    SendBytes.append(123)
    client_socket.send(SendBytes)

    # 메시지 수신
    data = client_socket.recv(1024)
    print('4. RECV', repr(data.decode()))





# 소켓을 닫습니다.
client_socket.close()
print('5. tcpclient.py 종료')
