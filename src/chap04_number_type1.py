
def myprint(val):
    print("val : " , val,end=',');
    print('type ', type(val),sep=': ')


#int형
myprint(100)
#float 형
myprint(1.23)
# 정수 / 정수도 파이썬에서는 float형 계산임
myprint(5/5)
# 나눈 값을 정수로 형변환할때
myprint(int(5/2))
# 반올림할때는 5까지는 올림안함
myprint(round(5.1/2))
# 반올림할때는 5까지는 올림안함
myprint(round(7/2))




#진수의표현
# 0b 2  (bin)
# 0o 8  (Oct)
# ox 16 (hex)
print('10진수',15)
print('02진수',0b1111)
print('08진수',0o17)
print('16진수',0xf)


#float형의 오차
a=0.1
b=0.2
#float의 부동소수점에 의해 오차가 나므로 일치하지 않음
print(a+b)
print(a+b == 0.3)
