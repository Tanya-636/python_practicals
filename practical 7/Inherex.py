class Parent():
       def first(self):
           print('first function')
 
class Child(Parent):
       def second(self):
          print('second function')
 
ob = Child()
ob.first()
ob.second()

#subclass
class Parent:
     def __init__(self , fname, fage):
          self.firstname = fname
          self.age = fage
     def view(self):
         print(self.firstname , self.age)
class Child(Parent):
     def __init__(self , fname , fage):
          Parent.__init__(self, fname, fage)
          self.lastname = "Xyz"
     def view(self):
          print("I am", self.firstname, self.lastname,".", "My age is ",  self.age)
ob = Child("Abc" , '28')
ob.view()

#Single Inheritance
class Parent:
     def func1(self):
          print("this is function one")
class Child(Parent):
     def func2(self):
          print(" this is function 2 ")
ob = Child()
ob.func1()
ob.func2()

#Multiple Inheritance
class Parent:
   def func1(self):
        print("this is function 1")
class Parent2:
   def func2(self):
        print("this is function 2")
class Child(Parent , Parent2):
    def func3(self):
        print("this is function 3")
 
ob = Child()
ob.func1()
ob.func2()
ob.func3()

#Multilevel Inheritance
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Child):
      def func3(self):
          print("this is function 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()

#Hierarchical Inheritance
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
      def func3(self):
          print("this is function 3")
 
ob = Child()
ob1 = Child2()
ob1.func1()
ob1.func3()

#Hybrid Inheritance
class Parent:
     def func1(self):
         print("this is function one")
 
class Child(Parent):
     def func2(self):
         print("this is function 2")
 
class Child1(Parent):
     def func3(self):
         print(" this is function 3")   
 
class Child3(Child1):
     def func4(self):
         print(" this is function 4")
 
ob = Child3()
ob.func1()

#Python super() Function
class Parent:
     def func1(self):
         print("this is function 1")
class Child(Parent):
     def func2(self):
          super().func1()
          print("this is function 2")
 
ob = Child()
ob.func2()

#Method Overriding
class Parent:
    def func1(self):
        print("this is parent function")
 
class Child(Parent):
    def func1(self):
        print("this is child function")
 
ob = Child()
ob.func1()

