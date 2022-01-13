# Created a function
def yes_no():
    """ If you can answer the 4 questions correctly then you win the game. """

    while(1):

        # Simply a design for output
        print("*************************************************************************************\n".rjust(100))
        print("Stop! Who would cross the Bridge of Death\n".rjust(64))

        print("Must answer me these questions three, 'ere the other side he see. \n".rjust(89))
        print("*************************************************************************************\n".rjust(100))

        # For the user input (user name)
        name = input("\n\t 1.) What is your name?\n\t" + " ->  ").lower()               
        
        # Checks if the user name is arthur 
        if name == "arthur":
                print("\n\t My liege! You may pass!\n")
                break
        else:
            quest = input("\n\t 2.) What is your quest? \n\t" + " ->  ")

            # checks the word grail is in the user input
            if "grail" not in quest:                                                        
                print("\n\t Only those who seek the Grail may pass.\n")
                break

            else:
                colour = input("\n\t 3.) What is your favourite colour?\n\t" + " ->  ") 

                # For the confirmation of the first letter of the color matches with the first letter of the user's name         
                if colour[0] == name[0]:
                    print("\n\t You may pass!\n")
                    break

                else:
                    print("\n\t Incorrect! You must now face the Gorge of Eternal Peril.\n")
                    break
# Function call
yes_no()