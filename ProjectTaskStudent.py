class Address:
    def set_pincode(self,pincode):
        self.pincode = pincode

    def set_city(self,city):
        self.city = city

    def get_pincode(self):
        return self.pincode
    
    def get_city(self):
        return self.city

a1 = Address()



class Student:
    def set_rn(self,rollno):
        self.rollno = rollno
        

    def set_name(self,name):
        self.name = name
        

    def set_marks(self,marks):
        self.marks = marks
        

    def set_address(self,address):
        self.address = address
        

    def get_rn(self):
        return self.rollno
        

    def get_name(self):
        return self.name
        

    def get_marks(self):
        return self.marks
        

    def get_address(self):
        return self.address
        

s1 = Student()

