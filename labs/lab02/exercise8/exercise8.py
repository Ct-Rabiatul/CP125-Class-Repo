# Lab 02 Exercise 8: Bouncing Ball Simulation
# Write your code below:

def calculate_bounce_height(current_height):
    """Calculate next bounce height (80% of current)."""
    # TODO: Implement this function
    bounce_height = 0.8 * current_height

    return bounce_height

def is_ball_stopped(height):
    """Return True if height < 1, False otherwise."""
    # TODO: Implement this function
    if height < 1:
        return True
    else:
        return False

def simulate_bouncing_ball(start_height):
    """
    Simulate bouncing ball.
    Returns: (bounce_count, total_distance)
    """
    # TODO: Implement using calculate_bounce_height and is_ball_stopped 
    bounce_count = 
    total
# Test your code here
print("Testing Bouncing Ball Simulation...")
