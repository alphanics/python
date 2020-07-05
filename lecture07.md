# 클래스
* 클래스와 객체
* 생성자(Constructor)
* 클래스의 상속
* 메서드 오버라이딩
* 클래스 변수

## 클래스와 객체
* 과자틀 → 클래스(class)
* 과자  → 객체(object)

클래스에는 필드(변수)와 메서드(함수)가 있다.

```py
# 파이썬 클래스의 가장 간단한 예
class Cookie:
    pass
```
* 위의 클래스는 아무 기능도 갖고 있지 않은 껍질뿐인 클래스이다
```py
# Cookie 클래스
class Cookie:
    pass

#  Cookie 클래스의 객체를 만드는 방법
a = Cookie()
b = Cookie()
```

## 계산기 클래스 만들기
```py
class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


# 객체 만들기
calc = Calculator()

# 메서드 호출방법#1
calc.setdata(10, 20)
print(calc.first)
print(calc.add())

# 메서드 호출방법#2
Calculator.setdata(calc, 10, 20)
print(calc.second)
print(Calculator.add(calc))
```


## 생성자 (Constructor)
이번에는 우리가 만든 Calculator 클래스를 다음과 같이 사용해 보자.
```py
a = Calculator()
a.add()

#Traceback (most recent call last):
# File "xxx.py", line 1, in <module>
# File "xxx.py", line 6, in add
# AttributeError: 'Calculator' object has no attribute 'first'
```
* setdata() 메서드를 수행하지 않고 add 메서드를 수행하면 self.first를 인식하지 못하여 오류가 난다.
* 클랙스가 객체화 될 때, 초기값이 필요하면 생성자를 사용하자
* 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미

```py
class Calculator:
    # Calculator 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = Calculator(4, 2)        
```


## 클래스의 상속

* 상속 : class 클래스이름(상속할 클래스이름) :
* 자식은 부모의 기능을 모두 사용할 수 있다.
```py
class MoreCalculator(Calculator):
    pass
```

* 기능추가
```py
class MoreCalculator(Calculator):
    def pow(self):
        result = self.first ** self.second
        return result

calc = MoreCalculator(3,4)        
print(calc.pow())
```

## 메서드 오버라이딩

* 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
* 메서드 오버라이딩(Overriding, 덮어쓰기)

```py
class MoreCalculator(Calculator):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        # 나누는 값이 0인 경우 0을 리턴하도록 수정
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

calc = MoreCalculator(3,4)
print(calc.div(3/0))
```


## 클래스 변수(field)
```py
class Family:
    lastname = "김씨"

# 클래스 변수는 위 예와 같이 클래스이름.클래스 변수로 사용할 수 있다.
print(Family.lastname)

# 객체를 통해서도 클래스 변수를 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname) # 김씨
print(b.lastname) # 김씨

# 클래스의 변수 변경
Family.lastname = "박씨"
 
# 객체의 변수도 변경된다
print(a.lastname) # 박씨
print(b.lastname) # 박씨

# id값을 확인하자
print( id(Family.lastname) )
print( id(a.lastname) )
print( id(b.lastname) )

#id 값이 모두 같다.
# Family.lastname
# a.lastname
# b.lastname은 모두 같은 메모리를 가리키고 있다.

```
