###########################
# 6.00.2x Problem Set 1: Space Cows 
from collections import OrderedDict
from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    sortedCows = OrderedDict(sorted(cows.items(), key=lambda item: item[1], reverse= True))
    allShippedCows = []
      
    while sortedCows:
        shippedCows = []
        tempLimit = limit
        
        for n,v in list(sortedCows.items()):
            if v <= tempLimit:
                shippedCows.append(n)
                tempLimit -= v
                del sortedCows[n]
                
        allShippedCows.append(shippedCows)
            
    return allShippedCows


# print(greedy_cow_transport({'Horns': 50, 'Louis': 45, 'Polaris': 20, 'Lotus': 10, 'Clover': 5, 'Patches': 60, 'Milkshake': 75, 'MooMoo': 85, 'Miss Bella': 15, 'Muscles': 65}, 100))

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    
    all_partitions = get_partitions(list(cows.keys()))

    # Filter valid partitions based on weight limit
    
    
    '''
    
    valid_partitions = [
        partition for partition in all_partitions
        if all(sum(cows[cow] for cow in trip) <= limit for trip in partition)
    ]
    
    
    '''
    
    valid_partitions = []

    for partition in all_partitions:
        is_valid_partition = True

        for trip in partition:
            total_weight = 0
    
            for cow in trip:
                total_weight += cows[cow]
    
            if total_weight > limit:
                is_valid_partition = False
                break
    
        if is_valid_partition:
            valid_partitions.append(partition)
    

    # Find the partition with the minimum number of trips
    min_trips_partition = min(valid_partitions, key=len)

    return min_trips_partition
            
print(brute_force_cow_transport({'Boo': 20, 'Miss Bella': 25, 'MooMoo': 50, 'Lotus': 40, 'Horns': 25, 'Milkshake': 40}, 100))
# print(greedy_cow_transport({'Boo': 20, 'Miss Bella': 25, 'MooMoo': 50, 'Lotus': 40, 'Horns': 25, 'Milkshake': 40}, 100))

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start_time = time.time()
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    # greedy_cow_transport(cows, limit)
    brute_force_cow_transport(cows, limit)
    end_time = time.time()
    return end_time - start_time

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))

# print(compare_cow_transport_algorithms())

