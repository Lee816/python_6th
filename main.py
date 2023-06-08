# 변수 선언
a = 10
b = 3.14
c = "Hello, World!"
d = [1, 2, 3]
e = (4, 5, 6)
f = {7, 8, 9}
g = {"apple":1 ,"banana":2, "orange":3}

# 데이터 타입 출력
print("a: ",type(a))
print("b: ",type(b))
print("c: ",type(c))
print("d: ",type(d))
print("e: ",type(e))
print("f: ",type(f))
print("g: ",type(g))

# 덧셈
a = 4
b = 2
total = a + b
print('totla = a+b = ', total)
# 뺄셈
total = a - b
print('totla = a-b = ', total)
# 곱셈
total = a * b
print('totla = a*b = ', total)
# 나눗셈
total = a / b
print('totla = a/b = ', total)
# 나머지
a = 5
b = 2
print('a%b :', a%b)
# 거듭제곱
print('a**b : ',a**b)
# 몫(양수)
print('a//b : ',a//b)
# 몫(음수)
a = -5
print('a//b : ',a//b)

# 비교연산자
a = 5
b = 2
print('a<b : ',a<b)
print('a<=b : ',a<=b)
print('a==b : ',a==b)
print('a!=b : ',a!=b)

# 논리연산자
a = 5
b = 2
c = 3
d = 200

print('a>b and a>c : ',a>b and a>c)
print('a>b and a<c : ',a>b and a<c)
print('a>b or a>c : ',a>b or a>c)
print('a>b or a<c : ',a>b or a<c)
print('a<b : ',a<b)
print('not(a<b) : ',not(a<b))

# 할당 연산자
a = 10
b = 20
m = 15
y = a+b
print(y)
m += 10
print('m += 10 : ',m)
m **= 2
print('m **= 2 : ',m)
m //= 10
print('m //= 10 : ',m)

# 비트 연산자
a = 10
b = 15
print('bin(2진수) : 0b')
print('hex(16진수) : 0x')
print('hex(a) : ',bin(a))
print('bin(b) : ',hex(b))
print('~a : ',~a)
print('bin(~a) : ',bin(~a))
print('bin(a&b) : ',bin(a&b))
print('bin(a<<2) : ',bin(a<<2))
print('bin(a>>2) : ',bin(a>>2))

# 멤버 in 연산자
st1 = "Welcome to 멋쟁이 사자"
print('st1 : ',st1)
print('to in st1 : ',"to" in st1)
print('to not in st1 : ',"to" not in st1)

st2 = "Welcome top 멋쟁이 사자"
print('st2 : ',st2)
print('to in st2 : ',"to" in st2)
print('to not in st2 : ',"to" not in st2)

st3 = "Welcome to 멋쟁이 사자"
print('st3 : ',st3)
print('subs in st3 : ',"subs" in st3)
print('subs not in st3 : ',"subs" not in st3)
print('wel in st3 : ',"wel" in st3) # 대소문자 구분

# is 연산자
a = 10
b = 10
print('a is b : ',a is b)
print('a is not b : ',a is not b)

b = '10'
print('a is b : ',a is b)
print('a is not b : ',a is not b)

# 암시적 타입 변환
a = 5
b = 2
print(b, type(b))
value = a/b
print(value)
print(type(value))

x = 10
y = 5.5
total = x+y
print(total)
print(type(total))

j = "hello"
k = "likelion"
p = j+k
print(p)
print(type(p))

# q = 20
# u = "10"    
# r = q+u
# print(r)
# print(type(r))

# 명시적 타입 변환
a = 5
b = 2
value = a / b
print(type(value))
int_value = int(value)
print(type(int_value))

q = 20
u = '10'
print(type(u))
r = q + int(u)
print(r,type(r))
r = str(q) + u
print(r,type(r))

n1 = 10.36
vn1 = int(n1)
print(vn1,type(vn1))
vn2 = float(vn1)
print(vn2,type(vn2))
vn3 = complex(vn1)
print(vn3,type(vn3))

n5 = "멋쟁이 사자"
vn5 = list(n5)
print(vn5,type(vn5))
vn5 = tuple(n5)
print(vn5,type(vn5))

n6 = "멋쟁이 사자와 멋쟁이 호랑이"
vn6 = set(n6)
print(vn6,type(vn6))

print('1')
print('2',end='')
print('3')
print('4')

data = [10, 20, -50, 21.3, 'LikeLion']
print(data)

print('Like','Share','Subscribe', sep='')
print('Like','Share','Subscribe', sep='***')
print('Like','Share','Subscribe', sep='*',end='\t')
print('Like','Share','Subscribe', sep='**',end='\n')

m = 40
print("value :", m)

name = "홍길동"
age = 30
print("My name is", name, "and My age is", age)

print('Welcome', end='\t')
print('to',end='\t')
print('LikeLion')

# name = input('문자입력 : ')
# print(name)
# print(input('문자입력 : '))

# name = input('Your Name : ')

mobile = input("Enter Your Mobile Number : ")
mb = int(mobile)
print(mb,type(mb))

price = float(input("Total Price : "))
print(price)

print("He said, \"Hello World\" ")
print('He said, "Hello World" ')
print('It\'s, \"Hello World ')
print("It's, \"Hello World")

# 예제 1 : 간단한 if 문
x = 5
if x > 3:
    print("x는 3보다 크다.")

# if else 문
age = 18
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 중첩된 if else
score = 85
if score >= 90:
    print("A 학점")
else:
    if score >= 80:
        print("B 학점")
    else:
        if score >= 70:
            print("C 학점")
        else:
            print("D 학점")

# 예제 4 : if elif
marks = 75
if marks >= 90:
    print("A 등급")
elif marks >= 80:
    print("B 등급")
elif marks >= 70:
    print("C 등급")
else:
    print("D 등급")

# 입력에 대한 if 문
a = int(input("Enter Number Greater then 2 : "))
if a >= 2:
    print("Correct!! You have Entered :", a)
else:
    print("Wrong!! You have Entered :", a)

day = input("요일을 입력하세요 ex) Mon : ")
if day == "Mon":
    print("오늘은 월요일")
elif day == "Tue":
    print("화요일")
elif day == "Wed":
    print("수요일")
else:
    print("휴일")

# while 루프
i = 0
while i < 10:
    i += 1
    print("i :", i)
    if a == 5:
        break
else: # while 문이 끝나면 실행 break로 탈출할 경우 실행 안됨
    print("else")

# 첫번째 while 루프
a = 1
while a <= 10:
    print(a)
    a += 1
print("코드종료")

a = 2
while a <= 20:
    print(a)
    a += 2
print("코드종료")

a = 1
while a <= 10:
    print(a)
    a += 1
else:
    print("While 조건이 거짓이므로 Else 부분 시행됨")
print("코드종료")

# 무한 루프

# while True:
#     print("멋쟁이 사자")
# print("코드 종료")

i = 0
while True:
    i += 1
    print(i)
    if i == 5:
        break
print("코드 종료")
#--------------------------------------------------
# while 중첩
i = 1
while i <= 3:
    print("Outer Loop",i)
    i += 1
    j = 1
    while j <= 5:
        print('Inner Loop',j)
        j += 1
print('코드 종료')

# range 실습
for i in range(5):
    print(i)

for i in range(2,7):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(-1,-10, -2):
    print(i)

a = range(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(type(a)) # class range
print(type(a[1])) # class int

print("Reverse Rage with Start, Stop, Step")
r = range(5, 0 ,-1)
print(r[0])
print(r[1])
print(r[2])
print(r[3])
print(r[4])

# for in
str = "멋쟁이 사자"
for cha in str:
    print(cha)
else: # for문 종료후 실행 break문으로 탈출시 실행 x
    print("Else")
print("코드종료")

# pass문
a = 5
if a < 6:
    pass # TODO FIXME 개발내용
else:
    print("6보다 큼")

#---------------------------------------------------------------------
# 배열 생성 및 원소 접근
import array

stu_roll = array.array('i',[101, 102, 103, 104, 105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print('for in 사용')
for element in stu_roll:
    print(element)

print('인덱스를 이용한 순회')
n = len(stu_roll)
for i in range(n):
    print(i, '=', stu_roll[i])

print('인덱스를 사용한 while 루프 배열 순회')
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1


from array import *

stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print("배열 삽입 실습")
stu_roll.insert(1,106)
stu_roll.insert(3,107)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print('배열 요소 삭제')
stu_roll.remove(101)
for element in stu_roll:
    print(element)

print('배열 pop() 함수 실습')
stu_roll.pop()
for element in stu_roll:
    print(element)

print('array index 메소드')
print(stu_roll.index(101))

print('extend() 메소드')
arr = array('i',[201,208,209])
stu_roll.extend(arr)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

print('reverse() 메소드')
stu_roll.reverse()
for element in stu_roll:
    print(element)

from array import *

stu_roll = array('i',[101,102,103,104,105,106,107])

print('배열 슬라이싱')
n = len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])

print("1:5")
a = stu_roll[1:5]
for a_value in a:
    print(a_value)

print('0번째 부터 끝까지')
b = stu_roll[0:]
for b_value in b:
    print(b_value)

print('처음부터 5번째 까지')
c = stu_roll[:5]
for c_value in c:
    print(c_value)

print('마지막 요소 4개 출력')
d = stu_roll[-4:]
for d_value in d:
    print(d_value)

print('0부터 6번째 까지 1개 건너뛰어 출력')
e = stu_roll[0:7:2]
for e_value in e:
    print(e_value)

print('마지막 5개 요소 중 [-5-(-3)] = (-2) 오른쪽부터 2개의 요소를 출력')
f = stu_roll[-5:-3]
for f_value in f:
    print(f_value)

str1 = 'LikeLion'
str2 = "LikeLion"
str3 = '''
통해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
'''
str4 = """
통해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
"""

print(str1)
print(str2)
print(str3)
print(str4)

str5 = 'Hello "Like Lion" How are you'
str6 = "Hello 'Like Lion' How are you"

print(str5)
print(str6)

str7 = 'Hello \n How are you?'
str8 = 'Hello \\n How are you?'
str9 = r'Hello \n How are you?'

print(str7)
print(str8)
print(str9)

s = 'hello world'

print(s.upper())
print(s.lower())
print(s.swapcase()) # 대문자를 소문자로 소문자를 대문자로 변환
print(s.title()) # 각 단어 대문자
print(s.isupper()) # 모두 대문자면 True
print(s.islower()) # 모두 소문자면 True
print(s.istitle())
print(s.isdigit()) # 모두 숫자면 True (공백x)
print(s.isalpha())
print(s.lstrip())
print(s.rstrip())
print(s.strip())

s = '     Hello World     '
print(s.replace('world'.title(),'there'))

s = 'Hello,World'
print(s.split(','))

spl_s = s.split(',')
print(spl_s)
print(' '.join(spl_s))

print(s.startswith('Hello'))
print(s.endswith('World'))

print('인자가 없는 함수 정의')

def disp():
    name = '멋쟁이사자'
    print('Welcome to',name)

def add():
    x=10
    y=20
    c = x+y
    print(c)

print('함수 실행')
disp()
disp()
disp()

add()

print('인자가 있는 함수 정의')
def add(y):
    x=10.2334
    print(x+y)
    print(f'Formatted Ouput {x+y:.2f}')

add(20.1597)

def add():
    x = 10
    y = 20
    c = x + y
    return c

sum1 = add()
print(sum1)

def add2():
    x = 10
    y = 20
    return x+y

sum2= add2()
print(sum2)

def add(y):
    x = 10
    return x+y

sum3 = add(20)
print(sum3)

def add(y):
    x = 10
    c = x+y
    d = y-x
    return c,d, 50

sum4, sub1, a = add(20)
print(sum4, sub1, a)

def disp():
    def show():
        print('Show Function')
    print('Disp Function')
    show()

disp()

def disp():
    def show():
        # print('Show Function')
        return 'Show Fuction'
    # print('Disp Function')
    result = show() + ' Disp Function'
    return result

print(disp())

def disp(sh):
    print(type(sh))
    print('Disp Function'+sh())

def show():
    return ' Show Function'

disp(show)

def disp():
    def show():
        return 'Show Function'
    print('Disp Function')
    return show

r_sh = disp()
print(r_sh(), type(r_sh))

def pw(x,y):
    z = x**y
    print(z)

pw(2,5)
# pw(5,2,3) # 에러

def show(name, age=20): # 함수인자의 default 값 설정 가능
    print(f'Name: {name} Age: {age}')

show(name='멋쟁이사자',age=20)
show(age=20,name='멋쟁이사자')
show(name='멋쟁이사자')
