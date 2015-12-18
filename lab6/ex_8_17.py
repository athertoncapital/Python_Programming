def cypher():
    st1=input("Please let me know your message: ")
    st2=input("Please type in your code, i.e., the mapping. You should type 26 letters in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' order.")
    j=""
    for i in range(len(st1)):
        if ord(st1[i])<=90 and ord(st1[i])>=65:
            a=st1[i]
            if ord(st1[i])==65 or ord(st1[i])==97:
                a=st2[0]
            elif ord(st1[i])==66  or ord(st1[i])==98:
                a=st2[1]
            elif ord(st1[i])==67  or ord(st1[i])==99:
                a=st2[2]
            elif ord(st1[i])==68  or ord(st1[i])==100:
                a=st2[3]
            elif ord(st1[i])==69  or ord(st1[i])==101:
                a=st2[4]
            elif ord(st1[i])==70  or ord(st1[i])==102:
                a=st2[5]
            elif ord(st1[i])==71  or ord(st1[i])==103:
                a=st2[6]
            elif ord(st1[i])==72  or ord(st1[i])==104:
                a=st2[7]
            elif ord(st1[i])==73  or ord(st1[i])==105:
                a=st2[8]
            elif ord(st1[i])==74  or ord(st1[i])==106:
                a=st2[9]
            elif ord(st1[i])==75  or ord(st1[i])==107:
                a=st2[10]
            elif ord(st1[i])==76  or ord(st1[i])==108:
                a=st2[11]
            elif ord(st1[i])==77  or ord(st1[i])==109:
                a=st2[12]
            elif ord(st1[i])==78  or ord(st1[i])==110:
                a=st2[13]
            elif ord(st1[i])==79  or ord(st1[i])==111:
                a=st2[14]
            elif ord(st1[i])==80  or ord(st1[i])==112:
                a=st2[15]
            elif ord(st1[i])==81  or ord(st1[i])==113:
                a=st2[16]
            elif ord(st1[i])==82  or ord(st1[i])==114:
                a=st2[17]
            elif ord(st1[i])==83  or ord(st1[i])==115:
                a=st2[18]
            elif ord(st1[i])==84  or ord(st1[i])==116:
                a=st2[19]
            elif ord(st1[i])==85  or ord(st1[i])==117:
                a=st2[20]
            elif ord(st1[i])==86  or ord(st1[i])==118:
                a=st2[21]
            elif ord(st1[i])==87  or ord(st1[i])==119:
                a=st2[22]
            elif ord(st1[i])==88  or ord(st1[i])==120:
                a=st2[23]
            elif ord(st1[i])==89  or ord(st1[i])==121:
                a=st2[24]
            elif ord(st1[i])==90  or ord(st1[i])==122:
                a=st2[25]
        elif ord(st1[i])>=97 and ord(st1[i])<=122:
            a=st1[i]
            if ord(st1[i])==65 or ord(st1[i])==97:
                a=st2[0]
            elif ord(st1[i])==66  or ord(st1[i])==98:
                a=st2[1]
            elif ord(st1[i])==67  or ord(st1[i])==99:
                a=st2[2]
            elif ord(st1[i])==68  or ord(st1[i])==100:
                a=st2[3]
            elif ord(st1[i])==69  or ord(st1[i])==101:
                a=st2[4]
            elif ord(st1[i])==70  or ord(st1[i])==102:
                a=st2[5]
            elif ord(st1[i])==71  or ord(st1[i])==103:
                a=st2[6]
            elif ord(st1[i])==72  or ord(st1[i])==104:
                a=st2[7]
            elif ord(st1[i])==73  or ord(st1[i])==105:
                a=st2[8]
            elif ord(st1[i])==74  or ord(st1[i])==106:
                a=st2[9]
            elif ord(st1[i])==75  or ord(st1[i])==107:
                a=st2[10]
            elif ord(st1[i])==76  or ord(st1[i])==108:
                a=st2[11]
            elif ord(st1[i])==77  or ord(st1[i])==109:
                a=st2[12]
            elif ord(st1[i])==78  or ord(st1[i])==110:
                a=st2[13]
            elif ord(st1[i])==79  or ord(st1[i])==111:
                a=st2[14]
            elif ord(st1[i])==80  or ord(st1[i])==112:
                a=st2[15]
            elif ord(st1[i])==81  or ord(st1[i])==113:
                a=st2[16]
            elif ord(st1[i])==82  or ord(st1[i])==114:
                a=st2[17]
            elif ord(st1[i])==83  or ord(st1[i])==115:
                a=st2[18]
            elif ord(st1[i])==84  or ord(st1[i])==116:
                a=st2[19]
            elif ord(st1[i])==85  or ord(st1[i])==117:
                a=st2[20]
            elif ord(st1[i])==86  or ord(st1[i])==118:
                a=st2[21]
            elif ord(st1[i])==87  or ord(st1[i])==119:
                a=st2[22]
            elif ord(st1[i])==88  or ord(st1[i])==120:
                a=st2[23]
            elif ord(st1[i])==89  or ord(st1[i])==121:
                a=st2[24]
            elif ord(st1[i])==90  or ord(st1[i])==122:
                a=st2[25]
        else:
		    a=st1[i]
        j=j+a
    print(j)
    
def main():
    cypher()
    
main()
