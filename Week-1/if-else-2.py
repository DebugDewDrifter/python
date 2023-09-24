#To check whether the year entered is leap
year = int(input("Enter Year: "))
if (year%4==0) and (year%100!=0):
  print("{0} is leap year".format(year))
else:
  print("{0} is not leap year".format(year))


# Odd Or Even Checker
Number = int(input("Enter Number: "))
if Number%2==0:
  print(f"{Number} Is Even")
else:
  print(f"{Number} Is Odd")


# Prime Number Checker
Number = int(input("Enter Number: "))
if Number%Number==0 and Number%2!=0:
  print(f"{Number} Is Prime Number")
else:
  print(f"{Number} Is Not A Prime Number")
