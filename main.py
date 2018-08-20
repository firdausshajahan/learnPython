import datetime
import csv
from random import *

def optM():
    opt = input("return to main menu ? Type 'Y' to return,or 'N' to exit: ")
    if opt == 'yes':
        main(name)
    elif opt == 'Yes':
        main(name)
    elif opt == 'y':
        main(name)
    elif opt == 'Y':
        main(name)
    else:
        print("\033c")
        exit()

def opt1():
    print("\033c")
    #import datetime
    now = datetime.datetime.now()
    time_now = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    print(time_now)
    optM()

def opt2():
    print("\033c")
    w = str(input("your location ?: "))
    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(w)
    condition = location.condition
    print("The weather at ",w," is ",condition.text)
    optM()

def opt3():
    print("\033c")
    #import csv
    with open('listmotivation.csv', newline='') as f:
        reader = csv.reader(f)
        quotes = []
        for row in reader:
            quote = row[0]
            quotes.append(quote)
        maxArrayQuotes = len(quotes)
        #print(len(quotes))
        x = randint(1, maxArrayQuotes)

        print(quotes[x])
    optM()

def main(n):
    print("\033c")
    print("great",n,",what would you like to do today,select option below?")
    longtext = "1. What is the date today?\n2. What is the temperature today?\n3. Tell me a quote\n4. Open facebook\n"
    print(longtext)
    option = int(input("enter your option: "))

    if option == 1:
        opt1()
    elif option == 2:
        opt2()
    elif option == 3:
        opt3()
    elif option ==4:
        print("\033c")
        import webbrowser
        url = 'https://facebook.com'

        webbrowser.open(url)
        optM()
    else:
        exit()

name = str(input("whats your name?: ")) #get user name input
main(name)
print("\033c") #clear screen
