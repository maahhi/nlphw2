with open("predictor.txt") as pr:
    clas = 1
    prrc=[0,0,0,0]#11,12,22,21
    for line in pr:

        line = float(line)
        if clas > 0:
            if line >0:
                prrc[0]+=1 #class 1 true
            else:
                prrc[1]+=1#class 1 false
        else:
            if line > 0:
                prrc[3] += 1#class 2 false
            else:
                prrc[2] += 1#class 2 true

        if(clas==-1):
            clas =1
        else:
            clas=-1

    pr1=prrc[0]/(prrc[0]+prrc[1])
    rc1=prrc[0]/(prrc[0]+prrc[3])
    pr2=prrc[2]/(prrc[2]+prrc[3])
    rc2=prrc[2]/(prrc[2]+prrc[1])

    print("pr1" , pr1)
    print("pr2" , pr2)
    print("rc1" , rc1)
    print("rc2" , rc2)
