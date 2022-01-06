#함수

def helloPython():
    print('hello')


# helloPython()
# print(helloPython())# 반환 값 자체는 없으므로 None이 나옴



def msg(sten):
    '''
    함수 doc 주석, 내부에 작성해야한다
    __doc__ 내장 함수를 통해 출력가능
        :param sten: 출력할 문자열
        :return null
    '''
    print(sten)

# msg('안녕하세요')
# print(msg.__doc__)

def add(a,b):
    """
    두 수를 더하는 함수
    :param a: int
    :param b: int
    :return: a+b 값
    """
    return a+b
# print(add(10,20))
# print(msg.__doc__)


def getAvg():
    a,b,c = map(int,input('국영수 점수를 입력하세요 >').split(' '))
    avg = (int)(a+b+c)/3
    return 'A' if avg >= 90 else  'B' if avg >=80 else  'C' if avg >=70 else  'D' if avg >=60 else 'F'

    # if avg >= 90 :
    #     return 'A'
    # elif avg >=80:
    #     return 'B'
    # elif avg >=70:
    #     return 'C'
    # elif avg >=60:
    #     return 'D'
    # else:
    #     return 'F'

# print(getAvg())


def getAvg(a,b,c):
    avg = (int)(a+b+c)/3
    return 'A' if avg >= 90 else  'B' if avg >=80 else  'C' if avg >=70 else  'D' if avg >=60 else 'F'

# a,b,c = map(int,input('국영수 점수를 입력하세요 >').split(' '))
# print(getAvg(a,b,c))



score = [[90,78,89],
         [66,78,55],
         [80,55,90],
         [100,99,100],
         [40,35,20]]

for human in score:
    print(getAvg(human[0],human[1],human[2]))

def getMax(cnt):
    data = []
    for _ in range(cnt):
        data.append(int(input('숫자를 입력하세요')))
    return max(data)
# print(getMax(3))


def fixedParams(a,b,c,d):
    return print(a,b,c,d)

fixedParams(1,2,3,4)        #1 2 3 4
fixedParams(d=1,c=2,a=3,b=4)#3 4 2 1

def unfixedParams(a,*b):
    '''

    :param a: 정수가 들어올것임
    :param b: 리스트가 들어올 것임
    :return: a* b요소
    '''
    #a이하 파라미터 값을 튜플로 인식하게 됨

    print(b,type(b))
    for i in b:
        for j in i:
            print(j*a,end='')
    print()
unfixedParams(2,[1,2,3,4,5])


def unfixedParams1(*b):
    print(b)

# 변수에 *붙이면 unpacking 상태가 된다.
unfixedParams1([1,2,3])     # (1,2,3,)
unfixedParams1(*[1,2,3])    # ([1,2,3],)


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

unfixed_keyword_params()
unfixed_keyword_params(username='jsik')
unfixed_keyword_params(username='제이식',age=20)
unfixed_keyword_params(**{'username':'jsik','age':21})




#키워드 가변 파라미터는 반드시 가변파라미터 보다 뒤에 온다
def person_like(name,age,*likenum,**gender):
    result ="이름 : {} 나이 : {}".format(name,age)
    if likenum :
        result += " 좋아하는 숫자: "
        for _ in likenum:
            result += str(_)+" "

    if gender :
        for key,value in gender.items():
            result += " 성별 : " +value

    print(result)

person_like('제이식',27)
person_like(*['제이식',27])
#키워드를 전달 할수가 없다.
person_like(*[278,'jsik'])
# dictionary로 unpacking시, 키값으로 파라미터가 셋팅이됨
person_like(*{'name':'제이식','age':27})
# value값을 넣고 싶다면 double unpacking하면 된다.
person_like(**{'name':'제이식','age':27})
# key 값이 의미없이 버려지는 것이 아니라, 파라미터를 매핑하는 키워드 파라미터로 동작홤
person_like(**{'age':27,'name':'제이식'})
# person_like(**{'age':27,'nam':'제이식'}) #error 키워드 파라미터 오류

person_like('제이식',28,1,2,3,gender='여자')
person_like(*['jsik',29,1,2,3],**{'gender':'남자'})


#디폴트 파라미터
#사용자가 파라미터값을 전달하지않아도 기본값이 파라미터에 존재하는경우
#C계열에서 볼 수 있는 파라미터 형식과 같다.
#파라미터를 생략해도 자동으로 기본값이 들어간다.
#디폴트 파라미터는 오른쪽부터 채워나가야한다.

#디폴트 파라미터가 앞에 온 경우 ->Error
#왜 에러가 나는가 ? 디폴트 파라미터로 인해, 인자의 위치가 뒤틀리기 때문
# def default_param1(a=20,b):
#     return a+b

def default_param2(a,b=20):
    print((a+b))


# 전달하지 않으면 생략가능
default_param2(10) # 10+20 = 30
# 전달하면, 기본값이 아닌 입력값으로 변수 설정
default_param2(10,30) # 10+30 = 40


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