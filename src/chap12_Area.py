import copy


def change1(data):
    data[0] =13;

def change2(data):
    mydata = data
    mydata[0] = 13

def change3(data):
    mydata = copy.copy(data)
    mydata[0] = 13

def change4(data):
    mydata = copy.deepcopy(data)
    mydata[0] = 13

print("1]")
origin_list = [1,2,3,4,5]
copy_list = origin_list
print(origin_list)
print("trans")
change1(origin_list)
print(origin_list)
print(copy_list)

print("2]")
origin_list = [1,2,3,4,5]
copy_list = origin_list
print(origin_list)
print("trans")
change1(origin_list)
print(origin_list)
print(copy_list)

print("3]")
origin_list = [1,2,3,4,5]
copy_list = origin_list
print(origin_list)
print("trans")
change3(origin_list)
print(origin_list)
print(copy_list)

print("4]")
origin_list = [1,2,3,4,5]
copy_list = origin_list
print(origin_list)
print("trans")
change4(origin_list)
print(origin_list)
print(copy_list)

add = lambda *args : "{} ~ {} 까지 합 : {}".format(min(args),max(args),sum(args)) if args else '값이 없다~'
print(add)
print(add(10,80,30))
