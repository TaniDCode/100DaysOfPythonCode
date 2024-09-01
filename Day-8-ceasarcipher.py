def encode_decode():
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    direction=input("Type **'encode'** for a encoding a message or **'decode'** for decoding the message.\n").lower()
    print(f"You have chosen to **{direction}** you message")
    message=input(f"Enter the text to be {direction}d.\n").lower()
    shift=int(input("Type the shift number\n"))
    # pos=alphabets.index(x)
    # print(pos)
    
    msglist=[]
    decodemsglist=[]
    restart=False
    
    if direction=='encode':
        for x in message:
            if x not in alphabets:
                msglist.append(x) 
            else:
                # print(f"{x}")
                pos=alphabets.index(x)
                encode=pos+shift
                encode%=len(alphabets)
                # print(pos)
                # print(encode)
                msglistalph=alphabets[encode]
                msglist.append(msglistalph)
                # print(msglist)
            encodemsg=''.join(msglist)
        
        print(f"Here is the encoded result: {encodemsg}")
            
        
    elif direction=='decode':
        for x in message:
            if x not in alphabets:
                decodemsglist.append(x) 
            else:
                # print(f"{x}")
                pos=alphabets.index(x)
                encode=pos-shift
                encode%=len(alphabets)
                msglistalph=alphabets[encode]
                decodemsglist.append(msglistalph)
                    # print(msglist)
            decodemsg=''.join(decodemsglist)
        
        print(f"Here is the dencoded result: {decodemsg}")
encode_decode()

restart=True
while restart:
    userchoice=(input("yes or no")).lower()
    print (f"{userchoice}")
    if userchoice in ['yes']:
        encode_decode()

    if userchoice in ['no']:
        restart=False
        print("End of Ceasar Cipher")
        


        