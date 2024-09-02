logo='''
88,dPYba,,adPYba,   ,adPPYba,  8b,dPPYba,   ,adPPYba, 8b       d8  
88P'   "88"    "8a a8"     "8a 88P'   `"8a a8P_____88 `8b     d8'  
88      88      88 8b       d8 88       88 8PP"""""""  `8b   d8'   
88      88      88 "8a,   ,a8" 88       88 "8b,   ,aa   `8b,d8'    
88      88      88  `"YbbdP"'  88       88  `"Ybbd8"'     Y88'     
                                                          d8'      
                                                         d8'       
'''
print(logo)

print("Welcome to the secret auction program.")

bid={}

def bidadd(key,value):
    bid[key]=value

morebidder=True
while morebidder:
    name=input("What is your name?: ")
    bidvalue=int(input("What is your bid?: $"))
    bidadd(key=name,value=bidvalue)
    userchoice=input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if userchoice in ('yes'):
        bidadd(key=name,value=bidvalue)
        print("\n" * 100)
    elif userchoice in ('no'):
        maxvalue=max(bid, key=bid.get)
        print("\n" * 100)
        print(f"The winner is {name} with a bid of ${bidvalue}")
        morebidder=False
