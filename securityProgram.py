known_users = ["Adam","Bob","Travis","Jack","Rob","Dimitri","Abby"]



while True:
    print("Hi! My name is Travis")
    name = input("what is your name?: ").strip().capitalize()

    if name in known_users:
        print("welcome back {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").lower()
#if the user enters the correct value 
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
             print("No problem, I didn't want you to leave anyway!")
#if we dont have the name in the array ' known_users ' play this logic             
    else:
        print("hmmm I dont think I have met you yet {}".format(name))
        add_me = input("would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":            
            known_users.append(name)
        elif add_me == "n": 
            print("no worries, see you around bud..")
        
