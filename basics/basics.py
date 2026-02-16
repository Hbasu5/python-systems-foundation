# BEGINNER BASICS OF PYTHON PROGRAMMING

def run():
    
    #----THE BASIC PRINT EVERYONE STARTS WITH----
    print("Hello World")

    #----SIMPLE MATHEMATICAL OPERATIONS----
    a=5
    print(a)
    print("5+3")
    print(5+3)

    #----A STRING VARIABLE AND DIFFERENT WAYS TO PRINT IT----
    instructor='Hardik Basu'
    print("Python by",instructor)
    print("Python by",instructor,sep='--')

    #----A FOR LOOP TO PRINT NUMBERS FROM 1 TO 10----
    for i in range(1,11):
        print (i)

if __name__ == "__main__":
    run()