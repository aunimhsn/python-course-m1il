from typing import Self, Type
from math import sqrt

class Point2D:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def distance_to_origin(self) -> float:
        return sqrt((self.x**2) + (self.y**2))

    def distance_to_other(self, other:Type[Self]) -> float:
        return sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))
    
class Point3D(Point2D):
    def __init__(self, x, y, z):
        # Appel du constructeur de la classe mère
        Point2D.__init__(self, x, y)
        # Ajout de la troisième dimension z
        self.z = z

    # Surcharge des méthodes / Override
    # Réécriture des méthodes, adaptation à la classe enfant
    def distance_to_origin(self) -> float:
        return sqrt((self.x)**2+(self.y)**2+(self.z)**2)

    def distance_to_other(self, other:Type[Self]) -> float:
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)

point_a = Point2D(3, 5)
point_b = Point2D(1, 10)

point_c = Point3D(3, 5, 9)
point_d = Point3D(3, 1, 12)
print(point_c.distance_to_other(point_d))