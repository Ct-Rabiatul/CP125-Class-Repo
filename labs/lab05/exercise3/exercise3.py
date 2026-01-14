
def find_bottleneck_index(traceroute):
    """
    Find the index of the hop where the largest latency jump begins.
    """
    bottleneck_index = 0
    current_jumps = 0
    for i in range (1, len(traceroute)):
    
        hop_number, latency_in_ms = traceroute[i-1]
        hop_number1, latency_in_ms2 = traceroute[i]

        jumps = abs(latency_in_ms2 - latency_in_ms)
        
        if jumps > current_jumps:
            current_jumps = jumps
            bottleneck_index = i-1
        
    return bottleneck_index






# Test
traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
result = find_bottleneck_index(traceroute)
print(f"Bottleneck Index: {result}")  # Expected: 1
