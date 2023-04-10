import random

rand_num = random.randint(1, 100)

# print(rand_num)

try_count = 1

while True:
    answer = int(input("1~100 사이 숫자를 입력하세요.\n"))

    if answer > rand_num:
        print("다운")
    elif answer < rand_num:
        print("업")
    elif answer == rand_num:
        print("정답입니다!! %d번만에 맞췄어요!" %try_count)
        break
    try_count += 1