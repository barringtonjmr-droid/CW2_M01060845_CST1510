from datetime import datetime
class ITTicket:
    def __init__(self, id:int, ticket_id: int, priority: str, status: str,category:str, subject:str, description: str, created_date: str, resolved_date: str, assigned_to: str):
        self.__id = id
        self.__ticket_id = ticket_id
        self.__priority = priority
        self.__status = status
        self.__category = category
        self.__subject = subject
        self.__description = description
        self.__created_date = created_date
        self.__resolved_date = resolved_date
        self.__assigned_to = assigned_to
        self.__created_at = datetime.now()

    def get_id(self) -> int:
        return self.__id
    def get_ticket_id(self) -> int:
        return self.__ticket_id
    def get_priority(self) -> str:
        return self.__priority
    def get_status(self) -> str:
        return self.__status 
    def get_category(self) -> str:
        return self.__category
    def get_subject(self) -> str:
        return self.__subject
    def get_description(self) -> str:
        return self.__description
    def get_created_date(self) -> str:
        return self.__created_date
    def get_resolved_date(self) -> str:
        return self.__resolved_date
    def get_assigned_to(self, staff:str) -> None:
        self.__assigned_to = staff
    def close_ticket(self, resolved_date:str) -> None:
        self.__status = "Closed"
        self.__resolved_date = resolved_date
    def get_created(self):
        return self.__created_at
    def __str__(self) -> str:
        return f"Ticket {self.__ticket_id} {self.__priority} - {self.__status}  assigned to {self.__assigned_to}"