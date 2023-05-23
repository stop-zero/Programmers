def sort_scores(students):
    # 정렬 우선순위를 기준으로 학생들을 정렬하는 함수
    def sort_key(student):
        return (-student['국어'], student['영어'], -student['수학'], student['이름'])

    # 학생들을 정렬하여 반환
    sorted_students = sorted(students, key=sort_key)
    return sorted_students

# 학생의 수 입력
N = int(input())

# 학생들의 정보를 담을 리스트
students = []

# 학생 정보 입력 받기
for _ in range(N):
    name, korean, english, math = input().split()
    student = {
        '이름': name,
        '국어': int(korean),
        '영어': int(english),
        '수학': int(math)
    }
    students.append(student)

# 성적 정렬
sorted_students = sort_scores(students)

# 정렬된 학생들 출력
for student in sorted_students:
    print(student['이름'])
