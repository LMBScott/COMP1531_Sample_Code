import math

EARTH_RADIUS = 6353000
SIMULATION_STEPS = 1440
EPSILON = 1e-6

cities = []
satellites = []
cityCoverage = {}

def fgt(a, b): # Check whether float {a} is greater than float {b}
    return a > b + EPSILON

def fgte(a, b): # Check whether float {a} is greater than or equal to float {b}
    return a >= b - EPSILON

def flte(a, b): # Check whether float {a} is less than or equal to float {b}
    return a <= b + EPSILON

def simulate():
    global cities
    global satellites
    global cityCoverage 
    cityCoverage = dict((c['name'], 0) for c in cities)
    for i in range(SIMULATION_STEPS):
        thetaRanges = [] # List of tuples representing the coverage range of each satellite
        for s in satellites:
            s['theta'] += 60 * s['velocity'] / (EARTH_RADIUS + s['height']) # Update satellite position
            if fgt(s['theta'], 2*math.pi): # Wrap satellite position between 0 and 2Pi
                s['theta'] -= 2*math.pi
            thetaRanges.append(getThetaRange(s['theta'], s['height'])) # Add satellite's current coverage range to list
        for c in cities:
            covered = False
            for r in thetaRanges:
                if isInRange(r, c['theta']): # If the city lies within range of the satellite, it is covered
                    covered = True
            if not covered:
                cityCoverage[c['name']] += 1 # Increment the city's blackout minutes if no satellite currently covers it
    output = sorted(cityCoverage.items(), key=lambda x: x[0]) # Sort output list of tuples alphabetically by city name
    return output

def getThetaRange(theta, height): # Get the range of angles across which the satellite is visible on the surface
    # thetaQ: angle between line perpendicular to tangent drawn from satellite to circle and line from satellite to centre of circle
    thetaQ = math.acos(EARTH_RADIUS/(EARTH_RADIUS + height))
    thetaMin = theta - thetaQ # Min angle at which a city can have coverage from the satellite
    thetaMax = theta + thetaQ # Max angle at which a city can have coverage from the satellite
    return (thetaMin, thetaMax)

def isInRange(thetaRange, theta): # Check whether a given value of theta (0 < theta < 2Pi) lies within a given thetaRange
    thetaMin, thetaMax = thetaRange
    if thetaMin < 0: # If the lower bound is negative, modify check accordingly
        return fgte(theta, 2*math.pi + thetaMin) or flte(theta, thetaMax)
    elif thetaMax > 2*math.pi: # Otherwise, if the upper bound > 2Pi, modify check accordingly
        return flte(theta, thetaMax - 2*math.pi) or fgte(theta, thetaMin)
    return fgte(theta, thetaMin) and flte(theta, thetaMax) # If bounds are between 0 and 2Pi, perform normal check