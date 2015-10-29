B = [[" "," "," "],[" "," "," "],[" "," "," "]]

print(B[0][0],"|",B[0][1],"|",B[0][2])
print("---------")
print(B[1][0],"|",B[1][1],"|",B[1][2])
print("---------")
print(B[2][0],"|",B[2][1],"|",B[2][2])

currentplayer ="X"
HAVEWON=False
turn=1
Winner=""

def check1(y):
    global HAVEWON,Winner
    numX=0
    numO=0
    for x in range(3):
        if B[x][y]=="X":
            numX=numX+1
        elif B[x][y]=="O":
            numO=numO+1
        if numX ==3:
            Winner = "X"
            HAVEWON = True
        elif numO==3:
            Winner = "O"
            HAVEWON = True

def check2(y):
    global HAVEWON,Winner
    numX=0
    numO=0
    for x in range(3):
        if B[y][x]=="X":
            numX=numX+1
        elif B[y][x]=="O":
            numO=numO+1
        if numX ==3:
            Winner = "X"
            HAVEWON = True
        elif numO==3:
            Winner = "O"
            HAVEWON = True

while turn < 10 and HAVEWON == False:

    print("current player:",currentplayer)
    row = int(input("Enter row(1-3):"))-1
    while row >2 or row <0 : 
        print("Wrong input. Try again.")
        row = int(input("Enter row(1-3):"))-1
    col = int(input("Enter col(1-3):"))-1
    while col >2 or col <0 :
        if col ==10085: #enter 10086 to regret last enter
            row = int(input("Enter row(1-3):"))-1
            col = int(input("Enter col(1-3):"))-1
        else:
            print("Wrong input. Try again.")
            col = int(input("Enter col(1-3):"))-1
        
    if B[row][col]==" ": 
        B[row][col]=currentplayer

        print(B[0][0],"|",B[0][1],"|",B[0][2])
        print("---------")
        print(B[1][0],"|",B[1][1],"|",B[1][2])
        print("---------")
        print(B[2][0],"|",B[2][1],"|",B[2][2])
        turn=turn+1

        if turn%2==0:
            currentplayer="O"
        else:
            currentplayer="X"
    
    else:
        print('------------------------')
        print('│Wrong input!Try again!│')
        print('------------------------')



    check1(0)
    if HAVEWON== False:
        check1(1)
    if HAVEWON== False:
        check1(2)

    if HAVEWON== False:
        check2(0)

    if HAVEWON== False:
        check2(1)

    if HAVEWON== False:
        check2(2)



    if HAVEWON == False and B[0][0]==B[1][1] and B[1][1]==B[2][2]:
        if B[1][1]=="X":
            Winner = "X"
            HAVEWON= True
        elif B[1][1]=="O":
            Winner = "O"
            HAVEWON = True



if HAVEWON == True:
    if Winner=="X":
        print ("Winner is X!")
    elif Winner=="O":
        print ("Winner is O!")
    else:
        print ("No one wins!")
