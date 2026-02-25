#SITI RABIATUL ADAWIAH BINTI HUSSAIN
#To get the ascending number by user input 5 number and find the sum of all number and the largest number

#does not have parameters beacuse get input
def sort_ascending_num():

    numbers=[]

    for i in range(1,6):

        #to get number from user
        num = int(input(f"Enter number {i} : "))

        #to add number that user insert into the list
        numbers.append(num)

    #arrange number to be ascending which is from small number to big number
    numbers.sort()
    total = sum(numbers)
    #to find the largest number
    largest = max(numbers)

    return numbers, total, largest

#to declare the return value with variable, so easy to get the value for each return value
sort_num, sum_all_num, largest_num = sort_ascending_num()

print(f"Numbers in ascending order: {sort_num}")
print(f"Sum of all numbers: {sum_all_num}")
print(f"Largest number: {largest_num}")
print(f"\n=== Code Execution Successful ===")

