def speed():  
    """ Prints the value in MPH if the user input is in KPH and vice versa, along with the average of the numbers in both reading. """

    kph = []    # List for the reading in e (European)
    mph = []    # List for the reading in u (British)
    count = 0
    try:
        # Takes the first user input in the form of u and e.
        user_input = input("\n\tEnter the Next Reading: \n\t" +"->  ").lower()
        if user_input == "":
            print("\tNo readings taken. Nothing to do.")
        elif user_input == "u" or user_input == "e" or user_input[1] =="u" or user_input[1] == "e":
            raise ValueError
        elif user_input[0] == "u":
            print("\n\tReading saved.")
            count += 1
            r = float(user_input[1:])
            mph.append(r)
            r *= 1.6
            kph.append(r) 
            while(True):
                # Takes the user input second time.
                # Runs the loop until nothing is entered by the user.
                user_input2 =  input("\n\tEnter the Next Reading: \n\t" +"->  ").lower()
                if user_input2 == "":
                    break
                elif user_input2 == "u" or user_input2 == "e" or user_input2[1] =="u" or user_input2[1] == "e":
                    raise ValueError
                elif user_input2[0] == "u":
                    print("\n\tReading saved.")
                    count += 1
                    r = float(user_input2[1:])
                    mph.append(r)
                    r *= 1.6
                    kph.append(r) 
                elif user_input2[0] == "e":
                    print("\n\tReading saved.")
                    count += 1
                    r = float(user_input2[1:])
                    kph.append(r)
                    r /= 1.6
                    mph.append(r)
        elif user_input[0] == "e":
            print("\n\tReading saved.")
            count += 1
            r = float(user_input[1:])
            kph.append(r)
            r /= 1.6
            mph.append(r)
            while(True):
                user_input2 =  input("\n\tEnter the Next Reading: \n\t" +"->  ").lower()
                if user_input2 == "":
                    break
                
                elif user_input2[0] == "u":
                    print("\n\tReading saved.")
                    count += 1
                    r = float(user_input2[1:])
                    mph.append(r)
                    r *= 1.6
                    kph.append(r) 

                elif user_input2[0] == "e":
                    print("\n\tReading saved.")
                    count += 1
                    r = float(user_input2[1:])
                    kph.append(r)
                    r /= 1.6
                    mph.append(r)
        else:
            raise ValueError

    # Handles all the value errors
    except ValueError:
        print("\tPlease enter valid input!!")

    # For the result summary
    print("\n\tResults Summary\n")
    if count > 1:
        print(f"\t{count} Readings Analysed.\n")
    else:
        print(f"\t{count} Reading Analysed.\n")
    try:
        # Displays the final results after the user input
        print(f"\tmax: {max(mph):.1f} MPH, {max(kph):.1f} KPH")
        print(f"\tmin: {min(mph):.1f} MPH, {min(kph):.1f} KPH")
        print(f"\tAvg Speed: {sum(mph)/len(mph):.1f} MPH, {sum(kph)/len(kph):.1f} KPH")
    except ValueError:
        print()

# simply a design for the output
print("*************************************************************************************\n".rjust(100))  
print("Swallow Speed Analysis: Version 1.0 \n".rjust(75))
print("*************************************************************************************\n".rjust(100))
# Function call
speed()
