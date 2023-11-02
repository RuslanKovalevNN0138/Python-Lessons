class Point:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return"({0},{1},{2})".format(self.x,self.y,self.z)

    def __add__(self,point):
        x=self.x+point.x
        y=self.y+point.y
        z=self.z+point.z
        return Point(x,y,z)

    def __sub__(self,point):
        x=self.x-point.x
        y=self.y-point.y
        z=self.z-point.z
        return Point(x,y,z)

    def __mul__(self,point):
        x=self.x*point.x
        y=self.y*point.y
        z=self.z*point.z
        return x+y+z

    def __lt__(self,point):
        self_dist = (self.x ** 2) + (self.y ** 2) +(self.z**2)
        point_dist = (point.x ** 2) + (point.y ** 2)+(point.z**2)
        return self_dist < point_dist
    
    def __gt__(self,point):
        self_dist=(self.x**2)+(self.y**2)+(self.z**2)
        point_dist=(point.x**2)+(point.y**2)+(point.z**2)
        return self_dist>point_dist

    def __eq__(self,point):
        return self.x==point.x and self.y==point.y and self.z==point.z

p1=Point(2,3,4)
p2=Point(5,6,7)

p3=p1+p2
print(p3)

p4=p3-p2
print(p4)

dot=p1*p2
print(dot)

print("p4==p1") if p1==p4 else print("p4!=p1")
print("p4>p1") if p1>p4 else print("p1>p4")
print("p4<p1") if p1<p4 else print("p1<p4")



    

    
