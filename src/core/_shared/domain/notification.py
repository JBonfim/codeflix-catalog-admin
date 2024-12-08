from dataclasses import dataclass
from typing import List, Union

@dataclass
class Notification:
    def __init__(self) -> None:
        self._errors: List[str] = []

    def add_error(self, error: Union[str, List[str], None]) -> None:
        if error is None:
            # Ignora valores None
            return
        if isinstance(error, list):
            # Adiciona cada item da lista como uma string
            self._errors.extend(map(str, error))
        elif isinstance(error, str):
            self._errors.append(error)
        else:
            raise TypeError(f"Expected a string or a list of strings, but got {type(error).__name__}")

    @property
    def messages(self) -> str:
        if len(self._errors) == 0:
            return ""
        return ",".join(self._errors)

    @property
    def has_errors(self) -> bool:
        return bool(self._errors)

    def __str__(self) -> str:
        return self.messages
