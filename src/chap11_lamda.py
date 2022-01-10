#람다
# function 타입의 객체다
print((lambda  a: a-10))
lam = lambda a: a+10
print("lam(10) : " ,lam(10), type(lam))



#리스트에서 요소를 람다로 표현하는 방법

print(list(map(lambda i: i+10,[i for i in range(0,10)])))

list_ =[lambda a,b : a+b, lambda a,b :a-b,lambda a,b:a*b,lambda a,b : a/b]
print(list_[0](10,20))
print(list_[1](10,20))
print(list_[2](10,20))
print(list_[3](10,20))

#딕셔너리에서 요소를 람다로 표현하는 방법

dic_= {"+": lambda a ,b : a+b,"/": lambda a ,b : a/b,"*": lambda a ,b : a*b,"-": lambda a ,b : a-b}
print(dic_["+"](10,20))
print(dic_["-"](10,20))
print(dic_["*"](10,20))
print(dic_["/"](10,20))


mylist = list(map(lambda a : a*2,[i for i in range(0,5)]))
print(mylist)

#람다 역시 함수이기 때문에 함수의 파라미터 속성을 그대로 상속받는다
lam = lambda a,*args : args*a
print(lam(3,1,2,3))
print(lam(3,*[1,2,3]))