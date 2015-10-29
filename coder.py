import random
L1='QWERTYUIOPASDFGHJKLZXCVBNM'
L2='qwertyuiopasdfghjklzxcvbnm'
number = int(input('How many digits do u want?' ))
for x in range(0,number):
    index= random.randrange(2)
    if index == 0:
        pw= ''
for x in range(0,number):
    index = random.randrange(2)
    if index == 0:
        index = random.randrange(25)
        pw = pw + L1[index]
    else:
        index = random.randrange(25)
        pw = pw+ L2[index]
print(pw)
'''可以优化的地方有：
1.给出用户输入时的最大最小默认值。
2.给出用户是否只需要大写或者小写的选择
3.增加密码字符的范围'''
