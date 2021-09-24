class Numbers():
    #MULTIPLIER = 3.5
    def init(self,x,y):
        self.x = x
        self.y = y
        self.__value = '' 
    def add(self, x, y):
        self.x=x
        self.y=y
        return self.x + self.y
    @classmethod
    def multiply(self, a):
        self.a = a
        MULTIPLIER = 3.5
        return (MULTIPLIER * self.a)
    @staticmethod
    def subtract(b, c):
        return b - c
    # Using @property decorator 
    @property  
    # Getter method 
    def value(self):
        print("Getting value...")
        return self.__value
    # Setter method 
    @value.setter 
    def value(self, xy_tuple):
        print("Setting value..." + xy_tuple)
        self.__value = xy_tuple
    # Deleter method 
    @value.deleter 
    def value(self):
        print("Deleting value")
        del self.__value


