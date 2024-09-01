def calculate_love_score(name1,name2):
    counttrue1=0
    countlove1=0
    counttrue2=0
    countlove2=0
    for x in name1.upper():
        if x=='T' or x=='R' or x=='U' or x=='E':
            counttrue1+=1
    for x in name2.upper():
        if x=='T' or x=='R' or x=='U' or x=='E':
            counttrue2+=1
    for x in name1.upper():
        if x=='L' or x=='O' or x=='V' or x=='E':
            countlove1+=1
    for x in name2.upper():
        if x=='L' or x=='O' or x=='V' or x=='E':
            countlove2+=1

    # print (counttrue1)
    # print (counttrue2)
    # print (countlove1)
    # print (countlove2)
    # print(name1)
    # print(name2)
    
           
    truecount=counttrue1+counttrue2
    lovecount=countlove2+countlove1
   
    print(f"{truecount}{lovecount}")
   
   
calculate_love_score(name1="Angela Yu",name2="Jack Bauer")
