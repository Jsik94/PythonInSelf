'''


    input() : 표준입으로 부터 사용자 입력을 받는 함수.
    입력값은 모두 문자열임!

'''

# print('[input() 함수]',end='')
# print('\n나이를 입력하세요 ')
# a=input()
# print('입력값: %s 타입 : %s' %(a,type(a)))

'''

    파라미터 : 안내메세지 가능
'''

# b=input('성적을 입력하세요 >>')
# print('입력값: %s 타입 : %s' %(b,type(b)))

'''
    split() 메소드를 통해서 구분하여 넣을 수도 있다.
'''

# c=input('값을 여러개 입력해볼래 ? ,로 구분해서!').split(',')
# print('입력값: %s 타입 : %s' %(c,type(c)))
#
#
# c,d,e,f=input('값을 4개 입력해볼래 ? ,로 구분해서!').split(',')
# print('입력값: %s 타입 : %s' %(c,type(c)))
# print('입력값: %s 타입 : %s' %(d,type(d)))
# print('입력값: %s 타입 : %s' %(e,type(e)))
# print('입력값: %s 타입 : %s' %(f,type(f)))



'''
    타입 종류 : () - 튜플 {} - 딕셔너리 [] - 리스트

'''

# print('두개의 데이터를 입력해볼래 ?')
# d,e = input().split(' ')
# print('입력값: %s 타입 : %s' %(d,type(d)))
# print('입력값: %s 타입 : %s' %(e,type(e)))
#
# print('그냥 더한다면 ?' , d+e)
# print('숫자로 더하려면 ? ' , int(d)+int(e))

'''
    Map 함수
    입력값을 변경할 때 map을 쓰면 유용함
    map(함수,리스트 or 튜플 )
    구조분해의 특징을 가진 놈임 
'''
# #숫자데이터 받기
# a,b = map(int,input('숫자 데이터 두개를 주시오').split(' '))
# print( a,' - ' , type(a))
# print( b,' - ' , type(b))
#
# #리스트 초기화 시키기
# #b를 그냥 찍으면 map 객체의 주소가 나옴
# b = map(lambda a : a+1,range(5));
# print(list(b) ,' - ',b, ' - ',type(b))


'''
    print 함수 
    sep 키워드 -,로 구분된 값들을 구분자로 합침
    end 키워드 -끝을 지정할 수 있음 주로 줄바꿈을 하지 않을때 많이 사용 default \n
    file 키워드 - 표준 출력을 파일로 혹은 에러처리할 때 많이 사용 

'''

# sep 과 end 적용
# print('요호요호','요호호호',sep='-',end='')

# import sys
# a,b = map(int,input('입력해 봐라 ').split(' '))
# print(a,b,file=sys.stderr)
#
# f=open('inputNprintResult','w')
# #파일에 쓰기
# print(a,b,file=f)
# f.close()

a= [1,2,3]
a.append(4)
print(a)
a.pop()
print(a)