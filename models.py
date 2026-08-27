from dataclasses import dataclass
from enum import Enum


class TicketStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"
    EXPIRED = "EXPIRED"

@dataclass
class Ticket:
    id: int
    name: str
    description: str
    created_at: str
    sla: int
    status: TicketStatus