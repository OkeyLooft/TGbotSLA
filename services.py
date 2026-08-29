from dataclasses import asdict
from datetime import datetime, timedelta, timezone

import utils
from models import Ticket, TicketStatus
from storage import TicketStorage


class TicketServices:
    def __init__(self, storage: TicketStorage):
        self.storage = storage

    def create_id(self) -> int:
        data: dict = self.storage.read_json()
        ids: list = []
        for d in data:
            idsnum = d.get("id")
            ids.append(idsnum)
        if not ids:
            return 0

        return max(ids) + 1

    def ticket_created_at(self) -> str:
        MSK = timezone(timedelta(hours=3), "MSK")
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
            name=name.lower(),
            description=description,
            created_at=self.ticket_created_at(),
            sla=sla,
            status=TicketStatus.OPEN
        )

        self.write_ticket(ticket)

        return ticket
        
    def write_ticket(self, ticket: Ticket) -> None:
        data: dict = self.storage.read_json()
        data.append(asdict(ticket))
        self.storage.write_json(data)

    def show_ticket(self) -> list[dict]:
        data: list = self.storage.read_json()
        MSK = timezone(timedelta(hours=3), "MSK")
        now_moscow_time: datetime = datetime.now(MSK)
        ticket_list: list = []
        for d in data:
            dd: datetime = datetime.strptime(d["created_at"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=MSK)
            sla = timedelta(hours=d['sla'])
            hours_sla: datetime = dd + sla
            hours_left: timedelta = hours_sla - now_moscow_time
            id_ = d['id']
            name = d['name']
            status = d['status']
            ticket: dict = {
                "id": id_,
                "name": name,
                "status": status,
                "hours_left": hours_left 
            }
            ticket_list.append(ticket)
        return ticket_list

    def find_ticket(
        self,
        menu_find: str,
        value: str
        ) -> list:
        data: dict = self.storage.read_json()
        data_by_find: list = [item for item in data if str(item.get(menu_find.lower())) == value]
        return data_by_find
        
        