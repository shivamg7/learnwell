from bsl.models import question


category = "ECO"
myfilename = "Economics.txt"
myfile = open('data/'+myfilename,'r')

for i in range(1,100):
    correct='A'
    text = myfile.readline().rstrip()
    optionA = myfile.readline().rstrip()
    optionB = myfile.readline().rstrip()
    optionC = myfile.readline().rstrip()
    optionD = myfile.readline().rstrip()
    while(myfile.readline()=='\n'):
        last_pos = myfile.tell()
        myfile.readline()

    myfile.seek(last_pos)
    if(optionA[0:1]=='1'):
        correct = 'A'
    elif(optionB[0:1]=='1'):
        correct = 'B'
    elif(optionC[0:1]=='1'):
        correct = 'C'
    elif(optionD[0:1]=='1'):
        correct = 'D'

    optionA = optionA[2:].strip()
    optionB = optionB[2:].strip()
    optionC = optionC[2:].strip()
    optionD = optionD[2:].strip()

    print("Question",text)
    print("optionA",optionA)
    print("Correct Ans",correct)


    #questionVar = Question(text=text,optionA=optionA,optionB=optionB,optionC=optionC,optionD=optionD,answer=correct,category=category,level=5)
    #questionVar.save()
