# 에러 처리를 안한 경우
# print('10년 뒤 나이를 계산해봅니다.. ',int(input('현재 나이를 입력해주세요 >>'))+10) #error

# try:
#     after_year = int(input('현재 나이를 입력해주세요 >>'))
#     print('10년 뒤 나이를 계산해봅니다.. ',after_year+10) #error
# except ValueError as e :
#     print('숫자만 입력해주세요' , e)
# else :
#     print("정상작동")
# finally:
#     print("최종적으로 이것이 출력됩니다.")

try:
    print("에러를 발생시켜보자")
    raise ValueError('에러 메세지도 함께 던져보자!')
except ValueError as e:
    print("ValueError를 발생시켜보았다.",e)


# def isEven():
#     value =int(input('숫자를 입력 >>'))
#     if value %2 !=0 :
#         raise Exception('%s는 짝수가 아닌데~' % value)
#     print("짝수가 맞습니다.")
#
# try:
#     isEven()
# except Exception as e:
#     print(e)



#커스텀 예외 클래스
# class NotEvenException(Exception):
#     def __init__(self):
#         super().__init__("짝수가 아닙니다!!!")
#
# def isEven():
#     value =int(input('숫자를 입력 >>'))
#     if value %2 !=0 :
#         raise NotEvenException()
#     print("짝수가 맞습니다.")
#
# try:
#     isEven()
# except NotEvenException as e:
#     print(e)


class NotEvenException(Exception):
    pass

def isEven():
    value =int(input('숫자를 입력 >>'))
    if value %2 !=0 :
        raise NotEvenException('Not Even')
    print("짝수가 맞습니다.")

try:
    isEven()
except NotEvenException as e:
    print(e)
