import sys
def main():
    print('''
      ========================
      ====Guess the Animal====
      ========================
      ''')

    answer="elephant"
    guess=""
    res=True

    while res==True:
        print("I'm thinking of an animal")
        guess=str(input("Guess the animal:  "))
        if guess[:1] == "q" or guess[:1] == "Q":
            print ("Goodbye")
            sys.exit()
        elif guess.lower() != "elephant":
            print ("Try Again \n")  
        else:
            res=False
    print ("Congrats, you have finally got it \n"
       "Took you long enough")
    likeness=str(input("Do you like elephants: (Yes or No)  "))
    if likeness[:1] == "y" or likeness[:1] == "Y":
        print ("Good.")
    else:
        print ("I am disappointed")
main()

    
