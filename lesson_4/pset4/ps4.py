import numpy as np
import pylab
import re
import matplotlib.pyplot as plt

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

INTERVAL_1 = list(range(1961, 2006))
INTERVAL_2 = list(range(2006, 2016))

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a numpy 1-d array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]



"""
End helper code
"""

# Problem 1
def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).
    Args:
        x: a list with length N, representing the x-coords of N sample points
        y: a list with length N, representing the y-coords of N sample points
        degs: a list of degrees of the fitting polynomial
    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """    
    models = []
    for deg in degs:
        model = np.polyfit(x, y, deg)
        models.append(model)
    return models

# Example usage:
# x_example = [1961, 1962, 1963]
# y_example = [4.4, 5.5, 6.6]
# degs_example = [1, 2]
# models_example = generate_models(x_example, y_example, degs_example)
# print(models_example)

# Problem 2
def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    # TODO
    mean = sum(y) / len(y)
    numerator = sum((y[i] - estimated[i]) ** 2 for i in range(len(y)))
    denominator = sum((y[i] - mean) ** 2 for i in range(len(y)))
    r_squared = 1 - (numerator / denominator)
    return r_squared
    
# print(r_squared([32.0, 42.0, 31.3, 22.0, 33.0], [32.3, 42.1, 31.2, 22.1, 34.0])) # 0.9944

# Problem 3

raw_data = Climate('data.csv')
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-square for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points
    Args:
        x: a list of length N, representing the x-coords of N sample points
        y: a list of length N, representing the y-coords of N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.
    Returns:
        None
    """
    for model in models:
        predicted_values = np.polyval(model, x)
        r_squared_value = r_squared(y, predicted_values)

        # Print the R^2 value
        print(f'R^2 value: {r_squared_value:.3f}')

        # Plotting code remains the same
        plt.scatter(x, y, color='blue', label='Data Points')
        plt.plot(x, predicted_values, color='red', label='Best Fit Curve')
        plt.xlabel('Year')
        plt.ylabel('Temperature')
        plt.title(f'Degree {len(model) - 1} Model\nR-squared: {r_squared_value:.3f}')
        plt.legend()
        plt.show()

# # Problem 3
# y = []
# x = INTERVAL_1
# for year in INTERVAL_1:
#     y.append(raw_data.get_daily_temp('BOSTON', 1, 10, year))
# models = generate_models(x, y, [1])
# evaluate_models_on_training(x, y, models)


# Problem 4
x1 = INTERVAL_1
x2 = INTERVAL_2
y = []

# Generate y values for the average annual temperature in Boston
for year in INTERVAL_1:
    y.append(np.mean(raw_data.get_yearly_temp('BOSTON', year)))

# Generate models and evaluate
models = generate_models(x1, y, [1])
evaluate_models_on_training(x1, y, models)


# # Problem 4: FILL IN MISSING CODE TO GENERATE y VALUES
# x1 = INTERVAL_1
# x2 = INTERVAL_2
# y = []
# # MISSING LINES
# models = generate_models(x, y, [1])    
# evaluate_models_on_training(x, y, models)

#%%


import random

class Lecture(object):
    def __init__(self, listen, sleep, fb):
        self.listen = listen
        self.sleep = sleep
        self.fb = fb
    def get_listen_prob(self):
        return self.listen
    def get_sleep_prob(self):
        return self.sleep
    def get_fb_prob(self):
        return self.fb
     
def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std
        
def lecture_activities(N, aLecture):
    '''
    N: integer, number of trials to run
    aLecture: Lecture object
 
    Runs a Monte Carlo simulation N times.
    Returns: a tuple, (float, float)
              Where the first float represents the mean number of lectures it takes 
              to have a lecture in which all 3 activities take place,
              And the second float represents the total width of the 95% confidence 
              interval around that mean.
    '''
    # IMPLEMENT THIS FUNCTION

    tot = []
    
    for _ in range(N):
        lect = 0
        act = set()
        while len(act) < 3:
            if random.uniform(0, 1) < aLecture.get_listen_prob():
                act.add('listen')
            if random.uniform(0, 1) < aLecture.get_sleep_prob():
                act.add('sleep')
            if random.uniform(0, 1) < aLecture.get_fb_prob():
                act.add('fb')
            lect += 1
        tot.append(lect)

    mean, std = get_mean_and_std(tot)
    total_width = 1.96 * std
    
    # Calculate margin of error using the t-distribution critical value
    margin_of_error = 1.96 * std * mean

    return mean, margin_of_error

    # return mean, total_width


# sample test cases 
a = Lecture(1, 1, 1)
print(lecture_activities(100, a))
# the above test should print out (1.0, 0.0)
          
b = Lecture(1, 1, 0.5)
print(lecture_activities(100000, b))
# # the above test should print out something reasonably close to (2.0, 5.516)





#%%

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))

#%%

import random
import pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.show()

# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_runs = []

    for _ in range(numTrials):
        rolls = [die.roll() for _ in range(numRolls)]

        # Calculate the longest run
        longest_run = 1
        current_run = 1
        for i in range(1, numRolls):
            if rolls[i] == rolls[i - 1]:
                current_run += 1
                longest_run = max(longest_run, current_run)
            else:
                current_run = 1

        longest_runs.append(longest_run)

    makeHistogram(longest_runs, 10, 'Longest Run', 'Frequency', 'Longest Run Histogram')

    mean, _ = getMeanAndStd(longest_runs)
    return mean

# One test case
print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000))








#%%

import itertools
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    min_sum = float('inf')  # Initialize with positive infinity
    best_combination = None

    for r in range(1, len(choices) + 1):
        for combination in itertools.combinations(choices, r):
            current_sum = sum(combination)
            if current_sum == total:
                result = np.array([1 if choice in combination else 0 for choice in choices])
                return result
            elif current_sum < total and current_sum < min_sum:
                min_sum = current_sum
                best_combination = combination

    if best_combination is not None:
        result = np.array([1 if choice in best_combination else 0 for choice in choices])
        return result
    else:
        # No exact match, return the closest result
        result = np.array([1 if choice <= total else 0 for choice in choices])
        return result

# Example usage:
choices = [1, 2, 2, 3]
total = 4
result = find_combination(choices, total)
print(result)


#%%


import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

def find_combination(choices, total):
    min_sum = float()
    best = None

    def get_result(combination):
        return np.array([1 if choice in combination else 0 for choice in choices])

    for r in range(1, len(choices) + 1):
        for i in range(len(choices)):
            combination = choices[i:i + r]
            cur_sum = sum(combination)
            if cur_sum == total:
                return get_result(combination)
            elif cur_sum < total and cur_sum < min_sum:
                min_sum = cur_sum
                best = combination

    if best is not None:
        return get_result(best)
    else:
        return get_result([choice for choice in choices if choice <= total])
    
    
#%%

def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')        
        elif i % 3 == 0:
            print('Fizz')
            
        elif i % 5 == 0:
            print("Buzz")    
        else:
            print(i)



fizzBuzz(15)





