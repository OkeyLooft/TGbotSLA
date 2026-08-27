from dataclasses import asdict
from datetime import datetime
from zoneinfo import ZoneInfo

from models import Ticket, TicketStatus
from storage import TicketStorage


class TicketServices:
    def __init__(self, storage: TicketStorage):
        self.storage = storage

    def create_id(self) -> int:
        data = self.storage.read_json()
        ids = []
        for d in data:
            idsnum = d.get("id")
            ids.append(idsnum)
        if not ids:
            return 0

        return max(ids) + 1

    def ticket_created_at(self) -> str:
        MSK = ZoneInfo("Europe/Moscow")
        create: datetime = datetime.now(MSK)
        created_at: str = create.strftime("%Y-%m-%d %H:%M:%S")

        return created_at

    def create_ticket(
        self,
        name: str,
        description: str,
        sla: int
        ) -> Ticket:

        ticket = Ticket(
            id=self.create_id(),
            name=name,
            description=description,
            created_at=self.ticket_created_at(),
            sla=sla,
            status=TicketStatus.OPEN
        )

        self.write_ticket(ticket)

        return ticket
        
    def write_ticket(self, ticket: Ticket) -> None:
        data = self.storage.read_json()
        data.append(asdict(ticket))
        self.storage.write_json(data)