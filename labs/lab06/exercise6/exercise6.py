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
    for name in drop_requests_set:

        enrolled.discard(name)

    check = len(enrolled)
    if check < 5:
        insert= waitlist.pop()
        enrolled.add(insert)

    


    return len(enrolled)