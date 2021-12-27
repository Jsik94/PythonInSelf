import copy
import sys

#getrefcount(k) : 현재 파라미터 k를 참조하고 있는 수를 반환

print("Before] 현재 2를 참조하고 있는 수 : " , sys.getrefcount(2)) # 143
a = 2 # 2를 참조하는 변수 추가ㅣ
print("After] 현재 2를 참조하고 있는 수 : " , sys.getrefcount(2)) # 144
#주소를 참조하고 있다는 증거
print('2의 주소 : ' ,id(2)) # id(k) k에 대한 주소 반환
print('a의 주소 : ' ,id(a)) # a의 주소를 반환하고 있다.

a= (10,20,30)
b= a
a = (20,30,40)
print('a의 주소 : ' ,id(a)) # a의 주소를 반환하고 있다.
print('b의 주소 : ' ,id(b)) # b의 주소를 반환하고 있다.
print('a',a) # 10
print('b',b) # 2가 나온다 (복사가 안됨)

#참조의 구조

a = [1,2,3,4]
b = [1,2,3,4]
c = a

# a,c는 주소 동일 b 는 다름
print('a의 주소' , id(a))
print('b의 주소' , id(b))
print('c의 주소' , id(c))

print('a 리스트 값 추가 ')
a.append(10)
# a,c는 주소 동일 b 는 다름
print('a의 주소' , id(a))
print('b의 주소' , id(b))
print('c의 주소' , id(c))
print('a 리스트 변경 ')
a = [2,3,4]
# a,b,c 다다름
print('a의 주소' , id(a))
print('b의 주소' , id(b))
print('c의 주소' , id(c))




#immutable의 예
a = (10,"호롤로",30)
b = (10,"호롤로",30)
print("a - {} & a_id - {}  ".format(a,id(a))) # 튜플은 변할 수 없으므로 값이 같음
print("b - {} & b_id - {}  ".format(b,id(b))) # a,b 두 id 값이 같다

#mutable의 예
a = [1,2,3]
b = [1,2,3]
print("a - {} & a_id - {}  ".format(a,id(a))) # 리스트는 변할 수 있으므로 값이 다름
print("b - {} & b_id - {}  ".format(b,id(b))) # a,b 두 id 값이 다르다.


#깊은 참조와 얕은 참조
listTest = [1,['하이','hello']]
a= listTest
b= copy.copy(listTest)
c= copy.deepcopy(listTest)

print("값 비교 : {}, 주소 비교 : 기준 - {}, 원소1 id - {}, 원소2-1 id -{} , 원소2-2 id - {} ".format(listTest,id(listTest),id(listTest[0]),id(listTest[1][0]),id(listTest[1][1])))
print("값 비교 : {},주소 비교 :   a - {},   a1 id - {},   a2-1 id -{} ,   a2-2 id - {} ".format(a,id(a),id(a[0]),id(a[1][0]),id(a[1][1])))
print("값 비교 : {},주소 비교 :   b - {},   b1 id - {},   b2-1 id -{} ,   b2-2 id - {} ".format(b,id(b),id(b[0]),id(b[1][0]),id(b[1][1])))
print("값 비교 : {},주소 비교 :   c - {},   c1 id - {},   c2-1 id -{} ,   c2-2 id - {} ".format(c,id(c),id(c[0]),id(c[1][0]),id(c[1][1])))

a.append('3')
print('after')
print("값 비교 : {}, 주소 비교 : 기준 - {}, 원소1 id - {}, 원소2-1 id -{} , 원소2-2 id - {} ".format(listTest,id(listTest),id(listTest[0]),id(listTest[1][0]),id(listTest[1][1])))
print("값 비교 : {},주소 비교 :   a - {},   a1 id - {},   a2-1 id -{} ,   a2-2 id - {} ".format(a,id(a),id(a[0]),id(a[1][0]),id(a[1][1])))
print("값 비교 : {},주소 비교 :   b - {},   b1 id - {},   b2-1 id -{} ,   b2-2 id - {} ".format(b,id(b),id(b[0]),id(b[1][0]),id(b[1][1])))
print("값 비교 : {},주소 비교 :   c - {},   c1 id - {},   c2-1 id -{} ,   c2-2 id - {} ".format(c,id(c),id(c[0]),id(c[1][0]),id(c[1][1])))

a[1].append('할로')
print('after')
print("값 비교 : {}, 주소 비교 : 기준 - {}, 원소1 id - {}, 원소2-1 id -{} , 원소2-2 id - {} ".format(listTest,id(listTest),id(listTest[0]),id(listTest[1][0]),id(listTest[1][1])))
print("값 비교 : {},주소 비교 :   a - {},   a1 id - {},   a2-1 id -{} ,   a2-2 id - {} ".format(a,id(a),id(a[0]),id(a[1][0]),id(a[1][1])))
print("값 비교 : {},주소 비교 :   b - {},   b1 id - {},   b2-1 id -{} ,   b2-2 id - {} ".format(b,id(b),id(b[0]),id(b[1][0]),id(b[1][1])))
print("값 비교 : {},주소 비교 :   c - {},   c1 id - {},   c2-1 id -{} ,   c2-2 id - {} ".format(c,id(c),id(c[0]),id(c[1][0]),id(c[1][1])))


a[1][1] = 'hellow'
print('after')
print("값 비교 : {}, 주소 비교 : 기준 - {}, 원소1 id - {}, 원소2-1 id -{} , 원소2-2 id - {} ".format(listTest,id(listTest),id(listTest[0]),id(listTest[1][0]),id(listTest[1][1])))
print("값 비교 : {},주소 비교 :   a - {},   a1 id - {},   a2-1 id -{} ,   a2-2 id - {} ".format(a,id(a),id(a[0]),id(a[1][0]),id(a[1][1])))
print("값 비교 : {},주소 비교 :   b - {},   b1 id - {},   b2-1 id -{} ,   b2-2 id - {} ".format(b,id(b),id(b[0]),id(b[1][0]),id(b[1][1])))
print("값 비교 : {},주소 비교 :   c - {},   c1 id - {},   c2-1 id -{} ,   c2-2 id - {} ".format(c,id(c),id(c[0]),id(c[1][0]),id(c[1][1])))

#Result : 내부주소는 같다.
# print("주소 비교 :   a - {}".format(id(a)))
# print("주소 비교 :   b - {}".format(id(b)))
# print("주소 비교 :   c - {}".format(id(c)))


(4>32) != True

print(4>32 != True)
print(4>(32 != True))
print((4>32) != True)