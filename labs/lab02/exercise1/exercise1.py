# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    liter_one_way = one_way_km / km_per_liter
    cost_one_way = liter_one_way * price_per_liter
    cost_round_trip = cost_one_way * 2
     
    if cost_round_trip > budget :
       budget = bool(False)
    else:
        budget = bool(True)
       
    return budget


