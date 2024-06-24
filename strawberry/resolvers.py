from typing import Any, Callable


def default_resolver(source: Any, name: str) -> object:
    """Accesses an object attribute or dictionary key."""
    return source.get(name) if isinstance(source, dict) else getattr(source, name)


def is_default_resolver(func: Callable[..., Any]) -> bool:
    """Check whether the function is a default resolver or a user provided one."""
    return getattr(func, "_is_default", False)
