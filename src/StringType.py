# 파이썬에서 문자열 만드는 여러방법

#한 줄은  아래와 같이 처리
print('문자열 만들기 1')
print('HI')
print('문자열 만들기 2')
print("HI")

##여러 줄은 아래와 같이 처리
print('문자열 만들기 3')
print('''
    배고프다
            졸리다
                        포스팅하고싶다

''')
print('문자열 만들기 4')
print("""Hello
HI
Mexican""")

import encodings
## 인코딩 default = UTF-8
sten = "hello 안녕하세요 !"
print('Default Str:',sten)
print('Default Str len:',len(sten))
print('[encode() 함수로 문자열 바이트 문자열로 변환]')
print('Encoded Str:',sten.encode(encoding='utf-8'))
print('Encoded Str len:',len(sten.encode(encoding='utf-8')))
print('Decoded Str:',sten.encode().decode())


a = {1:20,3:30,4:40}
b = {1:20,3:30,4:40}
print(id(a))
print(id(b))
b = a
print(id(a))
print(id(b))
print(a)
print(b)
a.update({5:50})
print(id(a))
print(id(b))
print(a)
print(b)
