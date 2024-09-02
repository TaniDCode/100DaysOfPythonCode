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