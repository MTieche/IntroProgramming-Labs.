def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'power', 'add', 'mult', 'sub', 'div', and 'quit'.\n")
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
def doLoop():
    result=0
    while True:
        cmd = input("What computation do you want to perform? ")
        if cmd.lower() == "quit":
            break
        while cmd.lower() != "add" or cmd.lower() != "sub" or cmd.lower() != "mult" or cmd.lower() != "div" or cmd.lower() != "power":
            print("Invalid Command. Please try again.")
            cmd = input("What computation do you want to perform? ")
            if cmd.lower() == "add" or cmd.lower() == "sub" or cmd.lower() == "mult" or cmd.lower() == "div" or cmd.lower() == "power":
                break
            break
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if cmd.lower() == "add":
            result = num1 + num2
            break
        elif cmd.lower() == "sub":
            result = num1 - num2
            break
        elif cmd.lower() == "mult":
            result = num1 * num2
            break
        elif cmd.lower() == "div":
            try:
                result = num1 / num2
            except:
                print("Unable to divide by zero")
                result=0
            break
        elif cmd.lower() == "power":
            result = num1 ** num2
            break
    print("The result is ",result, ".\n")
def main():
    showIntro()
    doLoop()
    showOutro()
main()
