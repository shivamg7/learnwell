from bsl.models import Question


category = "PSY"
myfilename = "Psychology.txt"
myfile = open('data/'+myfilename,'r')
outfile = open('data/out'+myfilename,'w')


for i in range(1,100):
    correct='A'
    text = myfile.readline().rstrip().replace(',',' ')
    optionA = myfile.readline().rstrip()
    optionB = myfile.readline().rstrip()
    optionC = myfile.readline().rstrip()
    optionD = myfile.readline().rstrip()

    while(myfile.readline()=='\n'):
        last_pos = myfile.tell()

    myfile.seek(last_pos)

    if(optionA[0:1]=='1'):
        correct = 'A'
    elif(optionB[0:1]=='1'):
        correct = 'B'
    elif(optionC[0:1]=='1'):
        correct = 'C'
    elif(optionD[0:1]=='1'):
        correct = 'D'

    optionA = optionA[2:].strip().replace(',',' ')
    optionB = optionB[2:].strip().replace(',',' ')
    optionC = optionC[2:].strip().replace(',',' ')
    optionD = optionD[2:].strip().replace(',',' ')


    #outfile.write(text+','+optionA+','+optionB+','+optionC+','+optionD+','+correct+'\n')

    #print(text+','+optionA+','+optionB+','+optionC+','+optionD+','+correct)

    questionVar = Question(text=text,optionA=optionA,optionB=optionB,optionC=optionC,optionD=optionD,answer=correct,category=category,rating=i*17)
    questionVar.save()
