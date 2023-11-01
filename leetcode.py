class Employee():
    def __init__(self,name,age,position):
        self.name=name
        self._age=age
        self.__position=position

    # def print_name(self):
    #     print(self.name)
    # def print_age(self):
    #     print(self.age)
    # def print_position(self):
    #     print(self.position)
emp1=Employee("sai",20,"manager")
print(emp1.name)
print(emp1._age)
# print(Employee.__position)
# emp1.print_name()
# emp1.print_age()
# emp1.print_position()


# program to illustrate access modifiers of a class
 
# super class
class Super:
     
     # public data member
     var1 = None
 
     # protected data member
     _var2 = None
      
     # private data member
     __var3 = None
     
     # constructor
     def __init__(self, var1, var2, var3):  
          self.var1 = var1
          self._var2 = var2
          self.__var3 = var3
     
    # public member function   
     def displayPublicMembers(self):
  
          # accessing public data members
          print("Public Data Member: ", self.var1)
        
     # protected member function   
     def _displayProtectedMembers(self):
  
          # accessing protected data members
          print("Protected Data Member: ", self._var2)
      
     # private member function   
     def __displayPrivateMembers(self):
  
          # accessing private data members
          print("Private Data Member: ", self.__var3)
 
     # public member function
     def accessPrivateMembers(self):     
           
          # accessing private member function
          self.__displayPrivateMembers()
  
# derived class
class Sub(Super):
  
      # constructor 
       def __init__(self, var1, var2, var3): 
                Super.__init__(self, var1, var2, var3)
           
      # public member function 
       def accessProtectedMembers(self):
                 
                # accessing protected member functions of super class 
                self._displayProtectedMembers()
  
# creating objects of the derived class     
obj = Sub("Geeks", 4, "Geeks !") 
 
# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers() 
 
# Object can access protected member
print("Object is accessing protected member:", obj._var2)