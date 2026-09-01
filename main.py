import utils
from handlers import TicketHandlers
from services import TicketServices
from storage import TicketStorage


def main():
    utils.print_header_SLA()

    ticket = TicketHandlers(TicketServices(TicketStorage()))

    actions: dict = {
        "1": ticket.create_ticket,
        "2": ticket.show_ticket,
        "3": ticket.find_ticket,
        "4": ticket.change_ticket,
        "5": ticket.delete_ticket,
        "6": ticket.view_sla
}   
    while True:
        utils.print_menu()
        choice: str = input("Выберите вариант из меню: ")
        if choice == "7":
            break
        action = actions.get(choice)
        if action:
            action()
            input("Нажмите любую кнопку что бы продолжить...")
        else:
            print("Проверьте что ввели верный номер из меню.") 

if __name__ == "__main__":
    main()   
