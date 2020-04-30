from random import *
i = 0
z = 0

while i < 10:
  divorce=str(input("would you want to file for divorce? : "))
  if divorce == "yes":
    spouse=str(input("who would you like to divorce? : "))
    cost=randint(10000, 100000)
    divCost=str(cost)
    print("--")
    print("you have divorced " + spouse + " with a price of $" + divCost)
    print("--")
  else:
    z = 0
    print("no divorce then")

  print(" ")
  stopPGRM=str(input("would you like to stop the program? : "))
  if stopPGRM == "yes":
    i = 10
  if stopPGRM == "no":
    print(" ")
    continue
  else:
    print("please input yes or no")
    print("rerunning Code")
    print(" ")
    continue