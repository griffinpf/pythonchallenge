#################################################################
#Challenge 15: http://www.pythonchallenge.com/pc/return/uzi.html#
#################################################################

# The year is 1XX6 and it's a leap year
import calendar
import datetime

years = []
date = datetime.datetime.strptime('01/01/1016','%m/%d/%Y')

leapyears = []
while date < datetime.datetime.now():
    if calendar.isleap(date.year) == True:
        leapyears.append(date.year)
    date = date.replace(year=date.year+1)

# We also know that Jan 26 is a Monday, so look for all leap years that qualify

for year in range(1006,1996,10):
    if datetime.date(year, 1, 26).isoweekday() == 1:
        if year in leapyears:
            print(datetime.date(year, 1, 26))

# The HTML clue says he's not the youngest, but the second, so the date we're looking for
# is 1/26/1756. The HTML clue also says to buy flowers for tomorrow, so we're looking for
# someone related to 1/27/1756. This is Mozart's birthday.