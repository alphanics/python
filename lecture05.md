# 함수
* 함수란 무엇인가?
* 함수를 사용하는 이유는 무엇일까?
* 파이썬 함수의 구조
* 매개변수와 인수
* 입력값과 결과값에 따른 함수의 형태
* 일반적인 함수
* 입력값이 없는 함수
* 결과값이 없는 함수
* 입력값도 결과값도 없는 함수
* 매개변수 지정하여 호출하기
* 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
* 함수의 결과값은 언제나 하나이다
* 매개변수에 초기값 미리 설정하기
* 함수 안에서 선언한 변수의 효력 범위
* 함수 안에서 함수 밖의 변수를 변경하는 방법
* lambda

----------

## 1. 함수란 무엇인가?
* 입력 -> 처리(함수) -> 결과

## 2. 함수를 사용하는 이유는 무엇일까?
* 반복
* 구조화

## 3. 파이썬 함수의 구조
파이썬 함수의 구조는 다음과 같다.
```py
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
```
* def는 함수를 만들 때 사용하는 예약어
* 함수 이름은 함수를 만드는 사람이 임의로 만들 수 있다. 
* 함수 이름 뒤 괄호 안의 매개변수는 이 함수에 입력으로 전달되는 값을 받는 변수이다. 

```py
# add 함수
# 입력 2개, 출력 1개
def add(a, b):
    return a + b


a = 3
b = 4
c = add(a, b)
print("add 함수 결과 : ", c)

```

## 4. 매개변수와 인수
* 매개변수(parameter)와 인수(arguments)는 혼용해서 사용되는 헷갈리는 용어이므로 잘 기억해 두자

```py
def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수
```

## 5. 입력값과 결괏값에 따른 함수의 형태
### 5.1 일반적인 함수
```py
def 함수이름(매개변수):
    <수행할 문장>
    ...
    return 결과값
```    

### 5.2 입력값이 없는 함수
```py
def say(): 
    return 'Hi'
```

### 5,3 결괏값이 없는 함수
```py
def add(a, b): 
...     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
```
### 5.4 입력값도 결괏값도 없는 함수
```py
def say(): 
    print('Hi')
```

## 6. 매개변수 지정하여 호출하기
```py
def add(a, b):
    return a+b

result = add(a=3, b=7)  # a에 3, b에 7을 전달
print(result) 
result = add(b=5, a=3)  # b에 5, a에 3을 전달 
print(result)   
```

## 7. 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
```py
def 함수이름(*매개변수): 
    <수행할 문장>
    ...
```
* 일반적으로 볼 수 있는 함수 형태에서 괄호 안의 매개변수 부분이 **[*매개변수]** 로 바뀌었다.

### 7.1 여러 개의 입력값을 받는 함수 만들기
```py
def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i 
    return result 

result = add_many(1,2,3)    
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)
```

```py
def add_mul(choice, *args): 
    if choice == "add": 
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul": 
        result = 1 
        for i in args: 
            result = result * i 
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)

```

### 7.2 키워드 파라미터 kwargs
* 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙인다.

* 입력값 a=1 또는 name='foo', age=3이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다
* 즉 **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.

```py
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='foo', age=3)

```

## 8. 함수의 결괏값은 언제나 하나이다

```py
def add_and_mul(a,b): 
    return a+b, a*b
result = add_and_mul(3, 4)
print(result)
# 결과값 result = (7, 12)

result1, result2 = add_and_mul(3, 4)

```    
* 결괏값은 a+b와 a*b 2개인데 결괏값을 받아들이는 변수는 result 하나만 쓰였으니 오류가 발생하지 않을까? 
* 당연한 의문이다. 하지만 오류는 발생하지 않는다. 
* 그 이유는 함수의 결괏값은 2개가 아니라 언제나 1개라는 데 있다. 
* add_and_mul 함수의 결괏값 a+b와 a*b는 튜플값 하나인 (a+b, a*b)로 돌려준다.

```py
def add_and_mul(a,b): 
    return a+b, a*b
result = add_and_mul(3, 4)
print(result)
# 결과값 result = (7, 12)
result1, result2 = add_and_mul(3, 4)
```
* 만약 이 하나의 튜플 값을 2개의 결괏값처럼 받고 싶다면 다음과 같이 함수를 호출하면 된다.
* 이렇게 호출하면 result1, result2 = (7, 12)가 되어 result1은 7이 되고 result2는 12가 된다.

## 9. 매개변수에 초기값 미리 설정하기
```py
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("장국태", 33)
say_myself("박기태", 33, True)        
```        


## 10. 함수 안에서 선언한 변수의 효력 범위
* 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관이 없다.
```py
a = 1
def vartest(x):
    a = a +1

vartest(a)
print(a)
```

## 11. 함수 안에서 함수 밖의 변수를 변경하는 방법
### 11.1 return 사용하기
```py
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a) 
print(a)
```
### 11.2 global 사용하기
```py
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)
```


## 12. lambda(람다식)
* lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다

사용법은 다음과 같다.

> lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
```py
add1 = lambda a, b: a+b
result = add1(3, 4)
print(result)
# ※ lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

def add2(a, b):
    return a+b
result = add2(3, 4)
print(result)
# add1(), add2()는 완전 일치
```