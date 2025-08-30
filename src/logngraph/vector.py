from typing import Self
import math


class Vec2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def mag(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def dist(self, other: Self) -> float:
        return (other - self).mag()

    def norm(self) -> Self:
        return self / self.mag()

    def rotate(self, degrees: float, pivot: Self = None) -> Self:
        if pivot is None:
            pivot = Vec2D(0, 0)
        dx, dy = self.x - pivot.x, self.y - pivot.y
        theta = math.radians(degrees)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        return Vec2D(
            dx * cos_theta - dy * sin_theta,
            dx * sin_theta + dy * cos_theta
        ).translate(pivot)

    def translate(self, translation: Self) -> Self:
        return Vec2D(self.x + translation.x, self.y + translation.y)

    def copy(self) -> Self:
        return Vec2D(self.x, self.y)

    def __mul__(self, other: float) -> Self:
        return Vec2D(self.x * other, self.y * other)

    def __truediv__(self, other: float):
        return Vec2D(self.x / other, self.y / other)

    def __add__(self, other: Self) -> Self:
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vec2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __cmp__(self, other: Self) -> bool:
        return self.x > other.x and self.y > other.y

    def __iter__(self):
        yield self.x
        yield self.y

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return (hash(self.x) + 1) * (hash(self.y) + 1) + hash(self.__repr__())

