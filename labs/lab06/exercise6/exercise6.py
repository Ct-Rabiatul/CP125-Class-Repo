def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """
    drop_requests_set = set(drop_requests)
    update_enrolled = enrolled ^ drop_requests_set

    check = len(update_enrolled)

    if check < 5:
        for item in range(7- check):
            if  len(waitlist)==0:
                return len(update_enrolled)
            else:
                insert= waitlist.pop()
                update_enrolled.add(insert)

    


    return len(update_enrolled)