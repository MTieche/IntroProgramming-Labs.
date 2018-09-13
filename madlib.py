def promptForWords():
    global Noun, Verb, Adjective, Place 
    Noun=str(input("Enter a noun:  "))
    Verb=str(input("Enter a verb:  "))
    Adjective=str(input("Enter an adjective:  "))
    Place=str(input("Enter a place:  "))
    
def makeAndPrintSentence():
    Sentence = ("Take your " + str(Adjective) + " " + str(Noun) + " and " + str(Verb) + " it at the " + str(Place) + "!")
    print (Sentence)
    
def main():
    promptForWords()
    makeAndPrintSentence()
    
main()
