dic = {}
i=0
while i<5:
    number = input("输入学生学号：")
    name = input("输入学生姓名：")
    dic.__setitem__(number,name)
    i+=1
    print("排序前：%s"%dic)

def dict2list(dic:dict):
    ''' 将字典转化为列表 '''
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst
    new = sorted(dict2list(dic), key)

new=sorted(dict2list(dic),key=lambda x:x[0],reverse=False)
print("排序后：%s"%new)