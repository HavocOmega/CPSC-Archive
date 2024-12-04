#Assignment 2
#Written by: Ryll Santillan
#UCID: 30257967

# Setup Variables
amtOfDataPoints = 0
fertility_data = {}

# Loop until the inputted amount of data points is greater than or equal to 2 data points
while amtOfDataPoints < 2:
    data_points_input = input("How many data points do you have? ")
    if int(data_points_input) >= 2: #Check if input is greater than or equal to 2
        amtOfDataPoints = int(data_points_input)
    else:
        print("Must enter at least two data points.")

# Query for year and fertility data
while len(fertility_data) < amtOfDataPoints:
    year_input = input("What is the year of data point " + str(len(fertility_data) + 1) + "? ")
    fertility_input = input("What is the fertility rate of data point " + str(len(fertility_data) + 1) + "? ")

    fertility_data[year_input] = fertility_input #Store fertility data by the year in an array (Using an array is super convenient because it allows to override pre-existing values wihtout any extra work)

#Nested if statement hell
start_year = input("Which year would you like to start with? ") #Query for start year
if fertility_data[start_year]: #Check if the input is valid
    end_year = input("Which year would you like to end with? ") #Query for the end year
    if fertility_data[end_year]: #Check if the input is valid
        if int(end_year) > int(start_year): #Check if end year is after start year
            avg_fertility = (float(fertility_data[start_year]) + float(fertility_data[end_year])) / 2 #Calculate average fertility
            print("The average fertility rate of these two years is %.2f." % float(avg_fertility)) #Print average fertility
            if float(fertility_data[start_year]) > float(fertility_data[end_year]): #Check if the fertility data for the start year is greater than the end year
                print("There is a downward trend.") 
            elif float(fertility_data[start_year]) < float(fertility_data[end_year]): #Check if the fertility data for the start year is less than the end year
                print("There is an upward trend.") 
            else: #If trend is neither upward nor downward then it's sideways
                print("There is a sideways trend.") 
        else:
            print("End year must be after start year.")
    else:
        print("The end year does not exist.")
else:
    print("The start year does not exist.")
