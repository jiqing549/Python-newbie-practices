def calendar(days,index):
    if days < 1 or days > 31:
        print('Invalid number!')
    elif index <0 or index > 6:
        print('Invalid number!')           #这里两个if其实可以合起来写
    else:
        print("Su  M   Tu  W   Th  F   Sa")      #两位数占两个字节 所以中间空两格


    for x in range(index):
        print("    ",end="")  #这里的end作用是打印空格后不换行，再打印引号内的东西

    for i in range(1, days+1):

        if i < 10:

            print(str(i),end="   ")


        else:
                print(str(i),end="  ")

        if (i+index)%7 == 0:

            print()

    print()  #这个print作用是 在结束日历打印之后换行

numDays = int(input("How many days does the month have? "))
numIndex= int(input("How many days should we skip at first? "))

calendar(numDays,numIndex)

