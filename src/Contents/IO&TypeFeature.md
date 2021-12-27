#Python 기본 정리
***
## Caution
- 본 포스팅은 코딩을 처음 배우시는 입문자 분들께는 적절하지 않은 포스팅일 수 있습니다. 
- 개발에 필요한 최소한의 내용만 정리해서 포스팅합니다.


<br/>
<br/>

## 입력
input()

표준 입력으로 들어오는 데이터를 받는다.엔터(\r\n)가 나올 때 까지 입력받음.
받은 문자열은 모두 str형으로 변수에 저장된다.

input().split()

문자열을 split 토큰으로 잘라 반환한다. 변수가 하나라면 리스트형으로 반환해준다.

map(자료형,input().split());

받은 문자를 형변환해서 받을 수 있다. 

```python

print("일반적으로 입력을 받을 때 ")
a = input() #a에 표준입력(키보드)를 받아 a 에 저장
print(a)

#input message를 사용할 수 있다.
a = input('입력해 주세요 >')
print(a)

#한 변수에 여러 데이터가 입력될 때 default space
# ex) 1 2 3 4 5
a = input().split()
print(a)
# ex) 1@2@3@4@5
a = input().split('@')
print(a)


#여러 변수에 여러 데이터를 입력할 때
# ex)1 3 2
a,b,c = input().split(' ')
print(a,b,c)
print(type(a),type(b),type(c))
#여러 변수에 여러 데이터를 입력할 때 (형변환)
# ex)1 3 2
a,b,c = map(int,input().split(' '))
print(a,b,c)
print(type(a),type(b),type(c))



```



## 출력
print()
sep
end
{} ~.format
%s ~ ,$(s,b)


## 실수형 타입에서 주의할점
다 비슷한데 실수형 연산에서의 오류 (Floating Point Rounding error)
해결법 3가지

```python
import math,sys
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

```

## 연산자 특징
***
다 비슷한데 증감연산자가 없다! (++,--)



## 비교 연산자

## bool type
리스트가 비었을 때도 판별할 수 있다.
빈리스트 : false
값이 있는 리스트 : true

## 논리연산자 
우선순위 not > and > or 
단락평가형 (short-circuit evlation) : 앞에가 거짓이면 뒤를 연산하지 않음

```python

#외부 라이브러리 (모듈) 사용하기
import operator
print(operator.__file__) # 모듈 경로알아내기
print(dir(operator))    # 모듈에 포함된 함수 보기 


```


## 할당연산자

동일

### 진수의 변환

```python
print("기본",125)
print("2진수",bin(125))
print("8진수",oct(125))
print("16진수",hex(125))
```

### 시프트 연산자
```python
# << 시프트시, 빈칸은 0 으로채움
# >> 시프트시. 빈칸은 양수일 땐 0 , 음수일 땐 1
print("기본",125)
print("2진수",bin(125))
print("기본",125<<1)
print("2진수",bin(125<<1))

```


## 조건식
조건식은 모든 식이 올 수 있다.

```python

if not 0 :
    print('0은 False 다')

if not None :
    print('None은 False 다')

if not "" :
    print('""은 False 다')

if not [] :
    print('[]]은 False 다')

```