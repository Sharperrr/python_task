"""
Flatland is a country with a number of cities, some of which have train stations. Cities are 
numbered consecutively and each has a road of 1km length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. Determine 
the maximum distance from any city to its nearest train station.
Notes:
- Cities are indexed from 0.
- Number of cities is between 1 and 10000.
- Number of cities with train station is between 1 and number of cities.
- No city has more than one train station.
Example:
number_of_cities == 3
cities_with_train_station == [1]
There are 3 cities and city #1 has a train station. They occur consecutively along a route. 
City #0 is 1km away, city #1 is 0km away and city #2 is 1km away from its nearest train station.
The maximum distance is 1.
"""

from typing import List


def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    if len(cities_with_train_station) == 1: # if there is only one station in the country then one of the border cities will have the maximum distance from that station
        return cities_with_train_station[0] if cities_with_train_station[0] >= number_of_cities - 1 - cities_with_train_station[0] else number_of_cities - cities_with_train_station[0]
    else: # if there are two or more stations, then we find the longest distance between stations (or country borders) and calculate the maximum distance that can be between a station and a city in that area
        cities_with_train_station.sort() # make sure the station indexes are sorted in ascending order
        max = cities_with_train_station[0] # first we set the max distance as the distance between the border and the first station
        for x in range(len(cities_with_train_station) - 1): # the for loop replaces max value with a distance between two stations if there is a distance longer than the current max
            max = cities_with_train_station[x + 1] - cities_with_train_station[x] if cities_with_train_station[x + 1] - cities_with_train_station[x] > max else max
        # lastly the distance between the last station and the border is checked against the current max
        max = number_of_cities - 1 - cities_with_train_station[len(cities_with_train_station) - 1] if (number_of_cities - 1 - cities_with_train_station[len(cities_with_train_station) - 1]) > max else max
        return max / 2 if max % 2 == 0 else (max - 1) / 2 # the city in the middle of max distance will be the furthest away from a station in the country, so we divide max by 2

if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )
    print("ALL TESTS PASSED")