try :
     num1 = int(input("Enter a number: "))
     num2 = int(input("Enter a number: "))
     result = num1/num2
     print("result is : ",result)
     print("result is : ",result1)

except ZeroDivisionError:
     print("division by 0 is not allowed")
except ValueError:
     print("Enter a numaricle value")
except NameError as ex:
     print("the exeption is: ",ex)
except:
     print("some error occured")
finally:
     print("I will exicute no matter what happens")