
#1 Write a program that asks the user for a number of a month and then prints out the corr........

month = int(input("Enter month in 1-12 :"))
season = ""

if month in [3, 4, 5]:
    season = "spring"
elif month in [6, 7, 8]:
    season = "summer"
elif month in [9, 10, 11]:
    season = "autumn"
elif month in [12, 1, 2]:
    season = "winter"
else:
    season = "Invalid month"

print(f"It is : {season}.")



#2 Write a program that asks the user to enter names until he/she enters an empty string

names = set()

while True:
    name = input("Enter names: ")

    if name == "":
        break

    if name in names:
        print("Existing Name")

    else:
        print("New Name")
        names.add(name)

print("sorted Names:", sorted(names))



#3 Write a program for fetching and storing airport data. Th......



airports = {}

while True:
    print("Choose an option:")
    print("1. Enter a new airport")
    print("2. Fetch information of an existing airport")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        icao = input("Enter ICAO code of the airport: ").upper()
        name = input("Enter the name of the airport: ")

        if icao in airports:
            print(f"Airport with ICAO code {icao} already exists.")
        else:
            airports[icao] = name
            print(f"Airport {name} with ICAO code {icao} has been added.")

    elif choice == "2":
        icao = input("Enter ICAO code of the airport to fetch: ").upper()

        if icao in airports:
            print(f"The name of the airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print(f"No airport found with ICAO code {icao}.")

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please try again.")

