class ITTicket:
    """Represents an IT support ticket."""

    def __init__(self, ticket_id, title, priority, status, assigned_to):
        self.__id = ticket_id
        self.__title = title
        self.__priority = priority
        self.__status = status
        self.__assigned_to = assigned_to

    def get_status(self):
        return self.__status

    def assign_to(self, staff):
        self.__assigned_to = staff

    def close_ticket(self):
        self.__status = "Closed"

    def __str__(self):
        return (
            f"Ticket {self.__id}: {self.__title} "
            f"[{self.__priority}] – {self.__status} "
            f"(assigned to {self.__assigned_to})"
        )