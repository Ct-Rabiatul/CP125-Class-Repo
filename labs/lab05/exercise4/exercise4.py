
def filter_query_times(query_times):
    """
    Remove slow outliers (mean + std deviation) and return sorted times.
    """
    if len(query_times) == 0 :
        return []
    
    mean = sum(query_times) / len(query_times)
    variance = find_variance(mean, query_times)
    std_dev = variance ** (0.5)
    upper_limit = mean + std_dev

    copy_query_times = query_times [:]

    for i in copy_query_times:

        if i > upper_limit:
            query_times.remove(i)

    query_times.sort()
    return query_times




def find_variance (mean, query_times):
    sum = 0
    for i in range (len(query_times)):

        variance = (i - mean) ** 2
        sum += variance

    return sum/ len(query_times)





# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
