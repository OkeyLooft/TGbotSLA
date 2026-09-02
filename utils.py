def print_header_SLA():
    print(50 * "=")
    print("SLA MONITOR")


def print_menu():
    print(50 * "=")
    print()
    print("1. Create ticket")
    print("2. Show ticket")
    print("3. Search ticket")
    print("4. Change status")
    print("5. Delete ticket")
    print("6. Check SLA")
    print("7. Exit")

def show_ticket_header():
    print("ID |NAME          |STATUS      |HOURS LEFT")
    print(50 * '-')

def menu_find_ticket():
    print(50 * '-')
    print("1. ID \n2. NAME \n3. STATUS \n4. Exit ")
    print(50 * '-')

def print_find_result(ticket):
        print("-" * 50)
        print(f"ID:          {ticket['id']}")
        print(f"NAME:        {ticket['name']}")
        print(f"DESCRIPTION: {ticket['description']}")
        print(f"CREATED AT:  {ticket['created_at']}")
        print(f"SLA:         {ticket['sla']}")
        print(f"STATUS:      {ticket['status']}")
        print("-" * 50)