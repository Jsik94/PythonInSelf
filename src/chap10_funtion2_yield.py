#Yeild 에 관하여

#yeild는 함수에서 쓰는 키워드이며 제네레이터임
#왜쓰는지 그리고 제네레이터가 무엇을 하는지알기 위해 일반적인 함수를 보자



# 해당 함수가 리스트를 반환하는 로직은 다음과 같다.
# for문을 number만큼 실행하여 result라는 객체에 리스트로 데이터를 담아 반환한다.
# 이 내용을 풀어쓴다면, for문 만큼 반복해서 저장한 다음 출력을 해야한다.
# 즉, number가 몇십억 된다면, 몇십억개의 메모리공간을 차지해야한다.

def list_number(number):
    result = []
    for i in range(1,number+1):
        result.append(i)
    return result

print(list_number(10))

# 이러한 반복을 줄여 효율성을 높히고자 고안된 것이 yield 키워드 이다.
# yield 키워드는 제네레이터 타입으로 이터레이터를 생성해준다.
# yield 키워드 라인을 실행한 뒤 함수를 호출한쪽으로 프로그램의 제어를 양보(yield)한다.
# 즉, yield 에서 멈춰있는 상태.

# 제네레이터가 뭐냐 ?
# 메모리를 효율적으로 사용하면서 반복을 수행하도록 돕는 객체
# iterator를 생성해 주는 함수를 의미한다.



'''
generator(제네레이터)
-함수에서 값을 반환할때 return 대신 사용하는 키워드
-yield키워드를 사용하면 그 함수는 제네레이터로 이터레이터를 생성해준다.
-yield는 반환 한다는 표현이 아님 즉, 함수가 끝나지않음
- yield 라인을 실행하고 함수를 호출한쪽으로 프로그램의 제어를 양보한다
- __iter__ 와 __next__를 내부적으로 가지고있음
- __iter__ 실행시 내부적으로 __next__가 실행되는데, 실행될때마다 yield를 통해 값을 발생시키는 로직임

https://dojang.io/mod/page/view.php?id=2412
개인적실험
-이터레이터 생성자라고 보면 편한듯 ?
-yield로 호출하면, 해당 값을 스택처럼 쌓아서 iterator를 만드는 개념임
-return과 섞어쓰니 return을 씹는다 ..?
-yield를 사용하면 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
'''

def yield_test():
    for i in range(5):
        yield i
        print(i,'번째 호출!')
    return

print(type(yield_test())) #<class 'generator'>
t = yield_test()
print(t.__iter__())

print("<-->")
for k in yield_test():
    print(k)

print(dir(yield_test()))
print(dir(list))
print(dir(set))
print(dir(tuple))
# 0
# 0 번째 호출!
# 1
# 1 번째 호출!
# 2
# 2 번째 호출!
# 3
# 3 번째 호출!
# 4
# 4 번째 호출!