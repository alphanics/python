# 사용자 입력과 출력

* 사용자 입력
* print 자세히 알기
    * 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
    * 문자열 띄어쓰기는 콤마로 한다
    * 한 줄에 결괏값 출력하기
* 파일 생성    
* 파일 쓰기 
* 파일 읽기


## 사용자 입력
```py
def password():
    pw = input("password를 입력하시오 : ")
    print("입력한 패스워드는" + pw + "입니다.")
    return pw
pw = password()
print(pw)
```

## print 자세히 알기
```py
# 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short")

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')
```


## 파일 생성
```py
# r:읽기모드
# w:쓰기모드
# n:추가모드
f = open("foo.txt", 'w')
f.close()
```

## 파일 쓰기
```py
f = open("foo.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
```

## 파일 읽기
```py
# 파일의 첫 번째 줄을 읽어 출력하는 경우
f = open("foo.txt", 'r')
line = f.readline()
print(line)
f.close()

# 모든 줄을 읽어서 화면에 출력
f = open("foo.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# 모든 줄을 읽어서 화면에 출력
f = open("foo.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
```

## with문과 함께 사용하기
```py
with open("foo.txt", "w") as f:
    f.write("abcde\n")
    f.write("1234\n")
    f.write("AAAA\n")
```
* with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다.    
