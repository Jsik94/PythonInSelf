# import 모듈명
# 해당키워드로 모듈을 import할수 있음
#폴더를 임포트하려면 __init__을 오버라이딩 하여 모듈을 엮으면 됨


# from modules import *
# print(dir())
# print(getYear(),getMonth(),getDate())

# from modules.module4 import *
# print(dir())
# print(getYear(),getMonth(),getDate())


from modules import *
print(dir())

# 패키지 파일에 __all__을 지정하면 지정한것만 외부공개가됨
print(getYear(),getMonth(),getDate())
