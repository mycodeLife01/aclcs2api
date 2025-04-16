from typing import Any, Optional
from pydantic import BaseModel


class ResponseWrapper(BaseModel):
    message: Optional[str] = "success"
    data: Any
