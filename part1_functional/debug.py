class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with width: {self.width} and height: {self.height}"    
    
    def __repr__(self) -> str:
        return f"Represent {self.__class__.__name__}"
    
    def __eq__(self, __o: object) -> bool:
        """
        This method will be used to compare one object of the class to other object in the same class

        Args:
            __o (object): another object of Rectangle

        Returns:
            bool: _description_
        """
        # Why we don't use type(o) at here. Because if the object is the instance of the sub class of Ractange -> the condition will not be true
        # So we use isinstance method -> it will used not for only class but also subclass
        return bool(isinstance(__o, Rectangle) and self.width == __o.width and self.height == __o.height)

    def __lt__(self, object):
        if isinstance(object, Rectangle):
            return self.area() < object.area()
        else:
            return NotImplemented
r1 = Rectangle(2, 3)
r2 = Rectangle(1, 3)

r1 < 100