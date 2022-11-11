#Lucas Wenger
#9/2/2022
#Quarterly Review Calculator (Non-Leap Years)

import sys

class Month:
    def __init__(self, monthname, monthnum, numofdays, daysinyear):
        self.monthname = monthname
        self.monthnum = monthnum
        self.numofdays = numofdays
        self.daysinyear = daysinyear

#Instances
Jan = Month("January", 1, 31, [x for x in range(0,31)]) #0 - 30
Feb = Month("February", 2, 28, [x for x in range(31,59)]) #31 - 58
Mar = Month("March", 3, 31, [x for x in range(59,90)]) #59 - 89
Apr = Month("April", 4, 30, [x for x in range(90,120)]) #90 - 119
May = Month("May", 5, 31, [x for x in range(120,151)]) #120 - 150
Jun = Month("June", 6, 30, [x for x in range(151,181)]) #151 - 180
Jul = Month("July", 7, 31, [x for x in range(181,212)]) #181 - 211
Aug = Month("August", 8, 31, [x for x in range(212,243)]) #212 - 242
Sep = Month("September", 9, 30, [x for x in range(243,273)]) #243 - 272
Oct = Month("October", 10, 31, [x for x in range(273,304)]) #273 - 303
Nov = Month("November", 11, 30, [x for x in range(304,334)]) #304 - 333
Dec = Month("December", 12, 31, [x for x in range(334,365)]) #334 - 364

months = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

def isvaliddate(month, day):
    '''
    Checks whether a given date is valid. 
    '''
    #Month and day entered as strings.
    if not month.isdigit() or not day.isdigit():
        return False
    else:
        month = int(month)
        day = int(day)
    if month not in [m.monthnum for m in months]:
        return False
    for m in months:
        if m.monthnum == month:
            if day < 0 or day > m.numofdays:
                return False
    return True

def datetonum(numtup):
    '''
    Take a month and a day and converts it to the numbered day of the year (e.g., 2,1 converts to 31). 
    '''
    #Month and day entered as a tuple of integers. 
    for i in months:
        if numtup[0] == i.monthnum:
            return i.daysinyear[numtup[1]-1]
    raise Exception("ERROR: Not a valid month -- problem with code.")

def numtodate(num):
    '''
    Take a numbered day of the year and converts it to month and day (e.g., 31 converts to (2,1)). 
    '''
    #Num entered as integer.
    for i in months:
        if num in i.daysinyear:
            return (i.monthnum,i.daysinyear.index(num)+1)
    raise Exception("ERROR: Not a valid day -- problem with code.")

def correctdate(numtup):
    '''
    If the date is not a real date, correct it by making it overflow into the next month.
    '''
    truemonth = numtup[0]
    trueday = numtup[1]
    if not isvaliddate(str(numtup[0]),str(numtup[1])):
        if truemonth > 12:
            truemonth -= 12
        for i in months:
            if truemonth == i.monthnum:
                if trueday > i.numofdays:
                    truemonth += 1
                    trueday -= i.numofdays
    return (truemonth,trueday)

def getmonthname(monthnum):
    '''
    Replaces the number of a month with its name.
    '''
    for i in months:
        if monthnum == i.monthnum:
            return i.monthname

title = '''▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄░█░██░█░▄▄▀█░▄▄▀█▄░▄█░▄▄█░▄▄▀█░██░██░████░▄▄▀█░▄▄█▀███▀█░▄▄██▄██░███░████░▄▄▀█░▄▄▀█░██▀▄▀█░██░█░██░▄▄▀█▄░▄█▀▄▄▀█░▄▄▀
██░██░█░██░█░▀▀░█░▀▀▄██░██░▄▄█░▀▀▄█░██░▀▀░████░▀▀▄█░▄▄██░▀░██░▄▄██░▄█▄▀░▀▄████░████░▀▀░█░██░█▀█░██░█░██░▀▀░██░██░██░█░▀▀▄
██▄▄░▀██▄▄▄█▄██▄█▄█▄▄██▄██▄▄▄█▄█▄▄█▄▄█▀▀▀▄████░██░█▄▄▄███▄███▄▄▄█▄▄▄██▄█▄█████░▀▀▄█▄██▄█▄▄██▄███▄▄▄█▄▄█▄██▄██▄███▄▄██▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀'''
print(title)

while True:
    user = ''
    month = ''
    day = ''
    print("Welcome to the Quarterly Review Calculator! How may I help you?\n")
    print("1. Calculate quarterly review date ranges")
    print("2. Quit")

    while user not in ["1","2"]:
        user = input("\nPlease enter \"1\" or \"2\".\n")
    
    if user == "1":
        while not isvaliddate(month, day):
            print("\nPlease enter a valid date:")
            month = input("What is the number of the month of the due date?\n")
            day = input("What is the number of the day of the due date?\n")
        #Date is valid -- format into a tuple of integers
        deadlineone = (int(month),int(day))
        #Get pastdeadlineone (30 days before due date)
        pastdeadlineone = numtodate((datetonum(deadlineone)-30)%365)
        #Get futuredeadlineone (15 days after due date)
        futuredeadlineone = numtodate((datetonum(deadlineone)+15)%365)
        #Get Q2 dates
        deadlinetwo = correctdate((deadlineone[0]+3,deadlineone[1]))
        pastdeadlinetwo = numtodate((datetonum(deadlinetwo)-30)%365)
        futuredeadlinetwo = numtodate((datetonum(deadlinetwo)+15)%365)
        #Get Q3 dates
        deadlinethree = correctdate((deadlinetwo[0]+3,deadlinetwo[1]))
        pastdeadlinethree = numtodate((datetonum(deadlinethree)-30)%365)
        futuredeadlinethree = numtodate((datetonum(deadlinethree)+15)%365)
        #Get Q4 dates
        deadlinefour = correctdate((deadlinethree[0]+3,deadlinethree[1]))
        pastdeadlinefour = numtodate((datetonum(deadlinefour)-30)%365)
        futuredeadlinefour = numtodate((datetonum(deadlinefour)+15)%365)
        #Output dates
        output = f'''
QUARTER 1 DEADLINE RANGE:

As Early As: {getmonthname(pastdeadlineone[0])} {pastdeadlineone[1]}
DUE DATE: {getmonthname(deadlineone[0])} {deadlineone[1]}
No Later Than: {getmonthname(futuredeadlineone[0])} {futuredeadlineone[1]}

QUARTER 2 DEADLINE RANGE:

As Early As: {getmonthname(pastdeadlinetwo[0])} {pastdeadlinetwo[1]}
DUE DATE: {getmonthname(deadlinetwo[0])} {deadlinetwo[1]}
No Later Than: {getmonthname(futuredeadlinetwo[0])} {futuredeadlinetwo[1]}

QUARTER 3 DEADLINE RANGE:

As Early As: {getmonthname(pastdeadlinethree[0])} {pastdeadlinethree[1]}
DUE DATE: {getmonthname(deadlinethree[0])} {deadlinethree[1]}
No Later Than: {getmonthname(futuredeadlinethree[0])} {futuredeadlinethree[1]}

QUARTER 4 DEADLINE RANGE:

As Early As: {getmonthname(pastdeadlinefour[0])} {pastdeadlinefour[1]}
DUE DATE: {getmonthname(deadlinefour[0])} {deadlinefour[1]}
No Later Than: {getmonthname(futuredeadlinefour[0])} {futuredeadlinefour[1]}

'''
        print(output)
    if user == "2":
        print("\nGoodbye.\n")
        sys.exit()
