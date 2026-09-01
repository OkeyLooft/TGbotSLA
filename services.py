from dataclasses import asdict
from datetime import datetime, timedelta, timezone

from models import Ticket, TicketStatus
from storage import TicketStorage


class TicketServices:
    def __init__(self, storage: TicketStorage):
        self.storage = storage

    def create_id(self) -> int:
        data: list = self.storage.read_json()
        ids: list = []
        for ticket in data:
            idsnum = ticket.get("id")
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
        data: list = self.storage.read_json()
        data.append(asdict(ticket))
        self.storage.write_json(data)

    def show_ticket(self) -> list[dict]:
        data: list = self.storage.read_json()
        MSK = timezone(timedelta(hours=3), "MSK")
        now_moscow_time: datetime = datetime.now(MSK)
        ticket_list: list = []
        for ticket in data:
            dd: datetime = datetime.strptime(ticket["created_at"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=MSK)
            sla = timedelta(hours=ticket['sla'])
            hours_sla: datetime = dd + sla
            hours_left: timedelta = hours_sla - now_moscow_time
            id_ = ticket['id']
            name = ticket['name']
            status = ticket['status']
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
        data: list = self.storage.read_json()
        data_by_find: list = [item for item in data if str(item.get(menu_find.lower())) == value]
        return data_by_find
    
    def show_ticket_by_id(
        self,
        id_input
        ):
        data: list = self.storage.read_json()
        data_by_id: list = [item for item in data if item.get('id') == id_input]
        return data_by_id
    
    def change_ticket(
        self,
        change_menu,
        id_input
        ):
        data: list = self.storage.read_json()
        data_by_id: list = [item for item in data if item.get('id') == id_input]
        try:
            data_by_id[0]['status'] = TicketStatus(change_menu)
            self.storage.write_json(data)
        except IndexError:
            print("Не верный ID")

    def delete_ticket(
        self,
        id_input
        ):
        data: list = self.storage.read_json()
        delete_data: list = [item for item in data if item.get('id') != id_input]
        self.storage.write_json(delete_data)

    def view_sla(self) -> list[str]:
        data: list = self.storage.read_json()
        MSK = timezone(timedelta(hours=3), "MSK")
        now: datetime = datetime.now(MSK)
        print_data: list = []
        for ticket in data:
            created_at: datetime = datetime.strptime(ticket["created_at"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=MSK)
            sla_dur = timedelta(hours=ticket["sla"])
            dl: datetime = created_at + sla_dur
            if now > dl:
                expired_ticket: str = f"Тикет ID:{ticket['id']} просрочен"
                print_data.append(expired_ticket)
            else:
                time_left: timedelta = dl - now
                ticket_left: str = f"У тикета ID:{ticket['id']} осталось: {time_left} "
                print_data.append(ticket_left)
        return print_data