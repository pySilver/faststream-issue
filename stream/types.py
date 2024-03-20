from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, PositiveInt


class FeedState(BaseModel):
    items_count: PositiveInt
    items_approved: int
    items_rejected: int
    started_at: datetime
    completed_at: Optional[datetime]
    images: Optional[List[str]] = None

    def increment_counter(self, counter: str):
        if hasattr(self, counter):
            setattr(self, counter, getattr(self, counter) + 1)
        else:
            raise ValueError(f"Invalid counter: {counter}")

    def is_completed(self) -> bool:
        completed = self.items_approved + self.items_rejected == self.items_count
        if completed and not self.completed_at:
            self.completed_at = datetime.now()
        return completed
