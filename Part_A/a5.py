# Write a function nearly equal to test whether two strings are nearly equal. two strings
# a and b are nearly equal if one character change in b results in string a.


def is_nearly_equal(str1, str2):
    if len(str1) != len(str2):
        return False
    num_diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            num_diff += 1
    return num_diff == 1


first_string = input("Enter the first string:")
second_string = input("Enter the second string:")
if first_string == second_string:
    print("Strings are exactly equal")
elif is_nearly_equal(first_string, second_string):
    print("The strings are nearly equal")
else:
    print("The strings are not nearly equal")
