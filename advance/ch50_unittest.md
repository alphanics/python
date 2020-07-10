unittest - 단위테스트
====================
원문 : https://wikidocs.net/16107

## 1. 테스트와 단위테스트
* 테스트 - 소프트웨어 산출물이 요구사항과 부합하는지 여부를 검증
* 단위테스트란 - 개별 코드 단위가 예상대로 작동하는지 확인

## 2. unittest
* 표준라이브러리
* 주요 개념
  * TestCase
    * 테스트 기본 단위
  * Fixture
    * 테스트 전후 환경
  * assertion
    * 성공/실패 확인
    
## 3. unittest 모듈 사용법
* test.py 파일 생성
* unittest.TestCase 상속
* test_xxx함수 작성
* test_run()
* unittest.main() 실행
```py

def custom_function():
    pass


class UnitTests(unittest.TestCase):
    def test_runs(self):
        print("단순 실행")
        custom_function()

    def test_func1(self):
        print("test_func1")

    def test_func2(self):
        print("test_func2")

    def test_func3(self):
        print("test_func3")


# unittest 실행
unittest.main()
```
```
$ python TestUnit.py 
test_func1
.test_func2
.test_func3
.단순 실행
.
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
* setUp() : Fixture. 테스트 **전에** 수행.
* tearDown() : Fixture. 테스트 **후에** 수행.



