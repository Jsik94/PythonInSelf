#Python 기본 정리
***
## Caution
- 본 포스팅은 코딩을 처음 배우시는 입문자 분들께는 적절하지 않은 포스팅일 수 있습니다.
- 개발에 필요한 최소한의 내용만 정리해서 포스팅합니다.


### 함수
> format 

    def [함수명] (파라미터,...) :
        실행코드
        [return 반환값](선택적) 

- 파이썬 함수는 'def' 예약어를 통해 시작하고, 콜론(:)을 통해 블락을 시전함
- 반드시 텝을 통해 한칸을 띄고 문법을 수행해야한다.(텝또한 구별하기 위한 문법이므로 중요함!)
- 파이썬은 반환값을 지정해주지않으면 자동으로 void 형태임
- 파이썬은 호이스팅을 지원하지 않는다.
- 문서형 주석을 지원한다.(함수 내부에 기술 해야함)



    def temp():
        '''
            함수형 주석
            :return 이런식으로 설명가능
        '''
> 함수의 파라미터
- 파이썬 파라미터에 몇가지 특징을 살펴보자
### 파라미터 키워드
- 파이썬 파라미터에는 키워드 파라미터라는 개념이있다. 일반적으로는 파라미터는 위치 순서를 따라가지만, 명시적으로 지정하므로써 위치를 바꿀 수 있음
```python

def fixedParams(a,b,c,d):
    return print(a,b,c,d)

fixedParams(1,2,3,4)            #result : 1 2 3 4
fixedParams(d=1,c=2,a=3,b=4)    #result : 3 4 2 1

#키워드 파라미터 ex) print end 키워드
print('하이',end='')

```
### 가변 파라미터
- args,... 처럼 가변 인수를 사용할 수 있다. ※단, 가변인수는 고정인수보다 뒤에 와야함
- 변수명 앞에 * 를 붙여서, 가변 파라미터로 만들 수 있다. 가변인수는 최소 0개의 인자를 받는다는 의미이다.
- 가변인수는 고정인수보다 **무조건 뒤에와야하며**, 여러개를 받을 수 있다.
- 가변인수는 튜플 형태로 받게된다.
- 리스트나, 튜플과같이 배열형 자료형인 경우 변수에 *을 붙여 unpacking할 수 있다.
```python
def unfixedParams1(*b):
    print(b)

# 여러개의 인자를 받았을 때 튜플로 인식한다.
unfixedParams1(1,2,3)       # (1,2,3,)
    
# ,로 자료형을 구별하므로 리스트가 들어온다면, 튜플에 단 하나의 리스트가 들어온것으로 해석
unfixedParams1([1,2,3])     # ([1,2,3],)

# 변수에 *붙이면 unpacking 상태가 된다.
unfixedParams1(*[1,2,3])    # (1,2,3,)

```

### 가변 키워드 파라미터
- 변수명 앞에 ** 를 붙여서, 키워드 가변 파라미터를 만들 수 있다.
- 이때, 가변파라미터는 dic 형태를 가지고 있으며, 키워드 형태로 한다.
```python

#키워드  가변 파라미터는 항상 뒤에 와야한다
#키워드 가변 파라미터는 반드시 ** 두개로 표현됨
#반드시 가변파라미터 보다 뒤에 온다
#키워드 가변 파라미터는 dic 형태로 존재함

def unfixed_keyword_params(**keywords):
    if keywords :
        for key,value in keywords.items():
            print(key,' - ' , value, end=' ')
        print()
    else :
        print("인수가 없어용")

unfixed_keyword_params() # 인수가 없어용
#키워드 가변 파라미터 사용
unfixed_keyword_params(username='jsik') # username  -  jsik
#가변이므로 여러개를 사용할 수 있음
unfixed_keyword_params(username='제이식',age=20) # username  -  제이식 age  -  20
#dic형태로도 사용이 가능하다.
unfixed_keyword_params(**{'username':'jsik','age':21}) # username  -  jsik age  -  21 

```

### 디폴트 파라미터
- 사용자가 파라미터값을 전달하지않아도 기본값이 파라미터에 존재하는경우
- C계열에서 볼 수 있는 파라미터 형식과 같다.
- 파라미터를 생략해도 자동으로 기본값이 들어간다.
- 디폴트 파라미터는 오른쪽부터 채워나가야한다.

#### 디폴트 파라미터가 앞에 온 경우 ->Error
### 왜 에러가 나는가 ? 
디폴트 파라미터는 파라미터를 생략할 수 있는 특성 때문에, 왼쪽부터 정의하게 된다면, 파라미터의 위치가 뒤틀릴 수 있다.
따라서 영향력이 없는 맨 뒤부터 넣는다.

```python
# def default_param1(a=20,b):
#     return a+b

def default_param2(a,b=20):
    print((a+b))


# 전달하지 않으면 생략가능
default_param2(10) # 10+20 = 30
# 전달하면, 기본값이 아닌 입력값으로 변수 설정
default_param2(10,30) # 10+30 = 40

```
※ 단, 가변인수와 섞어쓰는 경우 키워드 파라미터 처럼 명시적으로 사용하자!
```python

#가변 파라미터와 섞는 경우
def param_final1(name,age,*info,recommand='없음',**args):
    result ="사용자 이름 : {} 나이 : {} ".format(name,age)
    if info :
        result+= '정보 : '
        for i in info:
            result += i + ' '

    result += "추천인 : " + recommand

    if args :
        result += '\n 비고 : '
        for key ,value in args.items():
            result += " {} - {} ".format(key,value)

    print(result)

param_final1('Jsik',20)
param_final1('Jsik',20,recommand='시끄당')
param_final1('Jsik',20,'배고픈 상태가 강함','헬스장 일찍닫는거 싫음',like='귀여운거미침',**{'status':'좋음'})
```


##정리 (Order)
***
고정 파라미터 > 가변 파라미터 >  디폴트 파라미터 >키워드 가변 파라미터 



## 람다(lamda)
- 함수형 프로그래밍에서 자주볼 수 있는 표현식으로, 함수의 축약형이라고 보면된다.
- 람다 함수는 코드가 간결하며, 직관적인 코드다.
- 익명함수의 목적을 그대로 상속받는다.
- y=f(x)를 만족하는 완전함수이어야한다. (반드시 반환값이 있어야 함을 존재함)
###사용법

람다식을 통해 표현하고,직접 호출시에는 소괄호를 통해 파라미터를 전달함.


    (lamda arg1,arg2,args... : result )(param1,param2,params...)

```python
# function 타입의 객체다 
print((lambda  a: a-10)(11)) #1
lam = lambda a: a+10
print("lam(10) : " ,lam(10), type(lam)) # lam(10) :  20 <class 'function'>

```

직접호출 하지 않는 경우. ex) 리스트 초기화




