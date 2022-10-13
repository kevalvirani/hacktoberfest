print ("MENU")
print ()
print ("B - Burger ")
print("F - French Fries")
print("P - Pizza ")
print("S - Sandwich")
print ()
Burger= 0
FrenchFries= 0
Pizza= 0
Sandwich= 0

x=1

while x==1:
    i = input("Enter the food that you want to buy: ")
    if i  == "B":
        Burger+=200
        print ("Burger ------------Php. 200.00")
    elif i == "F" :
        FrenchFries+=50
        print ("FrenchFries ------------Php. 50.00")
    elif i == "P":
         Pizza+=500
         print ("Pizza ------------Php. 500.00")
    elif i == "S":
         Sandwich+=150
         print ("Sandwich ---------Php. 150.00")
    x=int(input("Do you still want to buy anything? 1 if yes 0 if no "))
total= Burger + FrenchFries + Pizza + Sandwich   
print("Total: ", total)
