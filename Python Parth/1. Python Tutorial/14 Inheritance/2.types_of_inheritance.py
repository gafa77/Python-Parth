# Types of Inheritance

# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# Single Inheritance
class A:
    def method_A(self):
        print("This is method A")

class B(A):
    def method_B(self):
        print("This is method B")
        
        
# Multiple Inheritance
class C:
    def method_C(self):
        print("This is method C")

class D(A, C):
    def method_D(self):
        print("This is method D")


# Multi-Level Inheritance
class E(B):
    def method_E(self):
        print("This is method E")


# Hierarchical Inheritance
class F(A):
    def method_F(self):
        print("This is method F")

class G(A):
    def method_G(self):
        print("This is method G")


# Hybrid Inheritance
class H(D, F):
    def method_H(self):
        print("This is method H")


# Create instances and call methods
b = B()
b.method_A()  # Output: This is method A
b.method_B()  # Output: This is method B

d = D()
d.method_A()  # Output: This is method A
d.method_C()  # Output: This is method C
d.method_D()  # Output: This is method D

e = E()
e.method_A()  # Output: This is method A
e.method_B()  # Output: This is method B
e.method_E()  # Output: This is method E

f = F()
f.method_A()  # Output: This is method A
f.method_F()  # Output: This is method F

g = G()
g.method_A()  # Output: This is method A
g.method_G()  # Output: This is method G

h = H()
h.method_A()  # Output: This is method A
h.method_C()  # Output: This is method C
h.method_D()  # Output: This is method D
h.method_F()  # Output: This is method F
h.method_H()  # Output: This is method H
            
        

            