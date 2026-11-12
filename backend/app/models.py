from pydantic import BaseModel, Field  # pyright: ignore[reportMissingImports]
from datetime import date
from typing import Optional

class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1)
    date:date
    notes:Optional[str] = None


class Expense(ExpenseCreate):
    id: int    