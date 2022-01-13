import re
from random import choice
import datetime


def time():
    """ Prints the current date/time. """
    return datetime.datetime.now()      # handles the current datetime. 

def bot_data(z):
    """ For the response of the chat bot towards the user asked questions. """
    
    print(f"\nHow may I help you?")
    while (True):
        # For the user input.
        user_input2 = input(f"\n{user} -> ").lower()
        e = ["end", "stop","exit","pause","bye"]

        # Conditional statements for the bots response.
        # Bot gives different response choosing from the list that has been provided.
        if "library" in user_input2 or "libraries" in user_input2:
            a = ["The library is closed today.", "The library opens at 11 am till 6pm.", "The library is still open."]
            print(f"{z} -> {choice(a)}")

        elif "wifi" in user_input2:
            b = ["WiFi is excellent across the campus.", "WiFi is very slow.", "There is no internet access."]
            print(f"{z} -> {choice(b)}")

        elif "deadline" in user_input2 or "submission" in user_input2 or "last date" in user_input2 or "due date" in user_input2:
            c = ["Your deadline has been extended by two working days.", "You have only two days for the submission.",
                "It seems like you have many days left."]
            print(f"{z} -> {choice(c)}")

        elif "date" in user_input2 or "time" in user_input2 or "year" in user_input2 or "month" in user_input2:
            print(f"{z} -> {time()}")

        elif "coffee" in user_input2 or "tea" in user_input2:
            d = ["The cafe opens at 9am till 9pm."]
            print(f"{z} -> {choice(d)}")

        elif "dinner" in user_input2 or "food" in user_input2 or "lunch" in user_input2 or "snacks" in user_input2 or "snack" in user_input2:
            e = ["The food isn't prepared yet.", "The food is ready. Wash your hands before eating.", 
                "It seems to be not ready yet. How about eating outside?", 
                "The newly opened restaurant has a high rating wanna try grab something?"]
            print(f"{z} -> {choice(e)}")

        elif "call" in user_input2 or "contact" in user_input2:
            f = ["You have low balance, cannot call anyone right now.", "Cannot make a call because of the low network."]
            print(f"{z} -> {choice(f)}")

        elif "movie" in user_input2 or "film" in user_input2 or "cinema" in user_input2:
            g = ["The ticket is available online.", "How about you try Spiderman: No Way Home.",
                "The QFX opens at 7am till 7pm", "All the tickets are out of stock"]
            print(f"{z} -> {choice(g)}")

        elif "hi" in user_input2 or "hello" in user_input2:
            h = [f"Hello, {user}.", f"Well hello there, {user}.", f"A fine greetings, {user}."]
            print(f"{z} -> {choice(h)}")

        elif "how are you" in user_input2 or "how do you do" in user_input2:
            print(f"well how generous of you {user}, I'm good.")

        elif user_input2 in e:
            print(f"Thanks, {user} for using PopChat. See you again soon!")
            break   
        # Response of the bot if the user asked question is not available.
        else:
            i = ["Hmmmm.", "Tell me more.", "Sorry, cannot find what you are looking for.",
                "How about trying something else.", "I don't think i understand."]
            print(f"{z} -> {choice(i)}")
            continue

def bot_config(user):
    """ For the bot configuration. """

    bots = ["Lumine", "Aether", "Alexa", "Jesus", "Yunjin"]    # Name for the working bots
    z = choice(bots) 
    # For the output design.                   
    print("\n**********************************************************")
    print(f"\nHi, {user}! Thank you, and Welcome to PopChat! \nMy name is {z}, and it will be my pleasure to help you.")
    print("\n**********************************************************")
    # For raising network error
    networks = ["n", "o"]
    if choice(networks) == "n":
        print("\n***Network Error***")
        print(f"Thanks, {user} for using PopChat. See you again soon!")
    else:
        bot_data(z)

# For the ouput design.
print("\t\t_________________________________________________________________________________________________________________\n")
print("Welcome to Pop Chat, \n".rjust(80))
print("One of our operators will be pleased to help you today.\n".rjust(100))
print("\t\t_________________________________________________________________________________________________________________\n")

# Email address confirmation/requirements
user_input = input("\n\nPlease enter your Poppleton email address\n" + "->  ")
regex  = re.compile(r"([A-Za-z0-9]{2,15}[.-_]*[A-Za-z0-9]*){2,15}@pop.ac.uk")
if re.fullmatch(regex, user_input):
    user = user_input.split("@")[0]
    bot_config(user)
else:
    print(f"{user_input} is invalid at pop.ac.uk.")