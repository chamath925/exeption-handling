try :
    num = int(input("Enter your number : "))
    print(num)
except ValueError as ex :
    print("exeption: ",ex)

print("I'm outside the try block")