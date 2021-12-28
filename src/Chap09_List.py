def confirm(obj):
    print('객체 : {} , 타입 : {}'.format(obj,type(obj)))
    if not isinstance(obj,float) and not isinstance(obj,int):
        print("길이 : ", len(obj))



#빈리스트 생성
a = []
b = list()
confirm(a)
confirm(b)

#packing 하나의 변수에 여러개를 담는것
c = ['sample',12,43.22,True]
print('packing exam')
confirm(c)
#unpacking 패킹을 해제하는 과정 변수의 갯수는 반드시 일치해야한다.
c1,c2,c3,c4 = c
print('unpacking exam')
confirm(c1)
confirm(c2)
confirm(c3)
confirm(c4)

b=[1,2,3]
#b.extend(4)#TypeError: 'int' object is not iterable 즉 같은 레벨의 iterable객체가 와야한다. 그래애 확장할 수 있다
# b.extend([True])
# b.extend(('b',12))
b.extend({102,103})
b.extend([True,"리스트"])
b.extend((1,"튜플",3))

b=[[0]*5]

for i in range(1,6):
    b.append([0]*5)
    for j in range(1,6):
        print(i,'-',j,'=',i*j)
        b[i-1][j-1] = i*j

print(b)
b=[[i*j for i in range(1,6)] for j in range(1,6)]

print(b)

