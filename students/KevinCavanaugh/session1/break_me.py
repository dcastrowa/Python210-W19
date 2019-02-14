# --------------------------------------- #
# Title: Assignment 1: Break_me
# Change Log: (who, when, what)
# kcavanaugh, 2019-01-13, created file
# --------------------------------------- #

def nameerror ():
    name = input("Enter your name:")
    print("Your name is", nama)

def typeerror ():
    number = len(int(input("Enter your favorite number:")))
    print("Your name is", number)

#def syntaxerror ():
#    name = innput("Enter your name:"")
#    print("Your name is", name)

def attributeerror ():
    name = str(input("Enter your name:"))
    print(sum(name))



#nameerror()
#typeerror()
#syntaxerror()
attributeerror()
