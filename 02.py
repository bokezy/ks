
while True:
    data = int(input("请输入0-9的整数"))
    if data==5:
        print("恭喜!猜对了")
        break
    elif data >5:
        print("太大")
    elif data <5:
        print("太小")
