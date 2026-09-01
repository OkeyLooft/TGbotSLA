from datetime import datetime, timedelta, timezone

import utils
from services import TicketServices


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

    def show_ticket(self) -> None:
        utils.show_ticket_header()
        data: list = self.service.show_ticket()
        for d in data:
            id_: int = d["id"]
            name: str = d["name"]
            status: str = d["status"]
            hours_left: timedelta = d["hours_left"]
            print(f"{id_:<3}|{name:<15}|{status:<13}|{hours_left}")


    def choice_find_status(self) -> str:
        status_menu: dict = {
            "1": "OPEN",
            "2": "IN_PROGRESS",
            "3": "CLOSED",
            "4": "EXPIRED",
            "5": "Exit"
        }
        while True:
            print("1. OPEN\n2. IN_PROGRESS\n3. CLOSED\n4. EXPIRED\n5. Exit")
            choice_status: str = input("Введите номер варианта из меню: ")
            choice_status_find: str = status_menu.get(choice_status)
            if choice_status_find:
                status_find: str = choice_status_find
                break
            else:
                print("Проверьте что ввели правильный номер варианта.")
        return status_find

    
    def choice_find_menu(self) -> str:
        menu: dict = {
            "1": "ID",
            "2": "NAME",
            "3": "STATUS",
            "4": "Exit"
        }
        while True:
            utils.menu_find_ticket()
            choice_menu: str = input("Введите номер варианта поиска: ")
            choice_menu_find: str = menu.get(choice_menu)
            if choice_menu_find:
                menu_find:str = choice_menu_find
                break
            else:
                print("Проверьте что ввели правильный номер варианта.")
        return menu_find
                    
    
    def find_ticket(self):
        while True:
            menu_find:str = self.choice_find_menu()
            if menu_find == "Exit":
                break
            elif menu_find == "STATUS":
                while True:
                    value: str = self.choice_find_status()
                    if value == "Exit":
                        break
                    else:
                        data_by_find: list = self.service.find_ticket(
                            menu_find=menu_find,
                            value=value
                        )
                        self.find_ticket_print(data_by_find)
            else:
                value: str = input(f"Введите {menu_find}")
                data_by_find: list = self.service.find_ticket(
                    menu_find=menu_find,
                    value=value
                )
                self.find_ticket_print(data_by_find)
    
    def find_ticket_print(self, data_by_find):
        for ticket in data_by_find:
            utils.print_find_result(ticket)
        input("Нажмите любую клавишу для продолжения... ")

    def change_ticket(self):
        status_menu: dict = {
            "1": "OPEN",
            "2": "IN_PROGRESS",
            "3": "CLOSED",
            "4": "EXPIRED",
            "5": "Exit"
        }
        id_input: int = int(input("Введите номер таска"))
        while True:
            print(50 * '-')
            print("1. OPEN \n2. IN_PROGRESS \n3. CLOSED \n4. EXPIRED \n5. Exit")
            change_input: str = input("Введите номер статуса на который вы хотите изменить таск: ")
            if change_input == "5":
                break
            change_menu: str = status_menu.get(change_input)
            if change_menu is None:
                print("Вы ввели неверное значение. Проверьте что ввели значение 1-5")
            else:
                ticket = self.service.change_ticket(
                    change_menu=change_menu,
                    id_input=id_input
                )
                print(f"Итоговый вид таска: {ticket}")
                
    def delete_ticket(self):
        while True:
            id_input: str = input("Введите ID таска для удаления(или Q): ").lower()
            if id_input == "q":
                break
            while True:
                try:
                    id_input = int(id_input)
                    break
                except ValueError:
                    print("Проверьте что ввели верный номер тикета")
                    id_input: str = input("Введите ID таска для удаления(или Q): ").lower()
            if id_input >= 0:
                ticket = self.service.show_ticket_by_id(id_input=id_input)
                print(ticket)
                user_agree: str = input("Вы уверены ? [д/н] ")
                if user_agree == "н":
                    continue
                elif user_agree == "д":
                    self.service.delete_ticket(id_input=id_input)
                else:
                    print("Проверьте написание [д/н].")

    def view_sla(self):
        expired_ticket, ticket_left = self.service.view_sla()
        print(expired_ticket)
        print(ticket_left)



            
