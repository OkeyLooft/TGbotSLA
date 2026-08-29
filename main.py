import utils
from handlers import TicketHandlers
from services import TicketServices
from storage import TicketStorage


def main():
    utils.print_header_SLA()

    ticket = TicketHandlers(TicketServices(TicketStorage()))
    service = TicketServices()

    actions = {
        "1": ticket.create_ticket,
        "2": service.show_ticket
}   
    
