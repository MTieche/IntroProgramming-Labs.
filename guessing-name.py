def main():
    print('''
      ========================
      ====Guess the Animal====
      ========================
      ''')

    answer="Elephant"
    guess=""
    res=True

    while res==True:
        print("I'm thinking of an animal")
        guess=str(input("Guess the animal:  "))
        if guess!="Elephant":
            print ("Try Again \n")
        else:
            res=False
    print ("Congrats, you have finally got it \n"
       "Took you long enough")
main()

    
