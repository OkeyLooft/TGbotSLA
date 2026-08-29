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
    print("ID | NAME          | STATUS      | HOURS LEFT")
    print(50 * '-')