class Shape:
    def init(self,x,y):
        self.x=x
        self.y=y
        
    def area(self,x,y):
        self.x=x
        self.y=y
        a=self.x*self.y
        print ('Area of a rectangle',a)   
class Square(Shape): #class Square inherits class Shape.
    def init(self,x):
        self.x=x
        
    def area(self,x):
        self.x=x
        a= self.x*self.x
        print('Area of a square',a)
