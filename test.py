# str_list = ["오즈", "코딩", "스쿨", "3"]
#
# int_list = [1, 2 ,3]
#
# print(str_list[3])
# print(int_list[2])
#
# int(숫자) or str(문자)

# ------------------------

# a_int = 10
# b_int = 20
#
# a_str = "10"
# b_str = "20"
#
# print(a_int+b_int)
# print(a_str+b_str)

# float -> 실수형(소숫점이 붙은 숫자)

# print(5)
# print(float(5))
#
# str -> 문자
# int -> 숫자(정수)
# float -> 숫자(실수)
#
# print(float(5))

# a = [1, 2, 3, 4, 5, 6, 7]
#
# b = a[4]
#
# print(b)
#
# a = [1, 2, [3, 4]]
# print ( a[2][0] )

# a = [1, 2, 3, 4, 5 ]
# print(a[2:-1])
#
# a[2] = 3
# a[-1] = 5

# Matryoshka = [1, [1, [1, [1, [1, [1]]]]]]
#
# print(Matryoshka[-1][-1][-1])

# word = "PyThon"
# word = word[:2] + 't' + word[3:]
# word = "Py" + 't' + "hon"
# print(word)

# 응출 -> 승우, 주희 삭제
# name = ["세은", "응출", "수호", "유중", "주희"]
# name[1] = "승우"
# del name[4]
# print(name)

# 여기서 부터는 조건문
# 날씨 = input()
# if 날씨 == '비':
#   print("우산을 챙기자.")
# if 날씨 == '맑음':
#   print("산책을 가자.")

# a = 9 // 2 # 몫
# print(a)
#
# b = 9 % 2 # 9 나누기 2 나머지가 1 ( (4*2)+1 )
# print(b)

# a = input("생각나는 과일을 입력하세요 :").split(',')
# if "사과" not in a:
#   print("사과는 입력하지 않았습니다.")
# if "배" not in a:
#   print("배는 입력하지 않았습니다.")

# a = 4
# if a > 3:
#   print(a, end='')
#   print("는 3보다 크다.")
# print("코드를 종료합니다.")

# a = int(input())
#
# if a > 15:
#     print(a , end='')
#     print("은 15보다 크다.")
# print("그리고")
#
# if a < 50:
#     print("{0}은 50보다 작다.".format(a))
# print("그리고")
#
# if a > 20:
#     print(a, "은 20보다 크다.", sep='')

# a = int(input())
# if a % 2 == 0:
#   print(a, "은 짝수입니다.")
# else:
#   print(a, "은 홀수입니다.")

# money = 0
# store = 600
# icecream = ["Apple", "Grape", "Watermelon"]
# if money != 0:
#     if money >= 1500:
#         if store < 500:
#             if "watermelon" in icecream:
#                 print("수박맛 아이스크림을 산다.")
#             else:
#                 print("다른 아이스크림을 산다.")
#         else:
#             print("다른 편의점을 찾아본다.")
#     else:
#         print("돈을 찾아본다.")
# else:
#     print("그냥 집에서 쉰다.")

# score = int(input())
#
# if score >= 90:
#     print("금상")
# else:
#     if score >= 75:
#         print("은상")
#     else:
#         if score >= 60:
#             print("동상")
#         else:
#             print("수상하지 못함")


# if , else , elif
#
# if = 조건문 ( 어떤 값에 조건을 걸고 싶을때 !!)
#
# else = if 조건문에 부합하지 않을경우 ( False ) 그 경우 else 조건문을 실행
#
# elif = if 문에 추가적으로 조건을 걸고 싶을때 ( 한번더 조건문을 거치게 됨 )
#
# else vs elif
#
# 가장 큰 차이는
# else : 무조건 if 문 마지막에 (중간에 XXXX)
# elif : 무조건 if 문 중간에
#
# if a > 5:
#   print(1)
# elif a < 5:
#   print(2)
# else :
#   print(3)
# elif (XX)
#
# ★ 가장 기본적인 IF 문의 사용법
# IF 는 TRUE or FALSE 확인하는 조건문
#
# if ~
#   elif
#   elif
#   elif
#   ...
# else 실행

# 96 ~ 100 A+
# 95 ~ 90 A
#
# score = int(input())
#
# if score >= 96 :
#   print("A+")
# elif score = 90 :
#   print("A")
# elif score

# a = 1
# print(a)
# a -= 1
# print(a)q
# a = a + 1
# print(a)


# for 조건문
# fruit = ["Apple", "Banana", "Grape", "Melon"]
# print("I want a", fruit[0])
# print("I want a", fruit[1])
# print("I want a", fruit[2])
# print("I want a", fruit[3])
# for name in fruit:
#   print("I want a", name)

# for i in range(1, 1001):
#   print(i)
#
#   if i == 10 :
#     break

# for i in range(3):
#   for j in range(5):
#     print(i,j)

# 조건문 : if, elif, else
#   특정한 조건을 걸고 True or Flase 판단해서 코드를 실행시키고 싶을 때
#
# 반복문 : for i in ~~ :
#   원하는 양 만큼 코드를 반복 실행시키고 싶을때
#
#   while : 별다른 조치가 없으면 끝까지 코드를 실행합니다.
#
# if, elif, else : 조건문
# for, while : 반복문

