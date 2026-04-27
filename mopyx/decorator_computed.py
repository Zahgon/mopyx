import functools
from typing import TypeVar, Callable

from mopyx import rendering

T = TypeVar("T")


def computed(f: Callable[..., T]) -> T:
    """
    Add a computed property. A computed property only updates
    when one of the inner values changes. A computed property
    is not allowed to change the state of the object.
    """

    @property  # type: ignore
    @functools.wraps(f)
    def computed_wrapper(self) -> T:
        pass

    return computed_wrapper  # type: ignore
