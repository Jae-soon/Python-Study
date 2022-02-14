print("Python", "Java", "JavaScript", sep = " vs ") # ,로 된 부분에 vs 입력
print("Python", "Java", sep=",", end="?") # ,로 나뉜 부분 ,로 입력 끝부분은 ?
print()

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러로 처리
print()

# 시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items(): # key,value를 튜플로 보내줌
    print(subject.ljust(5), str(score).rjust(4), sep=":")
    # 문자열 구조만 사용 가능(ljust : 왼쪽 정렬 / rjust : 오른쪽 정렬)
    # ljust(N), rjust(N) 의  N : 칸의 수
print()

# 은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill(N) : N이라는 공간을 확보하고, 남은 빈공간은 0으로 채움
