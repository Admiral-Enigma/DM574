from dataclasses import dataclass
from math import sqrt


@dataclass
class Point2D:
    x: float
    y: float


def make_point(x: float, y: float) -> Point2D:
    """Returns a point based on 2 coordinates"""
    return Point2D(x, y)


def move(p: Point2D, dx: float, dy: float) -> None:
    """Moves point p by dx and dy"""
    p.x += dx
    p.y += dy


def distance_to_origin(p: Point2D) -> float:
    """Calculates the distance to the origin"""
    return sqrt(p.x**2 + p.y**2)


def distance(p1: Point2D, p2: Point2D) -> float:
    """Calculates the distance between two points"""
    x = p2.x - p1.x
    y = p2.y - p1.y
    return sqrt(x**2 + y**2)


def equals(p1: Point2D, p2: Point2D) -> bool:
    """Checks if two points have the same postition"""
    return p1.x == p2.x and p1.y == p2.y


def copy(p: Point2D) -> Point2D:
    """Returns a copy of point p"""
    return Point2D(p.x, p.y)


def to_string(p: Point2D) -> str:
    """Convert a point to string"""
    return f"({p.x}, {p.y})"


if __name__ == "__main__":
    p1 = make_point(0, 0)
    p2 = p1

    move(p1, 1, 1)
    print(to_string(p2))

    move(p2, 3, 3)
    print(to_string(p2))
    print("----------------------------------------")
    print(distance_to_origin(p2))
