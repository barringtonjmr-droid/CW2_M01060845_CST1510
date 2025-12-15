from datetime import datetime
class ITTicket:
    def __init__(self, ticket_id:int, priority:str, description:str, status:str, assigned_to:str, created_at:str, resolution_time_hours:int):
        self.__ticket_id = ticket_id
        self.__priority = priority
        self.__description = description
        self.__status = status
        self.__assigned_to = assigned_to
        self.__created_at = created_at
        self.__resolution_time_hours = resolution_time_hours
    
    def get_ticket_id(self) -> int:
        return self.__ticket_id
    def get_priority(self) -> str:
        return self.__priority
    def get_description(self) -> str:
        return self.__description
    def get_status(self) -> str:
        return self.__status
    def get_assigned_to(self) -> str:
        return self.__assigned_to
    def get_created_at(self) -> str:
        return self.__created_at
    def get_resolution_time_hours(self) -> int:
        return self.__resolution_time_hours
    def __str__(self) -> str:
        return f"IT Ticket ({self.__ticket_id}, {self.__priority}, {self.__status}, {self.__assigned_to}, {self.__created_at})"

    