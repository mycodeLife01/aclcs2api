from typing import Any, Optional, Generic, TypeVar
from pydantic import BaseModel
T = TypeVar("T")

class ResponseWrapper(BaseModel, Generic[T]):
    message: Optional[str] = "success"
    data: Optional[T] = None
