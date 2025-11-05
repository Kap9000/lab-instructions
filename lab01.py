name = input("What is your name")
print ("Hi " + name)
drink = input("what would you like to order ")
meal = input("what meal would you like to order ")
print(name + " heres your order")
print("meal is " + meal)
print ("drink is " + drink)

total_bill = 148.45
tip = .20
sales_tax = .10

total = total_bill + total_bill*tip + total_bill*sales_tax
total = total / 6
print (total) 