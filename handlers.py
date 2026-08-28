from services import TicketServices
from storage import TicketStorage


class TicketHandlers:
    def __init__(self, services: TicketServices):
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



    def create_ticket(self):
        while True:
            name, description, sla = self.input_ticket()

            ticket_dict: dict = {
                "NAME": name,
                "DESCRIPTION": description,
                "SLA": sla
            }

            for keys, items in ticket_dict.items():
                print(keys, items)
            
            user_agree: str = input("Все верно ? [д/н] ").lower()
            if user_agree == "д":
                break
            elif user_agree == "н":
                pass
            else:
                print("Проверьте что ввели 'д' или 'н' ")

        self.service.create_ticket(
            name=name,
            description=description,
            sla=sla
        )

ticket = TicketHandlers(TicketServices(TicketStorage()))
ticket.create_ticket()
