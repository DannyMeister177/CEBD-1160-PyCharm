# This script separates all values in the list [1,2,3,4,5,6,7,8,9] in two other lists. One resulting list should
# contain all even numbers and the other should contain all odd numbers.

list = [1,2,3,4,5,6,7,8,9]

ls_even = [x for x in list if x%2==0]
ls_odd = [x for x in list if x%2!=0]

