def find_largest_drop(temps):
    """
    Return the largest consecutive temperature drop, or 0.0 if none.
    """
    current_drops = 0
    for i in range (len(temps)-1):

        drops = temps[i] - temps[i+1]
        
        if drops  > current_drops:
            current_drops = drops

    return current_drops

    if current_drops == 0:
        return 0.0




# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
