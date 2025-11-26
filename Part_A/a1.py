# A1. Write a program create list with N elements. find all unique elements in the list. If an
# element is found only once in the list, then add that element to the unique list.


# function to get unique values
def Unique(List1):
    # initialize a null list
    unique_list = []
    # traverse for all elements
    for x in List1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


# driver code
if __name__ == "__main__":

    List1 = []
    n = int(input("Enter the number of values: "))
    print("Enter the values of list")
    for i in range(n):
        value = input()
        List1.append(value)
    U_list = Unique(List1)
    print("The Unique values from the list is:\n")
    print(U_list)
