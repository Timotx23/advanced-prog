# Exercise 1

class Book:
    ### Your code here
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
    def borrow(self):
        self.available = False
    def return_book(self):
        self.available = True
    def describe(self):
        if self.available == False:
            return f"The book {self.title} not available "
        else:
            return f"The book {self.title} is available "
            
# Exercise 2

import math

class Point:
    ### Your code here
    def __init__(self, x,y ):
        self.point = [[x,y]]
    def update_point(self,x,y):
        self.point.append([x,y])
    def distance(self):
        point0x = self.point[0][0]
        point0y= self.point[0][1]
        distancex = point0x
        distancey = point0y
        for i in range(1,len(self.point)):
            distancex += self.point[i][0]
            distancey += self.point[i][1]
        return [distancex, distancey]


# Exercise 3





# Test your classes below
### Your code here

