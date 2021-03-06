print("output 공부하기\n")

# 오늘의 함수
# type()    : 자료형을 확인하는 함수 
# len()     : 문자열의 길이를 구하는 함수
print(type(1))
print()

# 2022. 02. 08
# 따옴표 문자열 만들기
print("'작은 따옴표'를 사용하기")
print('"큰 따옴표"를 사용하기\n')

# 이스케이프 문자를 사용해 문자열 만들기
print("\"이스케이프 문자\"를 사용하기")
print("\'이스케이프 문자\'를 사용하기2")
print()

# 이스케이프 문자 \n과 \t 사용해보기
print("줄바꿈을\n합니다")
print("Tab을\t의미합니다")

print("\\ \\ \\ \\")

# Python은 여러 줄 문자열이라는 기능을 지원합니다
# 큰 따옴표(") 또는 작은 따옴표(')를 세 번 반복한 기호를 사용합니다.
print("""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
""")
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세\

""")

# 문자열 연산자 +
print("문자열"+"연결하기!\n")

# 문자열 연산자 *
print("문자열 반복하기\n" * 3)

# 문자 선택 연산자(인덱싱) []
print("안녕하세요"[0])
print("안녕하세요"[-1])

# 문자열 범위 선택 연산자(슬라이싱) [:]
print("안녕하세요"[1:3])

hello = "하이여"
print(hello[0:2])

# 문자열의 길이 구하기
print(len("안녕하세요"))
print(len(hello))

