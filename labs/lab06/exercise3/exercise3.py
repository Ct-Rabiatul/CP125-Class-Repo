def audit_blocklists(list_a, list_b, list_c):


    set_list_a = set(list_a)
    set_list_b = set(list_b)
    set_list_c = set(list_c)

    universal = set_list_a & set_list_b & set_list_c

    redundant = (set_list_a & set_list_b) | (set_list_b & set_list_c) | (set_list_a & set_list_c)

    uniqueA = set_list_a - set_list_b - set_list_c

    return (universal, redundant , uniqueA)






