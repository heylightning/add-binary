fNum = int(input("Enter the first number: "))
sNum = int(input("Enter the second number: "))

for streams in list(str(fNum)):
    if streams in ['2','3','4','5','6','7','8','9']:
        print('Error: Invalid input.')
        exit()

for streams in list(str(sNum)):
    if streams in ['2','3','4','5','6','7','8','9']:
        print('Error: Invalid input.')
        exit()

resultList = []
def addBinary(fNum, sNum):
    sfNum = str(fNum); ssNum = str(sNum); tempVar = 0; carry = False; aCon = False
    if(len(sfNum) > len(ssNum)):
        maxNum = sfNum; minNum = ssNum
    elif(len(sfNum) == len(ssNum)):
        maxNum = sfNum; minNum = ssNum
    else:
        maxNum = ssNum; minNum = sfNum
    conTemp = int(max(len(ssNum), len(sfNum)) - min(len(ssNum), len(sfNum)))
    for a in range(conTemp):
        minNum = '0' + minNum
    for iteration in range((max(len(sfNum), len(ssNum))-1), -1, -1):
        tempVar+=1
        if(maxNum[iteration] == '0' and minNum[iteration] == '1'):
            if(carry == False):
                resultList.append('1')
            else:
                resultList.append('0'); carry = True   
        if(maxNum[iteration] == '1' and minNum[iteration] == '0'):
            if(carry == False):
                resultList.append('1')
            else:
                resultList.append('0'); carry = True
        if(maxNum[iteration] == '0' and minNum[iteration] == '0'):
            if(carry == False):
                resultList.append('0')
            else:
                resultList.append('1'); carry = False
        if(maxNum[iteration] == '1' and minNum[iteration] == '1'):
            if(tempVar == max(len(ssNum), len(sfNum))):
                if(carry == False):
                    resultList.append('1'); resultList.append('0'); aCon = True; break
                else:
                    resultList.append('1'); resultList.append('1'); break
            else:
                if(carry == False):
                    resultList.append('0'); carry = True
                else:
                    resultList.append('1'); carry = True
    if(len(maxNum) == 1 and len(resultList) == 2):
        print("".join(resultList))
    else:
        if(aCon == True):
            resultList.reverse()
            resultList[0] = '1'; resultList[1] = '0'
            print("".join(resultList))
        else:
            resultList.reverse()
            print("".join(resultList))
addBinary(fNum, sNum)