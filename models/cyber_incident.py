from datetime import datetime
class Cyber_Incident:
    def __init__(self, incident_id: int, date: str, incident_type:str, severity:str, status:str, description:str, reported_by:str):
        self.__incident_id = incident_id
        self.__date = date
        self.__incident_type = incident_type
        self.__severity = severity
        self.__status = status
        self.__description = description
        self.__reported_by = reported_by
        self.__created_at = datetime.now()
    
    def get_id(self) -> int:
        return self.__incident_id
    def get_date(self) -> str:
        return self.__date
    def get_type(self) -> str:
        return self.__incident_type
    def get_severity(self) -> str:
        return self.__severity
    def update_status(self, new_status: str) -> None:
        self.__status = new_status
    def get_description(self) -> str:
        return self.__description
    def get_reported(self) -> str:
        self.__reported_by
    def get_created(self):
        return self.__created_at
   
    def get_severity_level(self) -> int:
        """Return an integer severity level (simple example)."""
        mapping = {
        "low": 1,
        "medium": 2,
        "high": 3,
        "critical": 4,
        }
        return mapping.get(self.__severity.lower(), 0)

    def __str__(self) -> str:
        return f"Incident {self.__id} [{self.__severity.upper()}] {self.__status}"
