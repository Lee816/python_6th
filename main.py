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

q = 20
u = "10"    
r = q+u
print(r)
print(type(r))

# 명시적 타입 변환
a = 5
b = 2
value = a / b
print(type(value))
int_value = int(value)
print(type(int_value))