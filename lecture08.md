# 모듈(module)
* 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파일

## 사용법1
* import 모듈이름
```py
# mod1.py 파일을 포함한다
# mod2.py 파일을 포함한다
import mod1
import mod2

m1 = mod1.Mode1Class()
m2 = mod2.Mode2Class()
m1.Hello()
m2.Hello()
```

```py
#mod1.py
class Mode1Class:
    def __init__(self):
        self.name = "Mode1Class 생성자"

    def Hello(self):
        print(self.name)
```

```py
#mod2.py
class Mode2Class:
    def __init__(self):
        self.name = "Mode2Class 생성자"

    def Hello(self):
        print(self.name)
```

## 사용법2

* 모듈 이름을 붙이지 않고 바로 해당 모듈의 함수를 쓸 수 있다.

```py
from mod1 import add
from mod1 import add, sub
from mod1 import *
add(3, 4)
```

## if __name__ == "__main__": 의 의미
* 모듈은 실행 환경에 따라 문제가 발생할 수 있다.
```py
C:\> python
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod1
5
2
```
import mod1을 수행하는 순간 mod1.py가 실행이 되어 결괏값을 출력한다. 

이러한 문제를 방지하려면 mod1.py 파일을 다음처럼 변경해야 한다.

```py
# mod1.py 
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
```
* if __name__ == "__main__"을 사용하면 
* C:\>python mod1.py처럼 직접 이 파일을 실행했을 때
* __name__ == "__main__"이 참이 되어 
* if문 다음 문장이 수행된다. 
* 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 
* __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.


## __name__ 변수란?

* 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 만약 C:\>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다. 
* 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

## 클래스나 변수 등을 포함한 모듈

클래스나 변수 등을 포함할 수도 있다.

```py
# mod2.py 
PI = 3.141592
class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def add(a, b): 
    return a+b 
```


## [모듈을 불러오는 또 다른 방법]
### 1. sys.path.append(모듈을 저장한 디렉터리) 사용하기

### 2. PYTHONPATH 환경 변수 사용하기