from datetime import datetime
class Dataset:
    def __init__(self, dataset_id:int, name:str, rows:int, columns:int, uploaded_by:str, uploaded_date:str):
        self.__dataset_id = dataset_id
        self.__name = name
        self.__rows = rows
        self.__columns = columns
        self.__uploaded_by = uploaded_by
        self.__uploaded_date = uploaded_date
    def get_dataset_id(self) -> int:
        return self.__dataset_id
    def get_name(self) -> str:
        return self.__name
    def get_rows(self) -> int:
        return self.__rows
    def get_columns(self) -> int:
        return self.__columns
    def get_uploaded_by(self) -> str:
        return self.__uploaded_by
    def get_uploaded_date(self) -> str:
        return self.__uploaded_date
    def __str__(self) -> str:
        return f"Dataset ({self.__dataset_id}, {self.__name}, {self.__rows}, {self.__columns}, {self.__uploaded_by}, {self.__uploaded_date})" 
    