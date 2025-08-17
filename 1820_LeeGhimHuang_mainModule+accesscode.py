def mainMenu():
    gameCon = [' ','ROLL THE DICE', 'GUESS A COLOUR', 'MUSICAL CHAIR', 'HANGMAN'] # declare array
    print("--------------MENU--------------")
    for i in range(1,len(gameCon)): #automatic loop 
        print(i,gameCon[i]) #to print content in array
    while True:    
        gameIn = str(input("Choose a game to play : ")) #to get user input for which game
        if gameIn =='1': # if structure for choose game to play
            goGame = str(input("Press '1' to continue this game :")) #get input if user want to continue play the game
            if goGame == '1' : # if structure for continue play
                rollDice() #go to function
                break
            else:
                mainMenu() #go to function
                break
            break
        
        if gameIn =='2':
            goGame = str(input("Press '1' to continue this game :")) #get input if user want to continue play the game
            if goGame == '1' :# if structure for continue play
                guessColor() #go to function
                break
            else:
                mainMenu() #go to function
                break
            break
            
        if gameIn =='3':
            goGame = str(input("Press '1' to continue this game :")) #get input if user want to continue play the game
            if goGame == '1' :# if structure for continue play
                musicChair() #go to function
                break
            else:
                mainMenu() #go to function
                break
            break
            
        if gameIn =='4':
            goGame = str(input("Press '1' to continue this game :")) #get input if user want to continue play the game
            if goGame == '1' :# if structure for continue play
                print("hang") #go to function
                break
            else:
                mainMenu() #go to function
                break
            break

        if gameIn != '1' or gameIn != '2' or gameIn != '3' or gameIn != '4' : # if structure of the invalid input
            print("INVALID INPUT !!!\nPlease enter valid input")
            print("--------------MENU--------------")
            print("(1) ROLL THE DICE")
            print("(2) GUESS THE COLOUR")
            print("(3) MUSICAL CHAIR")
            print("(4) HANGMAN")
            continue
            break

Chance = 3 # delcare change
Password = "higame" #delcare password
import getpass 
while True:
    getPass = getpass.getpass("Enter valid password :") #get password input with not display the input
    if Password == getPass: #check the password
        print("-------------Welcome-------------")
        break
    else:
        Chance = Chance - 1 #reduce change
        print (getPass) #print invalid input 
        if Chance > 0 : #check the change 
            print("Chance(s) left :", Chance, "\nPlease enter correct password")
            continue
            break
        break
    if Password == getPass or Chance == 0: #go out the loop if condition correct
        break
if Password == getPass: #check password
    mainMenu() #go to function
    print("Thanks for playing\nCome play again")
    
if Chance == 0: #check change
    print("Chance(s) left :", Chance, "\nNo more chance to enter password\nHave better try next time")
