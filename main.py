def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
        #print("Leap year.")
      else:
        return False
        #print("Not leap year.")
    else:
      return True
      #print("Leap year.")
  else:
    return False
    #print("Not leap year.")

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year) == True:
      return month_days[month-1] + 1
  else:
    return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
while month > 12 or month < 1:
  if month > 12:
    print("You entered month greater than 12. Enter again.")
  if month < 1:
    print("You entered month less than 1. Enter again.")
  month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












