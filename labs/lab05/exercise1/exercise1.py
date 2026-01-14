
def was_backward_detected(path):
    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """
    

    for i in range(1, len(path)):
        x1, y1, z1 = path[i]
        x2, y2, z2 = path[i-1]

        if x1 < x2 or y1 < y2:
            return True
        
    return False






# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
