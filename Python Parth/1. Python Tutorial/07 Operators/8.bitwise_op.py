# Bitwise Operators

#Bitwise operators are used to compare (binary) numbers:

"""
Operator	Name	                Description	                                                                                              Example
& 	        AND	                    Sets each bit to 1 if both bits are 1	                                                                  x & y	
|	        OR	                    Sets each bit to 1 if one of two bits is 1	                                                              x | y	
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1	                                                          x ^ y	
~	        NOT	                    Inverts all the bits	                                                                                  ~x	
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                      x << 2
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	  x >> 2
"""

"""
Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""



print(6 & 3)

"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================
"""

print(6 | 3)

print(6 ^ 3)

print(~ 3)

print(6 << 3)

print(6 >> 3)

