#Python 기본 정리
***
## Caution
- 본 포스팅은 코딩을 처음 배우시는 입문자 분들께는 적절하지 않은 포스팅일 수 있습니다.
- 개발에 필요한 최소한의 내용만 정리해서 포스팅합니다.


<br/>
<br/>

## 문자열 변환
***
- ord() 함수 -> 문자열 값을 ASCII 코드값으로 변환
- chr() 함수 -> 숫자를 ASCII 코드값을 이용해 문자로 변환

```python

code = ord(input('한문자를 입력하세요 >>'))
print('아스키 코드 값:',ord(code))
print('문자열 값 :' ,chr(ord(code)))    
print(" 표현 'A' = ",code , 'A' ==code)

```

## 제어문의 형태
***
- 파이썬엔 switch 문이 없다! if문 만으로 표현
- 삼항 연산자가 따로 존재하진 않으나 if로 표현 가능


> case A. if 문의 표현

    if [조건식] :
        제어 처리 
    elif [조건식] :
        제어 처리
    else :
        제어 처리

반드시 텝으로 위치를 구분해줘야함(파이썬은 텝에 엄격) 제어처리할 것이 없다면, pass 키워드를 넣어주어야함
파이썬은 조건식에 대해 관대함. 빈값([],())에 대해서도 처리 가능(빈 값에 대해 false)

> case B. 삼항연산자

    참인경우 if [조건식] else 거짓인 경우


## 반복문 for
***

자바에서 foreach 문을 생각하면 편함. iterator객체를 이용하는 원리이다.

dir() 함수를 통해 range를 뜯어보면 __iter__라는 함수를 내부적으로 가지고 있음. 이는 다른 배열형 자료형도 동일

```python
print('range 정보')
print('__iter__' in dir(range(5))) #true
print('리스 정보')
print('__iter__' in dir([1,2,3,4,5])) #true
print('문자열 정보')
print('__iter__' in dir("python")) #true
```

내부적으로는 iter.__next__() 라는 이용하여 값을 하나씩 미는 방식임. 
따라서 for문이 끝나도 내부 변수에 마지막 iterator 값이 남아있다.

> 사용방법
    
    #case1
    for [객체] in [iterable 객체]:
        반복목적 코드 수행
    #case2
    for [객체] in [범위] :
        반복목적 코드 수행

```python
for _ in [4,3,4,78,3] :
    print(_,end=' ');

#Result 4 3 4 78 3
```

### case1
- 주로 리스트나 iterable 객체의 요소를 꺼내 이용할 때 사용

### case2
- 특정 구간 반복이나 횟수 반복 목적으로 사용 
- range()함수를 이용하며, 파라미터는 시작값(0),끝값,증감값(1) 3개가 존재함. 
괄호는 디폴트이며, 괄호친 파라미터는 생략가능 


```python
# 파라미터 하나일 때 - 끝값
for i in range(3):
    print(i)
    
#reuslt 0 1 2

# 파라미터 하나일 때 - 시작값, 끝값
for i in range(1,3):
    print(i)
    
#reuslt 1 2

 # 파라미터 하나일 때 - 시작값, 끝값, 증감값
for i in range(0,3,2):
    print(i)

#reuslt 0 2
```

파이썬은 for문이 소멸되어도 i가 사라지지않음. i를 찍어보면 i가 마지막값을 가지고 있음
```python
#...위의 코드
print(i) # 2
```



## 반복문 while
애초에 타 언어 반복문과 다를게 없다
    
    while [조건식] :
        반복 코드

