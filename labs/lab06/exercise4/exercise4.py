def synchronize_databases(legacy_list, modern_set, blacklist):

    lost_ID = set()
    ghost_ID = set()
    legacy_ID = set()
    blacklist_set = set(blacklist)

    for id,email in legacy_list:
        
        if email not in blacklist_set:
            legacy_ID.add(id)

    lost_ID = legacy_ID - modern_set
    ghost_ID = modern_set - legacy_ID

    return (lost_ID , ghost_ID)

