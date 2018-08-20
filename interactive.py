import datetime

name = str(input("whats your name?: ")) #get user name input

print("\033c") #clear screen
print("great",name,",what would you like to do today,select option below?")
longtext = "1. What is the date today?\n2. What is the temperature today?\n3. Tell me a quote\n4. Open facebook\n"
print(longtext)
option = int(input("enter your option: "))

if option == 1:
    print("\033c")
    now = datetime.datetime.now()
    time_now = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    print(time_now)
elif option == 2:
    print("\033c")
    w = str(input("your location ?: "))
    from weather import Weather, Unit
    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location(w)
    condition = location.condition
    print("The weather at ",w," is ",condition.text)
elif option == 3:
    print("\033c")
    import csv
    with open('listmotivation.csv', newline='') as f:
        reader = csv.reader(f)
        quotes = []
        for row in reader:
            quote = row[0]
            quotes.append(quote)
        maxArrayQuotes = len(quotes)

        from random import *

        x = randint(1, maxArrayQuotes)

        print(quotes[x])
elif option ==4:
    import webbrowser
    url = 'https://facebook.com'

    webbrowser.open(url)
else:
    exit()


