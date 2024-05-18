def sudoku_checker(value):
    l1=value[0]
    l2=value[1]
    l3=value[2]
    l4=value[3]
    l5=value[4]
    l6=value[5]
    l7=value[6]
    l8=value[7]
    l9=value[8]

    b=[]
    v=[]
    print("THE GIVEN SUDOKU IS :")
    print()
    su=l1+l2+l3+l4+l5+l6+l7+l8+l9
    for i in range(0,len(su)):
        if i%9!=8:
            print(su[i],'  ',end='')
        elif i%9==8:
            print(su[i],'  ',end='\n')
        else:
            print()
    print()

    dic={1:l1,2:l2,3:l3,4:l4,5:l5,6:l6,7:l7,8:l8,9:l9}
    check=0
    for i in range(0,9):
        for x in dic.keys():
            v.append(dic[x][i])
        ct=0
        if i%3==0:
            b.clear()
            for y in dic.keys():
                b.append([dic[y][i],dic[y][i+1],dic[y][i+2]])
        if b !=[]:
            b1=b2=b3=[]
            b1=b[0],b[1],b[2]
            b2=b[3],b[4],b[5]
            b3=b[6],b[7],b[8]
        for j in range(1,10):
            
            aa=[]
            bb=[]
            aa+=dic[j]
            aa.remove(v[j-1])
            bb+=v
            bb.remove(v[j-1])
           
            if v[j-1] not in aa and v[j-1] not in bb:
                check+=1
                aa.clear()
                bb.clear()
            else:
                check=0
        v.clear()


    print(check,'#')
    if check==81:
        return True
    else:
        return False
#print(sudoku_checker())
