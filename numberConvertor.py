#Name: Ibrahim Salisu #123
#numberconvertor.py

# a) Main Function Definition



def numberconvertor():
 
   
        print("""
              CHOOSE AN OPTION BELOW (1,2 or 3)
              1. converting a decimal number to binary
              2. converting a decimal number to hexadecimal
              3. exit the program.""")
        
        userOption = int(input())
        
        if(userOption==1):
                decimal = int(input("Enter a number between 0-1000\t"))
                #definiing decimalToBinary using recursion
                def decimalToBinary(decimal):
                    #base case:
                    if(decimal==0):
                        return 
                    else:
                        # recursive case
                        decimalToBinary(int(decimal/2))
                        print(decimal%2, end="")
                if(decimal>1000):
                     print("The decimal number entered is outside the given range")
                else:
                    print("The decimal number "+str(decimal)+" is in range\nThe binary number of "+str(decimal)+" is")
                    decimalToBinary(decimal)
                        
            
        elif(userOption==2):
            decimal = int(input("Enter a number between 0-1000\t"))

            def convertDigitToHex(decimal):
                if decimal < 10:
                    return str(decimal)
                elif (decimal == 10):
                    return 'A'
                elif (decimal == 11):
                    return 'B'
                elif (decimal == 12):
                    return 'C'
                elif (decimal == 13):
                    return 'D'
                elif (decimal == 14):
                    return 'E'
                elif (decimal == 15):
                    return 'F'
                
                def decimalToHex():
                    
                
                    remaining_digits = decimal // 16
                    remainder       = decimal % 16

                    if remaining_digits == 0:
                        return decimalToHex(remainder)
                    else:
                        return decimalToHex(remaining_digits) + convertDigitToHex(last_digit)
               

        
        else:
            exit()
            
            
        
      
numberconvertor()
 