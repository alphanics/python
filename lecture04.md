# 제어 흐음
* if
* while
* for

## 1. if
* if문은 왜 필요할까?
* if문의 기본 구조
* 들여쓰기
* 조건문이란 무엇인가?
    * 비교연산자
    * and, or, not
    * x in s, x not in s
* 다양한 조건을 판단하는 elif
* 조건부 표현식

### 1.1 if문은 왜 필요할까?

```
"돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다."
```

프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰는 것

```py
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
# 택시를 타고 가라
```
### 1.2 if문의 기본 구조

```py
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
```    
### 1.3 들여쓰기

if문을 만들 때는 **if 조건문:** 바로 아래 문장부터 if문에 속하는 모든 문장에 **들여쓰기(indentation)** 를 해주어야 한다. 
```py
# 들여쓰기 에러
if 조건문:
    수행할 문장1
수행할 문장2
    수행할 문장3

# 들여쓰기 에러
if 조건문:
    수행할 문장1
    수행할 문장2
        수행할 문장3
```    
* [조건문 다음에 **콜론(:)** 을 잊지 말자!]

### 1.4 조건문이란 무엇인가?
* if 조건문에서 "조건문"이란 **참과 거짓** 을 **판단** 하는 **문장** 을 말한다.

```py
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
# 택시를 타고가라

pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")
# 택시를 타고가라
```
if, elif, else를 모두 사용할 때 기본 구조는 다음과 같다.
```py
if <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
   ... 
```   

### 1.5 조건부 표현식
- 파이썬의 조건부 표현식(conditional expression)을 사용하면 위 코드를 다음과 같이 간단히 표현할 수 있다.
```py
if score >= 60:
    message = "success"
else:
    message = "failure"
```    
조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.
```py
message = "success" if score >= 60 else "failure"
# 변수 = [참값] if <조건문> else [거짓값]
```

---

## 2. while

* while문의 기본 구조
* while문 만들기
* while문 강제로 빠져나가기
* while문의 맨 처음으로 돌아가기
* 무한 루프

### 2.1 while문의 기본 구조
```py
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```
열 번 찍어 안 넘어가는 나무 없다"는 속담을 파이썬 프로그램으로 만든다면
```py
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
```

### 2.2 while문 만들기
* number 변수에 0을 먼저 대입한다. 
* 이렇게 변수를 먼저 설정해 놓지 않으면 다음에 나올 while문의 조건문인 number != 4에서 변수가 존재하지 않는다는 오류가 발생한다.
```py
number = 0
while number != 4:
    print(prompt)
    number = int(input())
```

### 2.3 while문 강제로 빠져나가기
loop를 강제로 멈추게 하는 것이 바로 break문이다.
break문은 **가장 가까운 loop** 를 탈출한다.

### 2.4 while문의 맨 처음으로 돌아가기
continue를 사용
```py
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a) # tab 조심해야 함
```

### 2.5 무한 루프
```py
while True: 
    수행할 문장1 
    수행할 문장2
    ...
```
while문의 조건문이 True이므로 항상 참이 된다. 따라서 while문 안에 있는 문장들은 무한하게 수행될 것이다.
```py
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
```

## 3. for
* for문의 기본 구조
* 예제를 통해 for문 이해하기
    * 1. 전형적인 for문
    * 2. 다양한 for문의 사용
    * 3. for문의 응용
* for문과 continue
* for문과 함께 자주 사용하는 range 함수
    * range 함수의 예시 살펴보기
    * for와 range를 이용한 구구단
* 리스트 내포 사용하기

---

### 3.1 for문의 기본 구조
for문의 기본 구조는 다음과 같다.
```py
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
```    

### 3.2  예제를 통해 for문 이해하기
* 전형적인 for문
```py
test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)
```
* 다양한 for문의 사용
```py
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
```
* for문의 응용
```py
marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)
```        
### 3.3 for문과 continue
- while문에서 살펴본 continue문을 for문에서도 사용할 수 있다. 
- 즉 for문 안의 문장을 수행하는 도중에 continue문을 만나면 for문의 처음으로 돌아가게 된다.
```py
marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue 
    print("%d번 학생 축하합니다. 합격입니다. " % number)
```    

### 3.4 for문과 함께 자주 사용하는 range 함수
- for문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다. 

* range 함수의 예시 살펴보기
```py
add = 0 
for i in range(1, 11): 
    add = add + i 
    print(add)
```

* for와 range를 이용한 구구단
```py
for i in range(2, 10):      # ①번 for문
    for j in range(1, 10):  # ②번 for문
        print(i*j, end=", ")
    print('')
```

### 3.5 리스트 내부에서 for 사용하기
```py
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
# list comprehension
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)
```
구구단
```py
result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
```
