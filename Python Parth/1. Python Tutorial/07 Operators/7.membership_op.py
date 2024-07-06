# Membership Operators

#Membership operators are used to test if a sequence is presented in an object:

"""
Operator	Description	                                                                        Example
in 	        Returns True if a sequence with the specified value is present in the object	    x in y	
not in	    Returns True if a sequence with the specified value is not present in the object	x not in y
"""

x = ["apple", "banana"]

# in
print("banana" in x)
#returns True because a sequence with the value "banana" is in the list


# not in
print("pineapple" not in x)
#returns True because a sequence with the value "pineapple" is not in the list



