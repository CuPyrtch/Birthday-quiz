"""
birthday.py
Author: CuPyrtch
Credit: None
Assignment: Birthday-quiz

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todayday = datetime.today().day
todaymonthname = month_name[todaymonth].lower()

name = input("Hello, what is your name?")
month = input("Hello " + name + ", what was the name of the month you were born in?").lower()
year = input("And what year were you born in, " + name + "?")
daystr = input("And the day?")
day = int(daystr)

if month == "october" and day == 31:
    print("You were born on Halloween!")
elif month == todaymonthname and day == todayday:
    print("Happy birthday!")
else:
    if int(year) >= 2000:
        era = "two thousands"
    elif int(year) >= 1990:
        era = "nineties"
    elif int(year) >= 1980:
        era = "eighties"
    elif int(year) < 1980:
        era = "Stone Age"
    
    if month in ["december","january","february"]:
        season = "winter"
    elif month in ["march","april","may"]:
        season = "spring"
    elif month in ["june","july","august"]:
        season = "summer"
    elif month in ["september","october","november"]:
        season = "fall"
    else:
        season = "idk"
        
    print(name + ", you are a " + season + " baby of the " + era + ".")





