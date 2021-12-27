import math,sys

'''

float 즉 부동소수점을 이용하므로 값이 근삿값임 즉, 연산결과가 완벽하게 일치하지 않을 수도 있음
부동 소수점 반올림 오차(Floating Point Rounding error ) 이슈가 날 수 있음

sys에 있는 float_info.epsilon 보다 작은 경우는 같다고 우회 변경해야함
'''

#부동 소수점 오차 이슈 해결하기
a =0.1
b =0.2
print("float 연산시 부동소수점 반올림 오차에 따른 결과")
print(a+b == 0.3)

#1] 앱실론 값을 이용하여 처리하기
print("앱실론 보다 작을 시 같다라고 표현하기")
print('machine epsilon value:',sys.float_info.epsilon)
print(True if math.fabs((a+b)-0.3) <= sys.float_info.epsilon else False)

#2] math isclose함수를 이용하기
print("math 함수를 이용하기")
print(math.isclose((a+b),0.3))
from decimal import Decimal
#3] decimal로 고정 소수점형태로 변환 -> 단, float만큼 큰수는 표현이안됨
print('decimal 이용하기')
print(Decimal('0.1')+Decimal('0.2') ==Decimal('0.3'))


print(chr(ord('A')+1))

k = [1,2,3,3,2,1,1,1,2]
print(k)
print(len(set(k)))