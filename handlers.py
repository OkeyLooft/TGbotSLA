from services import TicketServices
from storage import TicketStorage


class TicketHandlers:
    def __init__(self, storage: TicketStorage, services: TicketServices):
        self.storage = storage
        self.service = services


    def input_ticket(self):
        name: str = input("Задайте имя тикету: ")
        description: str = input("Введите описание тикета: ")
        sla = 0
        while sla <= 0:
            try:
                sla: int = int(input("Введите время выполнения: "))
                if sla <= 0:
                    print(f"Время выполнения:{sla} не может быть меньше или равно нулю")
            except ValueError:
                print(f"Неверное значение: {sla}. Значение может быть только целым числом. ")
        
        return name, description, sla

    def agree_ticket(self, name, description, sla) -> str:
        full_ticket = {
            "NAME": name,
            "DESCRIPTION": description,
            "SLA": sla
        }
        for keys, items in full_ticket:
            print(keys. items)
        user_agree = input("Все верно ?y/N: ")
        return user_agree

    def create_ticket(self):
        name, description, sla = self.input_ticket()
        self.service.create_ticket(
            name=name,
            description=description,
            sla=sla
        )
