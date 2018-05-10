import re
bachfilename = '000allfileof00bach.txt'
beetfilename = '000allfileof00beet.txt'
bach =0
beet =0


def toabc(words):
    newfile=''
    for goh in words:
        if goh == 'a' or goh == '' :
            continue
        gohh = goh.split('|')
        i = 0
        for word in gohh:
            if i > 0:
                newfile+=('o')
            i=i+1
            notenumber = int(word)
            remain = notenumber%12
            if remain == 0 :
                newfile+='C'
            if remain == 1 :
                newfile+=('Cs')
            if remain == 2 :
                newfile+=('D')
            if remain == 3 :
                newfile+=('Ds')
            if remain == 4 :
                newfile+=('E')
            if remain == 5 :
                newfile+=('F')
            if remain == 6 :
                newfile+=('Fs')
            if remain == 7 :
                newfile+=('G')
            if remain == 8 :
                newfile+=('Gs')
            if remain == 9 :
                newfile+=('A')
            if remain == 10 :
                newfile+=('As')
            if remain == 11 :
                newfile+=('B')
        newfile+=(' ')
    return newfile
          


with open(bachfilename) as bachf, open(beetfilename) as beetf:
    for line in bachf:
        if (len(line) < 10 or len(line) > 1000 ):
            continue;
        bach=bach+1
    for line in beetf:
        if (len(line) < 10 or len(line) > 1000 ):
            continue;
        beet=beet+1
with open(bachfilename) as bachf, open(beetfilename) as beetf, open('vwtrain.txt','w')as train, open('ttrain.txt','w')as trainn , open('vwtest.txt','w') as test, open('ttest.txt','w') as testt:
    linesbach=bachf.readlines()
    linesbeet=beetf.readlines()

    for i in range(bach-1):
        newbach=linesbach[i]#.replace('|','o')
        newbeet=linesbeet[i]#.replace('|','o')

        newbach = re.split(' |\n|\r|\t|',newbach)
        newbeet = re.split(' |\n|\r|\t|',newbeet)
        
        
        if(i%4==0):
            test.write('1|'+toabc(newbach)+'\n')
            test.write('-1|'+toabc(newbeet)+'\n')
        else:
            train.write('1|'+toabc(newbach)+'\n')
            train.write('-1|'+toabc(newbeet)+'\n')
print(bach,beet)
print(beet/bach)
