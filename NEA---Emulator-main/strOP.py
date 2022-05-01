
def findOP(fw,fw2,fw3,fw4):
    errorcode = "NOT CORRECT FORMAT"
    try:
        if fw == "#":
            return "comment"

        if fw == "CLS":
            return "0x00E0"
        elif fw == "RET":
            return "0x00EE"

        elif fw == "JP":
            if fw2[0:1] == "V0":
                return "Bnnn"
            else:
                return "1nnn"

        elif fw == "CALL":
            return "2nnn"

        elif fw == "SE":
            if fw3[0] == "V":
                return "5xy0"
            else:
                return "3xkk"

        elif fw == "SNE":
            if fw3[0] == "V":
                return "9xy0"
            else:
                return "4xkk"


        elif fw == "OR":
            return "8xy1"

        elif fw == "XOR":
            return "8xy3"

        elif fw == "AND":
            return "8xy2"

        elif fw == "ADD":
            if fw3[0] == "V":
                return "7xkk"

            elif fw2 == "I":
                return "Fx1E"

        elif fw == "SUB":
            return "8xy5"

        elif fw == "SHR":
            return "8xy6"

        elif fw == "SUBN":
            return "8xy7"

        elif fw == "SHL":
            return "8xyE"

        elif fw == "LD":
            if fw2[0] == "I":
                if len(fw2) > 1:
                    return "Fx55"
                else:    
                    return "Annn"
            if fw3[0] == "I":
                if len(fw3) > 1:
                    return "Fx65"
            elif fw3 == "DT":
                return "Fx07"
            elif fw3 == "K":
                return "Fx0A"
            elif fw2[0:1] == "DT":
                return "Fx15"
            elif fw2[0:1] == "ST":
                return "Fx18"
            elif fw2[0] == "F":
                return "Fx29"
            elif fw2[0] == "B":
                return "Fx33"
            elif fw2[0] == "V":
                return "6xkk"

        elif fw == "RND":
            return "Cxkk"

        elif fw == "DRW":
            return "Dxyn"

        elif fw == "SKP":
            return "Ex9E"

        elif fw == "SKNP":
            return "ExA1"
        else:
            print(fw,fw2,fw3,fw4)
    except:
        print("Error - ", errorcode)

def toBytes(word,line):
    if word == None:
        return None
    if word == "comment":
        return None
    print(word)
    print(word[1:4])

    if word == "0x00E0":
        return int(0x00E0)
    elif word == "0x00E0":
        return int(0x00E0)

    p1 = word[0]
    print(p1)
    p1 = bin(int(p1))
    print(p1)
    lineword = line[1]
    print(lineword)



    if word[1:4] == "xyn":
        l1 = 4
        l2 = 4
        l3 = 4
        l4 = 4
        p2 = lineword[1:-1]
        p2 = bin(int(p2))
        lineword = line[2]
        p3 = lineword
        p3 = bin(int(p3))
        lineword = line[3]
        p4 = lineword
        p4 = bin(int(p4))
    
    elif word[1:4] == "nnn":
        l1 = 4
        l2 = 12
        l3 = 0
        l4 = 0
        p2 = lineword
        print(p2)
        p2 = bin(int(p2))
        p3 = ""
        p4 = ""

    elif word[1:3] == "xy":
        l1 = 4
        l2 = 4
        l3 = 4
        l4 = 4
        p2 = lineword[1:-1]
        print ("part2")
        p2 = bin(int(p2))
        lineword = line[2]
        p3 = lineword
        p3 = bin(int(p3))
        p4 = word[3]
        p4 = bin(int(p4))


    elif word[1:4] == "xkk":
        l1 = 4
        l2 = 4
        l3 = 8
        l4 = 0
        p2 = lineword[1:-1]
        p2 = bin(int(p2))
        print("p2: " + p2)
        lineword = line[2]
        p3 = lineword
        p3 = bin(int(p3))
        print("p3: " + p3)
        p4 = ""
        
    
    elif word[1] == "x":
        l1 = 4
        l2 = 4
        l3 = 8
        l4 = 0
        print("yes in here")
        p2 = lineword[1:-1]
        print(p2+"  ...")
        print(int(p2))
        p2 = bin(int(p2))
        print(p2)
        print("pro")

        lineword = line[2]
        print(lineword)
        p3 = lineword
        print(p3)
        p3 = bin(int(p3))

        p4 = ""
        print(p4)

    print(p1,p2,p3,p4)

    fp1 = p1 
    fp2 = p2
    fp3 = p3 
    fp4 = p4

    finalList = [fp1,fp2,fp3,fp4]
    print ("final", finalList)
    finalLen = [l1,l2,l3,l4]
    print (finalLen)
    finalStrForm = ""

    for item in finalList:
        print("start")
        lengthOfData = finalLen[finalList.index(item)]
        print("data len:", lengthOfData, " value:", item) 
        if lengthOfData == 0:
            item = ""
            break
        elif lengthOfData == 4:
            looplen = 4 
        elif lengthOfData == 8:
            looplen = 8
        elif lengthOfData == 12:
            looplen = 12 
        elif lengthOfData == 16:
            break
        listofbin = ["","0","00","000","0000","00000","000000","0000000","00000000","000000000","0","0","0","0","0","0","0"]
        if not (len(item[2:])) == lengthOfData:
            print(item)
            print("lenofshift:" , (lengthOfData - len(item[2:])))
            item = listofbin[(lengthOfData - len(item[2:]))] + (item[2:])
            print(item)
        else:
            item = item [2:]
            #item = bin(item)
        print (item)
        finalStrForm = finalStrForm + (item)

        print ("final add", finalList) 
        print(finalStrForm, "strver")
    finalList2 = []

    finalValue = finalStrForm
    finalValue = int(finalValue,2)
    finalValue = hex(finalValue)
    finalValue = finalValue[2:]
    final1 = finalValue[:2]
    final2 = finalValue[2:]
    print("should be ", final1)

    final1 = "0x" + final1
    final1 = int(final1,16)
    print(final1)

    final2 = "0x" + final2
    final2 = int(final2,16)
    print(final2)
    
    finalList2.append(final1)
    finalList2.append(final2)

    print(finalList2)
    return finalList2





