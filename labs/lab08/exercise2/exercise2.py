# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # TODO: Implement this function
    list1 = open(file1, "r")
    list2 = open(file2, "r")
    

    list1_name = set(list1.readlines())
    list2_name = set(list2.readlines())

    result = list1_name | list2_name
    result_list = list(result)
    result_sort = sorted(result_list)


    f = open(output_file, "w")
    f.writelines(result_sort)

    list1.close()
    list2.close()
    f.close()

    return len(result)

# Test your code here
result = merge_lists("CP125-Class-Repo/labs/lab08/exercise2/data/list1.txt", "CP125-Class-Repo/labs/lab08/exercise2/data/list2.txt", "CP125-Class-Repo/labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
