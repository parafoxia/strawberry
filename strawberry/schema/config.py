from __future__ import annotations

from dataclasses import InitVar, dataclass, field
from typing import Any, Callable

from strawberry.resolvers import default_resolver

from .name_converter import NameConverter


@dataclass
class StrawberryConfig:
    auto_camel_case: InitVar[bool] = None  # pyright: reportGeneralTypeIssues=false
    name_converter: NameConverter = field(default_factory=NameConverter)
    default_resolver: Callable[[Any, str], object] = default_resolver
    relay_max_results: int = 100
    disable_field_suggestions: bool = False

    def __post_init__(
        self,
        auto_camel_case: bool,
    ) -> None:
        if auto_camel_case is not None:
            self.name_converter.auto_camel_case = auto_camel_case
