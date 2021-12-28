#Python 기본 정리
***
## Caution
- 본 포스팅은 코딩을 처음 배우시는 입문자 분들께는 적절하지 않은 포스팅일 수 있습니다.
- 개발에 필요한 최소한의 내용만 정리해서 포스팅합니다.


<br/>
<br/>

## List
***
- 여러개의 자료형을 담을 수 있는 형태
- 순서가 있고 수정이 가능한 특징이 있음


### 빈 만들기 
```python

#빈리스트 생성
def confirm(obj):
    print('객체 : {} , 타입 : {}'.format(obj,type(obj)))
    if not isinstance(obj,float) and not isinstance(obj,int):
        print("길이 : ", len(obj))



a = []
b = list()
confirm(a)
confirm(b)

```


### 리스트 만들기 packing
```python

#빈리스트 생성
def confirm(obj):
    print('객체 : {} , 타입 : {}'.format(obj,type(obj)))
    if not isinstance(obj,float) and not isinstance(obj,int):
        print("길이 : ", len(obj))



a = []
b = list()
confirm(a)
confirm(b)

#packing 하나의 변수에 여러개를 담는것
c = ['sample',12,43.22,True]
print('packing exam')
confirm(c)
```


### 리스트 만들기 unpacking
```python

#빈리스트 생성
def confirm(obj):
    print('객체 : {} , 타입 : {}'.format(obj,type(obj)))
    if not isinstance(obj,float) and not isinstance(obj,int):
        print("길이 : ", len(obj))

c = ['sample',12,43.22,True]
#unpacking 패킹을 해제하는 과정 변수의 갯수는 반드시 일치해야한다.
c1,c2,c3,c4 = c
print('unpacking exam')
confirm(c1)
confirm(c2)
confirm(c3)
confirm(c4)
```
### 값이 있는 리스트 만들기
값이 있는 리스트를 생성하는 방법은 여러가지가 있다.
- 확장 함수를 사용해서 추가하는 법(확장 함수는 바로 다음 목차에서 설명)
- 축약형을 사용하여 표현

> 확장 함수를 이용하는 법

```python
a = []
#0 ~4 까지 들어있는 리스트 만들기
for i in range(0,5):
    a.append(i)
print(a)
```

> 축약형을 이용하여 표현하는 법

```python
#case A
a = list(i for i in range(0,5))
print(a)

#case B - 축약
b = [i for i in range(0,5)]
print(b)
```
case B-축약 경우, 리스트 초기화에 굉장히 많이 쓰이니, 표현법을 잘 알아두자.

#### 리스트도 여러 차원에 대해 표현이 가능할까 ?
그렇다. 파이썬에는 리스트가 배열의 역활을 담당하기 때문에 리스트가 차원을 표현할 수 있다.

```python
# 2차원 빈배열 생성
a = [[]] 

# 2차원 생성
b=[[0]*5]
#case A
for i in range(1,6):
    b.append([0]*5)
    for j in range(1,6):
        print(i,'-',j,'=',i*j)
        b[i-1][j-1] = i*j

print(b)

#case B
b=[[i*j for i in range(1,6)] for j in range(1,6)]

print(b)

```
> Q. 왜 2차원 배열 생성할 때 b=[[0]*5]*5 라고 하지않고 한줄만 선언했나요 ?

좋은 질문이다. 안쪽 '[0]*5'의 의미는 단일 리스트를 5개를 **생성** 하는 것이지만, 바깥쪽은 **행을 복사한다**는 의미가 된다.
즉, 한 행이 바뀌면 참조에 의해 모든 행의 값이 바뀐다는 것. 잘못생성하면 굉장히 치명적일 수 있다. 
따라서 append를 통해 추가하거나, case B와 같이 선언과 동시에 초기화 하자.



### 리스트의 확장
리스트는 수정이 가능하므로, 추가 삭제를 위한 함수가 존재한다.

> 추가
- append() : 파라미터가 object 형으로, 요소에 들어갈 모든 자료형이 들어갈 수 있다.
- extend() : 파라미터는 itertable형태의 제네릭을 취하고 있다. 즉 iterable 객체가 들어간다.

### 두개의 차이는 ?
append의 경우 괄호 안에 있는 자료형을 그대로 넣는다.
```python
b=[1,2,3]
b.append(1)
b.append([True,"리스트"])
b.append((1,"튜플",3))
print(b) # [1, 2, 3, 1, [True, '리스트'], (1, '튜플', 3)]
```
반면, append의 경우 iterable 객체만 가능하며, iterable 객체의 요소를 자동으로 변환해 추가해준다.

```python
b=[1,2,3]

b.extend({102,103})
b.extend([True,"리스트"])
b.extend((1,"튜플",3))

print(b) # [1, 2, 3, 102, 103, True, '리스트', 1, '튜플', 3]
```

> 삭제

삭제에도 두가지가 존재한다.
- remove() : 파라미터로 인덱스가 들어가며 해당 인덱스 값을 삭제한다. 반환 값 X
- pop() : 기본적으로 가장 뒤에 있는 인덱스를 삭제하며, 파라미터 입력시 해당 인덱스 값을 삭제한다. 반환 값 O

### 두개의 차이는?
pop은 stack에서 존재하는 pop의 개념과 같다. 마지막 값을 빼주며, 그값을 반환하는 반면, remove는 삭제만 한다.

