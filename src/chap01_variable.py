a = 10
print(a,type(a),sep='\n')

a,b,c = '파이썬',"10",20
print('a의 값 :%s - a의 자료형: %s' %(a,type(a)))
print('b의 값 :{} - b의 자료형: {}'.format(b,type(b)))
print('c의 값 :',c,' - c의 자료형: ' ,type(c),sep='')

#패킹 방식

d = 10,'20','파이썬'

print('d의 값 :%s - d의 자료형: %s' %(d,type(d)))


x,y = 10 , 20
print('x :{} y : {}'.format(x,y))
y,x = x,y
print('x :{} y : {}'.format(x,y))

import keyword
print(keyword.kwlist)

del x #메모리에서 지워버림


#-----------------
#변수 선언 방법1] 변수명 = 데이터
a=10
print(a, type(a), sep='\n')

#변수 선언 방법2] 변수명,변수명,~ = 값,값,~ (갯수 맞춰줘야함)
a,b,c='파이썬',"10",20 #a,b,c=('파이썬',"10",20) 괄호안의 값은 튜플이란 객체 ..?
print(a,b,c, sep='$')
print('a의값 : %s a의 자료형 : %s' % (a, type(a)))
print('b의값 : {} b의 자료형 : {}' .format(b, type(b)))
print('c의값 :',c,'c의 자료형:', type(c))

#변수 선언 방법 3] 변수명 = 반복가능한 객체(이터레이터)
d=10,'20',"파이썬"
print('d의값 : %s d의 자료형 : %s' % (d, type(d)))
z=None
print('z의값 : %s z의 자료형 : %s' % (z, type(z)))
x,y = 10,20
print('x =',x,'y =',y)
print('[x와 y의 값 치환]')
y,x = x, y;
print('x =',x,'y =',y)
import keyword
print(keyword.kwlist)
# 변수 삭제
del x,y
print(y)