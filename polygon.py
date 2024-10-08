from dataclasses import dataclass
from point import (
    Point2D,
    distance,
    distance_to_origin,
    make_point,
    to_string as point_to_string,
)
from functools import reduce


@dataclass
class Polygon:
    vertices: list[Point2D]


def make_polygon(v: list[Point2D]) -> Polygon:
    """Creates a new polygon from a list of points"""
    return Polygon(v)


def perimeter(p: Polygon) -> float:
    def _permiter(v: list[Point2D], distance_acc: float):
        if len(v) == 0:
            return distance_acc
        elif len(v) == 2:
            return distance_acc + distance(v[0], v[1])
        else:
            # More than 2 elements left
            distance_acc += distance(v[0], v[1])
            return _permiter(v[1:], distance_acc)

    return _permiter(p.vertices, 0)


def nearest(p: Polygon) -> Point2D:
    distances = list(map(lambda x: distance_to_origin(x), p.vertices))
    return p.vertices[distances.index(min(distances))]


def longest_side(p: Polygon) -> float:
    distances = list(
        map(
            lambda x: distance(
                x, p.vertices[((p.vertices.index(x) + 1) % len(p.vertices))]
            ),
            p.vertices,
        )
    )
    return max(distances)


if __name__ == "__main__":
    p = make_polygon([make_point(1, 1), make_point(10, 10), make_point(10, 0)])
    print(longest_side(p))
    print(point_to_string(nearest(p)))
    print(perimeter(p))
