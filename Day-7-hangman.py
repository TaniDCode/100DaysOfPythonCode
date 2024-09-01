from random_word import RandomWords

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

stages = ['''
      _______
     |       |
     |      (_)
     |      \|/
     |      / \
     |      
     |
    _|___
 ''', '''
      _______
     |       |
     |      (_)
     |      \|/
     |      / 
     |      
     |
    _|___
 ''', '''
      _______
     |       |
     |      (_)
     |      \|/
     |      
     |      
     |
    _|___
 ''', '''
      _______
     |       |
     |      (_)
     |      \|
     |      
     |      
     |
    _|___
 ''', '''
       _______
     |       |
     |      (_)
     |      
     |       
     |      
     |
    _|___
 ''', '''
       _______
     |      |
     |      
     |      
     |       
     |      
     |
    _|___
 ''']

r = RandomWords()
randword = r.get_random_word()
# print(randword)
randlist = []
for x in randword:
    randlist.append(x)

# print(randlist)

randlistlen = len(randlist)
# print(randlistlen)

print("Word to guess: ", end=" ")
blankspace = []
while randlistlen != 0:
    print("_", end=" ")
    blankspace.append('_')
    randlistlen -= 1

lives = 5
game_over = False
while not game_over:
    userchoice = input('\nGuess a letter: ').lower()

    for y in range(len(blankspace)):
        if userchoice==blankspace[y]:
            print("**********************************You had already correctly chosen this letter before**********************************")

    
    for x in range(len(randlist)):
        if userchoice == randlist[x]:
            blankspace[x] = userchoice

    
    if userchoice not in randword:
        lives -= 1
        print(f"***************************You chose {userchoice} which is not in the word so you loose a life!********************************")
        print(f"************************************{lives}/6******************************************")
        if lives == 0:
            print("*************************************Game Over! You Lose!****************************************")
            print(f"The word to be guessed was {randword}")
            game_over = True

    if randlist == blankspace:
        print("*******************************************You Win!**************************************************")
        game_over = True

    print(stages[lives])

    combinelist = ''.join(blankspace)
    print(combinelist)


