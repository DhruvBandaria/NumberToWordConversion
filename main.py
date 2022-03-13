
def getWordNumber(number):
    numberLen = len(str(number))
    i = numberLen
    temp = number
    rem = 0
    numberPres = 0
    wordStr = ""
    if number == 0:
        return numberWord1[0]
    while i > 0:
        rem = temp % 1000
        temp = int(temp / 1000)

        if(numberPres==0):
            wordStr = getWord(rem,0)
        elif numberPres == 3:
            wordtemp = getWord(rem,0)
            if(wordtemp != ''):
                wordStr = wordtemp + numberWord4[1] + ' ' + wordStr
        elif numberPres == 6:
            wordtemp = getWord(rem,0)
            if(wordtemp != ''):
                wordStr = wordtemp + numberWord4[2] + ' ' + wordStr
        else:
            wordtemp = getWord(rem,0)
            if(wordtemp != ''):
                wordStr = wordtemp + numberWord4[3] + ' ' + wordStr
        numberPres+=3
        i-=3
    return wordStr


def getWord(number,currentPres):
    temp = number
    word = ''
    if temp == 0:
        return ''
    while temp != 0:
        rem = temp % 10
        tempRem = temp % 100
        if tempRem >= 11 and tempRem <= 19 and currentPres == 0:
            word = numberWord3[rem-1] + ' '
            currentPres+=2
            temp = temp//100
            continue
        if(rem == 0):
            currentPres+=1
            temp = temp // 10
            continue
        if(currentPres == 0):
            word = numberWord1[rem] + ' ' + word
        elif(currentPres == 1):
            word = numberWord2[rem-1] + ' ' + word
        elif(currentPres == 2):
            word = numberWord1[rem] + ' ' + numberWord4[0] + ' ' + word
        currentPres+=1
        temp = temp // 10
    return word


numberWord1 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
numberWord2 = ['Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
numberWord3 = ['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
numberWord4 = ['Hundred','Thousand','Million','Billion']

# number = int(input("Enter a number:"))
# numberLen = len(str(number))
# print(getWordNumber(number))



