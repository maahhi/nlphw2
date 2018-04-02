filename=input('filename')+'.txt'
newfilename = 'abc'+filename+'.txt'
with open (filename) as oldfile , open(newfilename,'w')as newfile:
    for line in oldfile:
        linelist=line.split();
        for words in linelist:
            wordlist=words.split('|')
            i = 0
            for word in wordlist:
                if word == 'a':
                    continue
                if i > 0:
                    newfile.write('|')
                i=i+1
                notenumber = int(word)
                remain = notenumber%12
                if remain == 0 :
                    newfile.write('C')
                if remain == 1 :
                    newfile.write('C#')
                if remain == 2 :
                    newfile.write('D')
                if remain == 3 :
                    newfile.write('D#')
                if remain == 4 :
                    newfile.write('E')
                if remain == 5 :
                    newfile.write('F')
                if remain == 6 :
                    newfile.write('F#')
                if remain == 7 :
                    newfile.write('G')
                if remain == 8 :
                    newfile.write('G#')
                if remain == 9 :
                    newfile.write('A')
                if remain == 10 :
                    newfile.write('A#')
                if remain == 11 :
                    newfile.write('B')
            newfile.write(' ')
            


