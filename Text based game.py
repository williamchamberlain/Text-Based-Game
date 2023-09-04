import random 
import time 
import webbrowser #for prize at the end

lives=3
global failed
failed="N"

choice=[]


def generate():
    global choice
    
    choice=[random.randint(1,3),random.randint(1,4),random.randint(1,5),random.randint(1,6),random.randint(1,7)]   #assigns a correct door using  a list 
    print(choice[0])
    print(choice[1])
    print(choice[2])
    print(choice[3])
    print(choice[4])

    
        






print("WELCOME TO THE DUNGEON GAME!!")
time.sleep(1)
name=(input("What is your name adventurer "))
time.sleep(1)
print("Hello "+name+ " your goal ,if you choose to accept it, is to get to the end on the dungeon and recover the lost artifact")
time.sleep(1)
print("You will have to navigate through a sets of random doors (one of them being the correct door )") 
time.sleep(1)     #welcome information
print("However if you get it wrong you will be sent back to the start and you will have to remember the previously chosen doors")
time.sleep(3)
print("each door you get through more doors will appear")
time.sleep(3)
time.sleep(3)
print("Get it wrong 3 times and it's GAME OVER!")
print("LETS COMMENCE!")
generate()



def win():
    print("\n")
    print("\n")
    print("\n")
    time.sleep(1)
    print("Here is the lost aritfact!!!!!!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    webbrowser.open_new("https://www.yout-ube.com/watch?v=xvFZjo5PgG0")
    exit






def powerup1():

    print("\n")

    print("POWERUP TIME!!!!!!!!!!!!!")
    time.sleep(3)
    print("You have a choice "+name)
    time.sleep(3)
    print("In a second if you type y I will give you a number")
    time.sleep(3)
    print("There is a 90 percent chance it is the correct number")            #expalains the powerup
    time.sleep(3)
    accept=input("Would you like the number y/n? ")

    if accept == "y":
        dud=[choice[2],random.randint(1,5)] #generates a randomnumber and puts it in a list with the correct number 
        ratio = [0.9,0.1]       # odds of a number being pick
        power_num=random.choices(dud,ratio)    #picks between the 'dud' list using the 'ratio'
        print("Your number is: ",*power_num)
    else:
        pass
        
        
    

def powerup2():
    global failed
    print("\n")
    time.sleep(3)
    print("ANOTHER POWERUP!")
    time.sleep(3)
    print("Since You are doing well "+name + " I have a proporsiton for you")
    time.sleep(3)
    print("IF you get this one correct you win the game automatically! (no more doors required)")
    time.sleep(3)
    print("(Keep in mind the odds of you winning are getting smaller each door you pick)")
    time.sleep(3)
    print("However if you fail " +name+ " you will be sent back and all doors you have previosuly completed will be randomised again")

    accept=input("So do you accept y/n " )

    if accept == "y":
        gate4=int(input("FOURTH DOOR 1,2,3,4,5,6? "))
        if gate4==choice[3]:
            print("\n")
            print("OMG!!! YOU DID IT YOU WINNNNNN")
            win()
        else:
            print("\n")
            time.sleep(1)
            print("Unfortuantely your gamble did not pay off and you are sent back with all options changed")
            generate()   #generates the numbers again
            failed="Y"  #changes variable so when the loop continues the change will be noticed and the player will be sent back to the start
            
            
            




    else:
        pass



while lives>0:


    time.sleep(0.5)
    

    gate1=int(input("FIRST DOOR 1,2,3? "))  #asking user which door they want to go through
    

    if gate1 ==choice[0]:
        print("Congradulations you can proceed!")
        print("\n")

        time.sleep(1)
        gate2=int(input("SECOND DOOR 1,2,3,4? "))  #proceeds if they choose correct door
        

        if gate2 == choice[1]:
            print("Congradulations you can proceed")
            print("\n")
            time.sleep(1)
            powerup1()                #calls powerup
            time.sleep(1)                                         
            gate3=int(input("THIRD DOOR 1,2,3,4,5? "))

            
            if gate3 == choice[2]:
                print("Congradulations you can proceed")
                print("\n")
                time.sleep(1)
                powerup2()

                if failed == "N":
                    pass
                elif failed == "Y":
                    continue                #this check is for if they fail on the powerup the game resets
                else:
                    pass
                    
                
                gate4=int(input("FOURTH DOOR 1,2,3,4,5.6? "))




                if gate4 == choice[3]:
                    print("Congradulations you can proceed")
                    print("\n")
                    time.sleep(1)
                    gate5=int(input("FITH AND FINAL DOOR 1,2,3,4,5,6,7? "))


                    if gate5 == choice[4]:
                        print("YOU'VE DONE IT!!!")
                        win()

                    else:
                        print("So close yet so far!")
                        lives=lives-1
                        print("Your lives is: ",lives)
                        continue


                
                


                
            


                else:
                    print("Incorrect")                                                                  
                    lives=lives-1
                    print("Your lives is: ",lives)
                    continue
                           

            

            else:
                print("Incorrect")                                                                  
                lives=lives-1
                print("Your lives is: ",lives)
                continue
                






        else:
            print("Incorrect")                                                                  
            lives=lives-1
            print("Your lives is: ",lives)
            continue
            print("\n")



        

    else:
        print("Incorrect")                                                                  
        lives=lives-1
        print("Your lives is: ",lives)
        continue
        print("\n")











    print("Game OVER!")

