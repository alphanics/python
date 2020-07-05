# 주석
# 설명문
# #으로 시작하면 주석이 된다.(한문장)
'''
작은따온표를 3개를 연속으로 앞뒤로 하면 주석이 된다
'''
# 범위 선택후 ctrl+/ 하면 주석이 된다


# 숫자형
print("숫자형 ==========================")
print(1)
print(1-10)
print(3.141592)
print(2*7)
print(2*(7+2))
print(type(123))
print("\n")


# 문자열
print("문자열 ==========================")
print('aaa')
print('aaa'*5)
print('가나다,'*5)
print('C:\some\name')
print('C:\\some\\name')
print(r'C:\some\name')  # note the r before the quote
print('"Isn\'t," they said.')
print(3 * 'A' + 'ium')
print(type('abc'))
print("\n")


# 리스트
print("리스트 ==========================")
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
print(type(squares))
print("\n")


# 튜풀
print("튜풀 ==========================")
t1 = (1, 2, 'a', 'b')
print(t1[0:3])
print(type(t1))
print("\n")


# 딕셔너리
print("딕셔너리 ==========================")
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic)
a = {1: 'hi'}
print(a)
print(type(dic))
print("\n")


# 집합
print("집합 ==========================")
s1 = set([1, 2, 3])
s1
# 결과 : {1, 2, 3}
s2 = set("Hello")
s2
print(type(s2))
# 결과 : {'e', 'H', 'l', 'o'}
# ※ 비어 있는 집합 자료형은 s = set()로 만들수 있다.
print("\n")


# 참/거짓(boolean)
print("참/거짓(boolean) ==========================")
print(5 > 10)
print(True)
print(False)
print(type(True))
print("\n")
