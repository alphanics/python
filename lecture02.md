# 자료형

**메모리**를 **해석** 하는 방법

## 1. 자료형

* 숫자형
* 문자열
* 리스트
* 튜플
* 틱셔너리
* 집합
* 불

### 1.1 숫자형
```py
print(1234)
print(1+2)
print(12.34)
print(1+(2*3))
```

### 1.2 문자열

**작은따옴표('...')** 나 **큰따옴표("...")**로 감싸면 문자열

```py
print('C:\\some\\name')
print('"Isn\'t," they said.')
print(r'C:\some\name')
# 첫따옴표 앞에 r 을 붙여서 날 문자열 (raw string) 

print(3 * 'A' + 'ium')
# 연산가능

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# 삼중 따옴표 사용 : """...""" 또는 '''...'''.  

word = 'Python'
word[0]  # P
word[5]  # n
word[-1] # 뒤에서 n
word[-6] # 뒤에서 P
# 인덱스


word[:2] + word[2:] # Python
# 슬라이스 인덱스
# 어디부터:어디까지
# [:2] : 처음부터 2미만 : Py
# [2:] : 2부터 끝까지 : thon
# [1:4] : 1부터 4미만 : yth

```

### 3. 리스트

```
# 대괄호([...])
# 항목의 자료형은 다를 수 있다

squares = [1, 4, 9, 16, 25]
print(squares)

squares = [1, "abc", 3.14, 16+22, "20"+"30"]
print(squares)

print(squares[-1])
# 역순

print(squares[2:5])
print(squares[:])
# 슬라이스

squares = squares + [36, 49, 64, 81, 100]
print(squares)
# 리스트 연산(이어붙이기,append)
```

### 4. 튜플(tuple)
* 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
* 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 **값을 바꿀 수 없다**.

```py
t1 = ()
t2 = (1,)
# 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
t3 = (1, 2, 3)
t4 = 1, 2, 3
# 괄호( )를 생략해도 무방하다
t5 = ('a', 'b', ('ab', 'cd'))
```
* 튜플은 값을 변화시킬 수 없다는 점만 제외하면 리스트와 완전히 동일

사용법
```py
t1 = (1, 2, 'a', 'b')
print(t1[0])
#사용은 리스트처럼...
```

### 5. 딕셔너리

* 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형

영어사전처럼 people="사람", baseball="야구"처점 해석되는 자료형
```py
# Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있다. 
# 각각의 요소는 Key : Value 형태로 이루어져 있고 
# 쉼표(,)로 구분되어 있다.
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
# ※ Key에는 변하지 않는 값을 사용하고, 
# Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)
a = {1: 'hi'}
print(a)

# 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)

# 삭제
del a[1]

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])

# 주의사항 :  key값 중복
```

### 6. 집합(set)

* 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.
* 집합 자료형은 다음과 같이 **set** 키워드를 사용해 만들 수 
있다.
* 중복을 허용하지 않는다.
* 순서가 없다(Unordered).

```py
s1 = set([1,2,3])
s1
# 결과 : {1, 2, 3}
s2 = set("Hello")
s2
print(type(s2))
# 결과 : {'e', 'H', 'l', 'o'}
# ※ 비어 있는 집합 자료형은 s = set()로 만들수 있다.
```

### 7. 불
* 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다. 
* 불 자료형은 다음 2가지 값만을 가질 수 있다.
  * True - 참
  * False - 거짓

--------------------
