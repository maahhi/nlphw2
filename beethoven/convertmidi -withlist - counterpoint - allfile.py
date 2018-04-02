    #crp : two first line in 11-crp file is valueless

def convmidi(oldfilename):
    last_time = ''
    pastnote = 0#crp
    currentnote = 0#crp
    notelist=[]
    oldfilename = oldfilename + '.txt' #input("file name without .txt\n") + '.txt'
    newfilename = '00' + oldfilename
    cpfilename = '11' + oldfilename
    hrmfilename = '22' + oldfilename
    hrm1 = 0

    with open(oldfilename) as oldfile, open( newfilename, 'w') as newfile, open( cpfilename, 'w') as cpfile, open( hrmfilename, 'w') as hrmfile:
        for line in oldfile:
            words = line.split()
            if words[1]=='Off'or words[3][0:1]!='n':
                continue
            note=words[3][2:]
            time=words[0]
            
            if time == last_time:
                notelist.append(note)
            else:
                
                notelist.sort()
                if len(notelist) >>0:#for initial case that note list size is 0
                    hrm1 = notelist[0]#hrm
                    currentnote = notelist[0]#crp
                    if len(notelist) >>1 :#hrm
                        hrm1 = notelist[0]
                i = 0
                for n in notelist :
                    if int(n) << int(pastnote):
                        currentnote = n#crp
                    if len(notelist) >> 1 and i >> 0 :
                        if abs(int(n)-int(hrm1)) > 0:#hrm
                            hrmfile.write(str(abs(int(n)-int(hrm1)))+' ')
                            hrm1 = n
                    newfile.write(n)
                    if (i!= (len(notelist)-1)):# harmonic notes in new file
                        newfile.write('|')
                    i=i+1
                interval = int(pastnote)-int(currentnote)#crp
                cpfile.write(str(interval)+ ' ')#crp
                #print(notelist)
                #print(pastnote , currentnote , interval)
                pastnote=currentnote#crp
                newfile.write(' ')
                notelist = []
                notelist.append(note)

            last_time = time
            
        if notelist!=[]:
            #print(notelist)
            i = 0
            notelist.sort()
            if len(notelist) >>0:
                currentnote = notelist[0]    
                if len(notelist) >>1 :
                    hrm1 = notelist[0]
            for n in notelist :
                if int(n) < int(pastnote):
                    currentnote = n
                if len(notelist) >>1 :
                    if abs(int(n)-int(hrm1)) > 0:
                        hrmfile.write(str(abs(int(n)-int(hrm1)))+' ')
                        hrm1 = n
                newfile.write(n)
                if (i!= (len(notelist)-1)):
                    newfile.write('|')
                    #print(n)
                    #print(len(notelist))
                i=i+1
            interval = int(pastnote)-int(currentnote)
            cpfile.write(str(interval)+ ' ')
            pastnote=currentnote




allfile = input('input all files name without .txt and seprated')
filelist = allfile.split()
for file in filelist:
    print(file)
    convmidi(file)
