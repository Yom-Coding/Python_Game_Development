Country_DB = {}

while True:
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")

    Choice = int(input("Enter an option: "))

    if Choice == 1: 
        country = input("Enter a country: ").upper()
        capital = input("Enter a capital: ").upper()
        Country_DB[country] = capital

    if Choice == 2: 
        list_data = list(Country_DB.keys())
        print(list_data)

    if Choice == 3: 
        list_data1 = list(Country_DB.values())
        print(list_data1)

    if Choice == 4: 
        country = input("Enter a country: ").upper()
        print(Country_DB[country])

    if Choice == 5: 
        key = input("Which Key do you want to delete: ").upper()
        del Country_DB[key]

    else: 
        print("Please Enter A Valid Choice")
