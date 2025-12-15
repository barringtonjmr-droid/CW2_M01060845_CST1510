from datetime import datetime
class CyberIncident:
    def __init__(self, incident_id: int, timestamp: str, severity:str, category:str, status:str, description:str):
        self.__incident_id = incident_id
        self.__date = timestamp
        self.__severity = severity
        self.__category = category
        self.__status = status
        self.__description = description
    def get_incident_id(self) -> int:
        return self.__incident_id
    def get_timestamp(self) -> str:
        return self.__date
    def get_severity(self) -> str:
        return self.__severity
    def get_category(self) -> str:
        return self.__category
    def get_status(self) -> str:
        return self.__status
    def get_description(self) -> str:
        return self.__description
    def __str__(self) -> str:
        return f"Cyber Incident ({self.__incident_id}, {self.__date}, {self.__severity}, {self.__category}, {self.__status})"