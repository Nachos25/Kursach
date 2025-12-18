from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Order:
    id: str
    title: str
    created_at: datetime = field(default_factory=datetime.utcnow)
