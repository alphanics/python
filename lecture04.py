treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)


# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")


test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

add = 0
for i in range(1, 11):
    add = add + i
    print(add)


for i in range(2, 10):      # ①번 for문
    for j in range(1, 10):  # ②번 for문
        print(i*j, end=", ")
    print('')

print('\n')  # 두줄

print('=================')
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

print('\n')  # 두줄

print('=================')
result = [x*y for x in range(2, 10) for y in range(1, 10)]
print(result)
