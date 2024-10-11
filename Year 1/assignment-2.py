#Assignment 2
#Written by: Ryll Santillan

amtOfDataPoints = 0
fertility_data = {}

while amtOfDataPoints < 2:
    data_points_input = input("How many data points do you have? ")
    if int(data_points_input) >= 2:
        amtOfDataPoints = int(data_points_input)
    else:
        print("Must enter at least two data points.")

for i in range(int(amtOfDataPoints)):
    year_input = input("What is the year of data point " + str(i + 1) + "? ")
    fertility_input = input("What is the fertility rate of data point " + str(i + 1) + "? ")

    fertility_data[year_input] = fertility_input

start_year = input("Which year would you like to start with? ")
if fertility_data[start_year]:
    end_year = input("Which year would you like to end with? ")
    if fertility_data[end_year]:
        if int(end_year) > int(start_year):
            avg_fertility = (float(fertility_data[start_year]) + float(fertility_data[end_year])) / 2
            print("The average fertility rate of these two years is %.2f." % float(avg_fertility))
            if float(fertility_data[start_year]) > float(fertility_data[end_year]):
                print("There is a downward trend.") 
            elif float(fertility_data[start_year]) < float(fertility_data[end_year]):
                print("There is an upward trend.") 
            else:
                print("There is a sideways trend.") 
        else:
            print("End year must be after start year.")
    else:
        print("The start year does not exist.")
else:
    print("The start year does not exist.")
