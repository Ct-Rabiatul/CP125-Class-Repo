# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    num_of_tent = math.ceil(participants / tent_capacity)
    cost_of_tent = num_of_tent * tent_price
    cost_of_meal = meal_price * participants
    total_cost = cost_of_meal + cost_of_tent

    return total_cost

# Test your code here
print("Testing Camping Logistics...")
