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

    def cross(self, other: Self) -> Self:
        return self.x * other.y - self.y * other.x

    def __mul__(self, other: float | Self) -> Self:
        if isinstance(other, float):
            return Vec2D(self.x * other, self.y * other)
        elif isinstance(other, Vec2D):
            dot = self.x * other.x + self.y * other.y
            return dot
        else:
            raise ValueError("Unsupported type")

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

    def __getitem__(self, index: int | str | slice):
        if type(index) is int:
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            else:
                raise IndexError("Index out of range")
        elif type(index) is str:
            if index == "x":
                return self.x
            elif index == "y":
                return self.y
            else:
                raise KeyError("Not such key")
        elif type(index) is slice:
            return self.x, self.y
        else:
            raise TypeError("Index must be int or str")

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __repr__(self):
        return "Vec2D" + self.__str__()

    def __hash__(self):
        return (hash(self.x) + 1) * (hash(self.y) + 1) + hash(self.__repr__())

