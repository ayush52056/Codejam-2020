def ND(string,answer,previous):
    if previous!='' and string!='':
        if int(previous)>int(string[0]):
            for k in range(int(previous)-int(string[0])):
                answer=answer+')'
    if string=='':
        for i in range(int(previous)):
            answer=answer+')'
        return answer
    if int(string[0])==0:
        return ND(string[1:],answer+string[0],string[0])
    if int(string[0])==1:
        if previous!='':
            if int(previous)==0:
                answer=answer+'('+string[0]
            else:
                answer=answer+string[0]
        else:
            answer=answer+'('+string[0]
        return ND(string[1:],answer,string[0])
    if int(string[0])>1:
        if previous !='':
            for i in range(int(string[0])-int(previous)):
                answer=answer+'('
            answer=answer+string[0]
        else:
            for i in range(int(string[0])):
                answer=answer+'('
            answer=answer+string[0]
        return ND(string[1:],answer,string[0])

for i in range(int(input())):
    S=input()
    answer=''
    previous=''
    final=ND(S,answer,previous)
    print('Case #{}: {}'.format(i+1,final))