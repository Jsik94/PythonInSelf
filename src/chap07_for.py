# 반복문

# 자바 foreach라고 생각하면 편함
# for [iterator] in 배열계열

'''
    반복 가능한 객체 (iteratable)
    __iter__()


    iterator 만드는 방법
    1. class 로 __iter__ 함수 오버라이딩
    2. 함수로 만들거나 (yield 키워드 사용)

'''

# print('[문자열에서 한 문자씩 꺼내오기]')
# a = [1,2,"요호호호",3,4]
#
# #요소를 반환하는 방법
# for i in a:
#     print("ㅇㅅㅇ")
#
# #반복만을 필요할때
# for _ in a:
#     print("dtd")

# # i와 _에는 마지막 iterator 값이 아직 남아있음 (안지워졌단 소리 )
# print(i,_)

#일반적으로 범위를 표현하고 싶을 때 Range
# 시작(0) 끝 증감(1) - 괄호는 default임
# print('range 정보')
# print('__iter__' in dir(range(5)))
# print('리스 정보')
# print('__iter__' in dir([1,2,3,4,5]))
# print('문자열 정보')
# print('__iter__' in dir("python"))
#
#
# for i in range(0,10):
#     print(i)
#
#
# for i in range(0,10,2):
#     print(i)


print("param1")
for i in range(3):
    print(i)

print("param2")
for i in range(1,3):
    print(i)

print("param3")
for i in range(0,3,2):
    print(i)