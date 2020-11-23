def getInput():
    tool = input("What do you want me to get?  ")

    if(tool=="wrench"):
        print("If you can dodge a wrench you can dodge a ball!")
        x=1
    
    elif(tool=="hammer"):
        print("It's hammer time!")
        x=2
    
    elif(tool=="screws"):
        print("Screw you!")
        x=3
    
    elif(tool=="bolts"):
        print("Its time to bolt!")
        x=4
    
    else:
        print("I've got no idea what you're talking about.")
        x=0
    
    return (x)
