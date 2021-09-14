from statistics import mean
import datetime
import csv

def weather(date, location):
    # Attempt to convert the given date string to a datetime object
    try:
        targetDate = datetime.datetime.strptime(date, '%d-%m-%Y') # Convert date string to datetime
    except:
        return (None, None) # Return empty tuple if date is in an invalid format
    minTemps = [] # List of min temps on each date at the given location
    maxTemps = [] # List of max temps on each date at the given location
    targetData = {} # Store the min and max temps on the given date at the given location
    with open('weatherAUS.csv', newline='') as csvfile:
        dataLines = csv.reader(csvfile)
        csvfile.readline() # Skip header line of data file
        for row in dataLines: # Read through each row of data
            loc = row[1] # Item in the second column is the location
            # If the current location and date match the target location and date, store the current data in targetData
            if loc == location:
                validData = True # Keep track of whether an invalid temperature value is found
                try: # Attempt to convert item in column 3 (min temp) to a float, if unsuccessful, it is invalid
                    minTemp = float(row[2])
                    minTemps.append(minTemp)
                except:
                    validData = False
                try: # Attempt to convert item in column 4 (max temp) to a float, if unsuccessful, it is invalid
                    maxTemp = float(row[3])
                    maxTemps.append(maxTemp)
                except:
                    validData = False
                rDate = datetime.datetime.strptime(row[0], '%Y-%m-%d') # Convert the date string into a datetime object
                if validData and rDate == targetDate: # If the min and max temps are valid and the date matches the target date, record the values
                    targetData = { 'min' : minTemp, 'max' : maxTemp}
    # Return an empty tuple if the given location or date were not found in the data or the min or max 
    # temperature was not recorded at that location on that date
    if targetData == {}:
        return (None, None)
    # Calculate the average min and max temperatures at the given location
    avgMinTemp = mean(minTemps)
    avgMaxTemp = mean(maxTemps)
    return (round(avgMinTemp - targetData['min'], 1), round(targetData['max'] - avgMaxTemp, 1))