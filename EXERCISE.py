

while True:
    print("Enter the operation you want to follow- MULTIPLY,DIVIDE,ADDITION or SUBTRACTION")

    x = input()
    if x=='MULTIPLY':
        print("Enter two numbers to multiply")

        while True:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                break
            except:
                print("Enter a valid number")
        if (a, b) == (45, 3) or (b, a) == (45, 3):
            print(555)
        elif (a, b) != (45, 3):
            print(a * b)




    elif x=='DIVIDE':
        print("Enter two numbers to divide")

        while True:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                break
            except:
                print("Enter a valid number")
        if (a, b) == (56, 6) or (b, a) == (56, 6):
            print(4)
        elif (a, b) != (56, 6):
            print(a / b)









    elif x=='ADDITION':
        print("Enter two numbers to add")

        while True:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                break
            except:
                print("Enter a valid number")
        if (a, b) == (56, 9) or (b, a) == (56, 9):
            print(77)
        elif (a, b) != (56, 9):
            print(a + b)


    elif x=='SUBTRACTION':
        print("Enter two numbers to subtact")
        while True:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                break
            except:
                print("Enter a valid number")


        print(a - b)


    elif x=="exit":
        quit()
    else:
        print("Enter a valid operation")
        continue
    print("Type 'exit' to exit the calculator")









   # if (a, b) == (45, 3):
        #print(555)
   # if (a, b) != (45, 3):
        #print(a * b)
      #  if x !='MULTIPLY':
         #   print("Enter a valid operation")










#if x=='ADDITION':
   #print("Enter two numbers to add: ")
   # int(input(a,b))
#else:
   # print("Enter a valid operation")
#if (a,b)==(56,9):
    #print(77)
#elif (a,b)!=(56,9):
   # print(a+b)
#else:
    #print("Please enter valid numbers")



#if x=='SUBTRACTION':
    #print("Enter two numbers to subtact")
#    int(input(a,b))
#else:
   # print("Enter a valid operation")
#if (a,b)==():
  #  print(a-b)
#else:
   # print("Please enter an valid numbers")

