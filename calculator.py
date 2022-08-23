sum = 0
while(True):
    Input = input("Enter the price or press q button to exit ")
    if(Input != "q"):
        sum = sum + int(Input)
        print("The price of each item is: ",sum)

    else:
        print("The total price is: ",sum)
        print("Thank you for shopping with us!!")
        break