# def one_to_ten():
#   for i in range(1, 1001):
#     print(i)
#
#     if i == 10 :
#       break
#
# def ten_to_one():
#   for i in reversed(range(1, 11)):
#     print(i)
#
# a = int(input())
# if a < 10 :
#   print(one_to_ten())
# else :
#   print(ten_to_one())

# def message():
#   print("가")
#   print("나")
# message()
# print("다")
# message()

# ★함수: 이름은 자유롭게 정할 수 있으나, 누가 봐도 대충 뭐하는 함수인지는 알아야 한다.

# def login_service(id):
#   print(f"로그인에 성공 하셨습니다. {id}님 환영합니다.")
#
# login_service("웅비")
# login_service("지영")
# login_service("동길")

# 결론 ->
# def : 함수
# 함수() 값을 넣는게 매개변수

# a = 123456
#
# print("오류가 발생 했습니다. 오류 코드는 {a}입니다.")
# print(f"오류가 발생 했습니다. 오류 코드는 {a}입니다.")

# 함수 : 정의한 코드를 언제든 어디서든 불러서 사용이 가능하다(호출)

# print(f"피자가 나왔습니다.{i}님 맛있게 드세요.")

# def odd_number(num):
#   if num % 2 == 0:
#     print(f'{num}는 짝수 입니다.')
#   else :
#     print(f'{num}는 홀수 입니다.')
#
# odd_number(7)
# odd_number(16)
# odd_number(4912391848)
# odd_number(484844418581)
# odd_number(4912391848412048)

# def check_len(s):
#
#   if len(s) <= 0:
#     print('이름은 1글자 이상 입력해야합니다.')
#   else:
#     print('정상 이름 길이 입니다.')
#
# Name1 = ''
# Name2 = '이민주'
# check_len(Name1)

# class Person:
#   def hello(self):
#     a = 5
#     print(f"학생입니다.{a}")
#
#   def no(self):
#     a = 150
#     print(f"아닙니다.{a}")
#
# person1 = Person()
# person1.hello()
# person1.no()

# [예외처리]
# 1. 강행해요 ? 덜 깐깐하다 ex) 서버에서 오류가 일어나거나 문제가 발생해도 무조건 실행을 시켜야하는 코드가 있으면 사용

# try :
#     number = int(input())
#     result = 10 / number
#     print(result)
# except:
#     print("오류번호는 ~~~ 입니다.")

# 2. if (조건문) : 깐깐하다 = 조건에 부합하지 않으면 그냥 안해버리거나 오류를 일으킨다
#
# number = int(input())
# if number > 0:
#   result = 10 / number
#   print(result)
# else:
#   print("숫자를 입력해 주세요")
#
# 결론 : 조건을 걸어야 할때는 10에 9은 if(조건문) 조건을 빡세게 걸어서 실행
# 다만, 강행해야 하는 코드 (반드시 실행 되어야 하는 코드는) except(예외처리)를 사용해야 할 수도 있다.

# if, else (elif)
# try, except
# 이렇게가 세트 메뉴


# class Cal :
#   def setdata(self, first, second):
#     self.first = first
#     self.second = second
#
#   def add(self):
#     result = self.first + self.second
#     return result
#
# method = Cal()
# method.setdata(4,12)
# print(method.add())

# 모듈화 (하나의 덩어리로 만들어서 다시 이용할때 쓰거나, 가독성이 좋아진다)
# 만약에 작성한 코드에서 오류가 발생 !! class 나 def 정리하지 않으면 엄청나게 찾기 힘들고 보수도 쉽지 않다.

# class Human:
#   pass
#
# person = Human()
# person.name = "민규"
# person.age = 13
# person.gender = "남자"
#
# class Human:
#   def __init__(self, name, age, gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
#
# person = Human("민규", 13, "남자")

# a = [1, 2 ,3 ,4 ,5 , "호랑이", "사자", [1,2,3]] # 리스트
# b = (1, 2 ,3 ,4 ,5 , "호랑이", "사자", [1,2,3]) # 튜플
# c = {"붕어빵": 1500, "슈붕": 2000, "피붕": 3000} # 딕셔너리

# 그러면 딕셔너리가 뭔데? 어떤 리스트가 있는데 거기에 값을 넣고 싶을때 쓴다
# key : value
#
# a[2] = 300
# print(a)
# 리스트 = [ ] (대괄호를 사용)
# 튜플 = ( ) (일반 괄호를 사용)
# 딕셔너리 = { }(중괄호를 사용)


# 여기서 또 큰차이 !! 리스트는 값 변경, 추가, 삭제 자유로움
# 튜플은 안됨!!

# a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# b = a[::-1]
# print(b)

# tuple_len = (1, 2, 3, 4, 5)
#
# for i in range(len(tuple_len)):
#   print(tuple_len[i])

# A = int(input())
# B = int(input())
# print( A + B )
#
# map -> 묶어준다

# A = int(input()) # int 를 붙여서 숫자를 입력받음
# B = input() # 딱히 붙힌거 없으면 아무거나 다 입력 받음 ( 문자, 정수, 실수~~ )

# 문제 : 입력받은 글자에 뒤에 ??! 가 붙었으면 좋겠어!!
# f-string : 에프스트링-> 문자 안에 변수를 출력할때 아주아주 유용하다.
# print("") : 일반 프린트문
# print(f"") : f-string 적용된 프린트문

# A = input()
# print(f"{A}??!")

def test() :
  pass

print("테스트 할래요")
문자 안에 변수를 출력할때 아주아주 유용합니다.