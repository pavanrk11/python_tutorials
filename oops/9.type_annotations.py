# variable annotations

x = 1
name = "Pavan"

# int x = 1
# string name  = "Pavan"

x: int = 1
# name : float = "Pavan"
name: str = "Pavan"

# mypy : static typing check for Python
# pip install mypy

# function annotations

# def add(a, b, c):
#     return a + b + c


def add(a: int, b: int, c: int) -> int:
    return a + b + c


result = add(1, 2, 3)
print(result)
# result1 = add(1.0, 2.0, 3.5)
# print(result1)
# result1 = add('a', 'b', 'c')
# print(result1)


def add1(a: int, b: int, c: int) -> None:
    print(a + b + c)


add1(1, 1, 1)
# add1('a', 'b', 'c')

# list, dict, set example
list1: list = [1, 2, 3]
list2: list[int] = [1, 2, 3]
list3: list[str] = ["a", "b"]
list4: list[list[int]] = [[1, 2], [3, 4]]

tuple1: tuple[int, int, int] = (1, 2, 3)

dict1: dict[int, list] = {1: ["a", "b"], 2: [3, 4]}

set1: set[int] = {1, 1, 2, 2, 3, 3}
set2: set[float] = {1.0, 2.0, 2.0}
set3: set[bool] = {True, False}

list5: list[dict[str, list]] = [{"a": [1, 2, 3], "b": [4, 5, 6]}]

# aliasing
from typing import List

# from typing import List
# Vector = List[float]

# Python 3.9+
from typing import TypeAlias

Point: TypeAlias = tuple[float, float]
Triangle: TypeAlias = tuple[Point, Point, Point]

Vector: TypeAlias = list[float]  # No import needed, lower case l


def func1(v: Vector) -> Vector:
    return v + v * 2


res1 = func1([1.0, 2.0])
print(res1)

Vectors = list[Vector]


def func2(v: Vectors) -> Vectors:
    return v + v * 2


res2 = func2([[1.0, 2.0], [3.0, 4.0]])
print(res2)

from typing import Optional, Any, Callable


def func3(a: int, c: Any, b: Optional[int] = None) -> int:
    return 1


func3(10, 20, 30)


def func4(func: Callable[[int, Any, Optional[int]], int]) -> None:
    func(1, 5.0, 100)


func4(func3)

##


def add2(x: int, y: int) -> int:
    return x + y


def foo1(add: Callable[[int, int], int]) -> None:
    add(10, 20)


print(foo1(add2))


from typing import TypeVar

TNum = TypeVar("TNum", int, float)


def quick_sort(arr: List[TNum]) -> List[TNum]:
    return arr


foo2 = [1, 2, 3, 4]  # type: List[int]
quick_sort(foo2)

bar = [1.0, 2.0, 3.0, 4.0]  # type: List[float]
quick_sort(bar)
