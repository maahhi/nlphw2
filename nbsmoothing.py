import re
import math
with open('train.txt') as train, open('test.txt')as test ,open('predictsmothing.txt','w') as prd:
    traintxt = train.readlines()
    i = 0
    class1wordcount={}
    class2wordcount={}
    for line in traintxt:
        clas=line[0:2]
        if clas=='1|':#1:class 1
            line = re.split(' |\n|\r|\t|',line[3:])
            for word in line:
                if word not in class1wordcount:
                    class1wordcount[word] = 1
                else:
                    class1wordcount[word] += 1
                class1wordcount['']=1
                class1wordcount['unk']=1
        else:#-1:class 2
            line = re.split(' |\n|\r|\t|',line[4:])
            for word in line:
                if word not in class2wordcount:
                    class2wordcount[word] = 1
                else:
                    class2wordcount[word] += 1
                class2wordcount['']=1
                class2wordcount['unk']=1

    class1sumwords = sum(class1wordcount.values())
    class1proboftokens = {}
    for key, value in class1wordcount.items():
        class1proboftokens[key] = math.log10(value+1 / class1sumwords+len(class1wordcount))

    class2sumwords = sum(class2wordcount.values())
    class2proboftokens = {}
    for key, value in class2wordcount.items():
        class2proboftokens[key] = math.log10(value+1 / class2sumwords+len(class2wordcount))



    recallprecision={}
    recallprecision['11'] = 0
    recallprecision['12'] = 0
    recallprecision['21'] = 0
    recallprecision['22'] = 0

    testtxt= test.readlines()
    for line in testtxt:
        lable=line[0:2]
        if lable=='1|':
            line = re.split(' |\n|\r|\t|', line[3:])
            lable='1'
        else:
            line = re.split(' |\n|\r|\t|', line[4:])
            lable='2'

        probofthislineinclass1=0
        probofthislineinclass2=0
        for word in line:
            if word == '':
                continue

            if word not in class1proboftokens:
                probofthislineinclass1 += class1proboftokens['unk']
            else:
                probofthislineinclass1 += class1proboftokens[word]

            if word not in class2proboftokens:
                probofthislineinclass2 += class2proboftokens['unk']
            else:
                probofthislineinclass2 += class2proboftokens[word]

        if probofthislineinclass1>probofthislineinclass2:
            predict='1'
        else:
            predict='2'
        strr='lable:'+lable+', predict:'+predict+'\n'
        prd.write(strr)

        tag=lable+predict
        recallprecision[tag]+=1

    print(recallprecision)

    recallforclass1 = recallprecision['11'] / (recallprecision['11'] + recallprecision['12'])
    precisionforclass1 = recallprecision['11'] / (recallprecision['11'] + recallprecision['22'])
    recallforclass2 = recallprecision['22'] / (recallprecision['22'] + recallprecision['21'])
    precisionforclass2 = recallprecision['22'] / (recallprecision['22'] + recallprecision['11'])


    prd.write('recal for class1: ' + str(recallforclass1) + ', precision for class1: ' + str(precisionforclass1) + '\n')
    prd.write('recal for class2: ' + str(recallforclass2) + ', precision for class2: ' + str(precisionforclass2) + '\n')







