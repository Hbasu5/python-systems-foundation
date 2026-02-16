# While-Loop, Squaring + Odd/Even + Try/Catch

def new(d):
            
        output=d*d
        if(output%2==0):
            output1='even'
        else:
            output1='odd'

        return output,output1
def run():

    while(True):

        try:
            n=int(input("Enter a number ")) 
        except ValueError:
            print("Enter a number, previous input did not qualify.")
            continue

        output,output1 = new(n)

        print(f"The square of the number is {output}\nThe number is {output1}")

        c=input("Do you want to continue Y/N? ")
        if(c.lower()=='y'):
            continue
        elif(c.lower()=='n'):
            print("You chose to exit.")
            break
        else:
            print("Wrong Choice. Exiting")
            break
if __name__ == "__main__":
    run()