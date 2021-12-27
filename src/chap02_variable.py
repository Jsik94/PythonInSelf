import sys

# getrefcount 객체(n)번에 대한 참조 갯수를 반환
print(sys.getrefcount(2002))
x = 2002
y = 2002
z = 2002
r = 2001
print(sys.getrefcount(x))

#is 연산자
print(x is y)
print(x is r)