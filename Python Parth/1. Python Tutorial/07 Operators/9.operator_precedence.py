# Operator Precedence

#Operator precedence describes the order in which operations are performed.


#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""

print(100 + 5 * 3)


#The precedence order is described in the table below, starting with the highest precedence at the top:
"""
Operator	   Description
()	           Parentheses	
**	           Exponentiation	
+x  -x  ~x	   Unary plus, unary minus, and bitwise NOT	
*  /  //  %	   Multiplication, division, floor division, and modulus	
+  -	       Addition and subtraction	
<<  >>	       Bitwise left and right shifts	
&	           Bitwise AND	
^	           Bitwise XOR	
|	           Bitwise OR	
==  !=  >      Comparisons,
>=  <  <=  is  identity,
is not  in     and membership
not in 	       operators
not	           Logical NOT	
and	           AND	
or	           OR	
"""

#If two operators have the same precedence, the expression is evaluated from left to right.


#Addition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)
"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
