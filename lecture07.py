class Family:
    lastname = "김씨"


# 클래스 변수는 위 예와 같이 클래스이름.클래스 변수로 사용할 수 있다.
print(Family.lastname)

# 객체를 통해서도 클래스 변수를 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname)  # 김씨
print(b.lastname)  # 김씨

# 클래스의 변수 변경
Family.lastname = "박씨"

# 객체의 변수도 변경된다
print(a.lastname)  # 박씨
print(b.lastname)  # 박씨

# id값을 확인하자
print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
