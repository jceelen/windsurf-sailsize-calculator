#! /usr/bin/env python3
#sailsize.py a simple calculator

import sys, csv
if len(sys.argv) < 3:
    print("Usage: python3 sailsize.py [weight in kgs] [windspeed in knots] - print correct sailsize")
    sys.exit()

# Function to round the weight to values available in the table
def myround(x, base=5):
    return int(base * round(float(x)/base))

# Userdata that actually should be asked and stored
my_sails = [4.2, 4.7, 5.3]

# Get Arguements
weight = sys.argv[1]    #first command line arg is the weight in kgs
windspeed = sys.argv[2]   #second command line arg is the windspeed in knots

# Open CSV file and store data
csvfile = open('data/data-sheet-example.csv')
reader = csv.reader(csvfile, delimiter=';')

#TODO lookup column for weight
header = next(reader)
roundedweight = myround(weight)
weight_index = header.index(str(roundedweight))

#TODO lookup row for windspeed and print correct sailsize
for row in reader:
    # define first row column as "value" for testing
    value = row[0]
    # test if value (1st column) is the same as input (windspeed)
    if value == str(windspeed):
        # ...if it is then print the 9th column (with 85kgs) in a certain way
        print('Take this sail: ' +row[weight_index]+ '. Your rounded weight is ' +str(roundedweight)+ ' and the windspeed was ' +str(windspeed))