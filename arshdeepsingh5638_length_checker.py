#Arshdeep Singh
#8805635
#Date created = 1st Feburary 2022
countryname = True#variable is craded with name countryname which will be looped if user enter wrong input
while countryname == True:#While loop is applied in case of wrong input
    print("Please enter a valid country name")
    userinput = input("")
    if len(userinput) < 2:#len function used to count length of string which user entered whether less then 2
        print("Sorry, country name must be longer than one letter")
        countryname = True
    elif len(userinput) > 20:#len function used to count length of string which user entered whether more then 20
        print("Sorry, country name cannot be more than 20 letters in length")
        countryname = True
    else:
        print("Thanks for giving your input")
        print("You entered" + userinput)#user input will be printed here
        countryname = False
            