# Logical Operators

#Logical operators are used to combine conditional statements:

"""
Operator	Description	                                              Example
and 	    Returns True if both statements are true	              x < 5 and  x < 10	
or	        Returns True if one of the statements is true	          x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	  not(x < 5 and x < 10)
"""

x = 5


print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

