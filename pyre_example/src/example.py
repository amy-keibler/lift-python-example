from typing import Callable
from typing import Optional
from pyre_extensions import ParameterSpecification

def to_seconds(milliseconds: List[float]) -> List[int]:
    return [int(x/1000.0) for x in milliseconds]

my_list: List[int] = [1]
my_list = to_seconds(my_list) # Pyre errors here!


def zeroes(number_of_elements: int) -> List[float]:
    a = [0] * number_of_elements
    return a # Pyre errors here!

P = ParameterSpecification("P")

# OK
def good(f: Callable[P, int], *args: P.args, **kwargs: P.kwargs) -> int:
    return f(*args, **kwargs)

# Error because `**kwargs: P.kwargs` is missing.
def bad1(f: Callable[P, int], *args: P.args) -> int:
    return f(*args)

# Error because `*args: P.args` is missing.
def bad2(f: Callable[P, int], **kwargs: P.kwargs) -> int:
    return f(**kwargs)


class Base: pass

class Child1(Base):
    size: int = 42

# No size field.
class Child2(Base): pass

def print_child2_size(get_size: Callable[[Base], int]) -> None:
    child2 = Child2()
    size = get_size(child2)
    print(size)

def size_of_child1(child1: Child1) -> int:
    return child1.size

print_child2_size(size_of_child1)


class Foo:
    x: int = 0

def f(foo: Foo) -> None:
    foo.x = "abc"


def foo(x: Optional[int]) -> bool:
    return x < 0  # type error: Optional[int] is not a supported operand

def bar(x: Optional[int]) -> bool:
    if x:
        return x < 0  # no type error
    return False


class A:
    @staticmethod
    def foo() -> int:
        pass

class B(A):
    @classmethod # Non-static method `B.foo` cannot override a static method defined in `A`.
    def foo(cls) -> int:
        pass
