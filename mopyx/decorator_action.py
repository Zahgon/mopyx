import functools
from typing import TypeVar, Callable, Optional, cast

from mopyx import rendering

T = TypeVar("T")

_update_index = 0


def action(f: Callable[..., T]) -> Callable[..., T]:
    """
    Do multiple operations on the model, at the end of which the
    rendering will be updated.
    """

    @functools.wraps(f)
    def action_wrapper(*args, **kw) -> Optional[T]:
        pass

    return cast(Callable[..., T], action_wrapper)
