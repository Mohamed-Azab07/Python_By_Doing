import sys
from datetime import datetime


args = sys.argv

if len(args) != 3:
    print("Usage: python scriptname.py MM-DD-YYYY MM-DD-YYYY")
else:
    start_date = args[1]
    end_date = args[2]


    start_date = datetime.strptime(start_date, "%m-%d-%Y")
    end_date = datetime.strptime(end_date, "%m-%d-%Y")


    difference = end_date - start_date
    days = difference.days

    print(f"The difference in days is {days}")
