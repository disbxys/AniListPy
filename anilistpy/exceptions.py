

from collections.abc import Mapping
from typing import Any


class AniListException(Exception):
    pass


class APIException(AniListException):

    def __init__(
            self,
            status_code: int,
            error_json: Mapping[str, Any] | None = None,
            **relevant_params: int | str | None
    ):
        self.status_code = status_code
        self.error_json = error_json
        self.relevant_params = relevant_params

        super().__init__(self.status_code)


    def __str__(self) -> str:
        output = f"HTTP {self.status_code}"

        if self.error_json:
            err_str = ", ".join(f"{k}={val}" for k, val in self.error_json.items())
            output += f" - {err_str}"

        if self.relevant_params:
            param_str = ", ".join(f"{k}={val}" for k, val in self.relevant_params.items())
            output += f" - {param_str}"

        return output
    

    def __repr__(self) -> str:
        return (
            f"APIException(status_code={self.status_code},"
            f"error_json={self.error_json}, relevant_params={self.relevant_params})"
        )
    

class InvalidMediaTypeError(AniListException):
    pass


class InvalidVariableError(AniListException):
    pass
