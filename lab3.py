import random                                                            #package for generating random number in given range
import math                                                              #package for using mathematical formulas
x =int(input("enter the range of X co-ordinates"))
y= int(input("enter the range of Y co-ordination"))
XL= random.sample(range(0,50),10)                                       #enter 10 random number in range 0 to 50
YL = random.sample(range(0,10),10)                                      #enter 10 random number in range 0 to 10

print(XL)
print(YL)

temp = []                                                               #temporary list to store the value of distance formula
for i in range(len(XL)):                                                #for loop to display the XL values in tabular form
    print(i+1,end="          ")
print("\n")
for i in range(len(XL)):                                                #for loop to display the YL values in tabular form                          
    print(i+1,end=" ")
    d = []                                                              # d list stores the value of distances between all the nodes 
    for j in range(len(YL)):
        d.append(math.sqrt((XL[i]-XL[j])**2+ (YL[i]-YL[j])**2))         #euclidian distance formula between two nodes
    temp.append(d)
    
    for k in d:
       print("%.5f"%k,end="     ")
    print("\n")
    
a= float(input("Enter the range for the Neighbour: "))                  #prompting the user to enter the value from which neighbour table constructed
b=0
for i in range(len(XL)):                                                #Making the neighbour table
    print("\n")
    print("The Neighbours"" "+str(i+1)+" ""are:",end="")
    for j in range(len(YL)):
       if temp[i][j]<=a:
          b = temp[i][j]
          print("{0}{1}".format(j+1,b))