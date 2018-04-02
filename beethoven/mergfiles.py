fileoffilenames=input('input name of file of all files')+'.txt'
pishvand = input('pishvand')
pishvandf = '000'+'allfileof'+pishvand+'.txt'
with open(fileoffilenames) as fffn:
    for line in fffn:
        filenamelist = line.split()
print(filenamelist)

with open(pishvandf,'w') as final:
    for fn in filenamelist:
        print(fn)
        newfilename = pishvand+fn+'.txt'
        with open(newfilename)as newfile:
            for line in newfile :
                final.write(line)
                
print('end')

