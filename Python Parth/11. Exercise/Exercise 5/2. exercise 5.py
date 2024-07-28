class students:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address

    def update_name(self,new_name):
        self.name=new_name
    
    def update_age(self,new_age):
        self.age=new_age

    def update_gender(self,new_gender):
        self.gender=new_gender

    def update_address(self,new_address):
        self.address=new_address    

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Address:",self.address)
            
s1=students("Parth",17,"Male","kalyan")

print("Initital details:")
s1.display()

# update details:
s1.update_name("Parth Patil")
s1.update_age(18)
s1.update_gender("Male")
s1.update_address("Mumbai")

# display updated details:
print("\nUpdated details:")
s1.display()










"""class Student:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def update_name(self, new_name):
        self.name = new_name

    def update_age(self, new_age):
        self.age = new_age

    def update_gender(self, new_gender):
        self.gender = new_gender

    def update_address(self, new_address):
        self.address = new_address

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Address:", self.address)


# Create a student object
student1 = Student("John Doe", 20, "Male", "123 Main St")

# Display initial details
print("Initial Details:")
student1.display_details()

# Update details
student1.update_name("Jane Doe")
student1.update_age(21)
student1.update_gender("Female")
student1.update_address("456 Elm St")

# Display updated details
print("\nUpdated Details:")
student1.display_details()"""