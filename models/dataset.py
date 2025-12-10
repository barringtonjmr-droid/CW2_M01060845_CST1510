from datetime import datetime
class Dataset:
    def __init__(self, id:int, dataset_name: str, category: str, source: str, last_updated: str, record_count: str, file_size_mb:str):
        self.__id = id
        self.__dataset_name = dataset_name
        self.__category = category
        self.__source = source
        self.__last_updated = last_updated
        self.__record_count = record_count
        self.__file_size_mb = file_size_mb
        self.__created_at = datetime.now()
    def get_id(self) -> int:
        return self.__id   
    def get_name(self) -> str:
        return self.__dataset_name
    def get_category(self) -> str:
        return self.__category
    def get_source(self) -> str:
        return self.__source
    def get_last_updated(self) -> str:
        return self.__last_updated
    def get_record_count(self) -> str:
        return self.__record_count
    def create_at(self):
        return self.__created_at
    def calculate_size_mb(self) -> float:
        return self.__file_size_mb / (1024 * 1024)
    def __str__(self) -> str:
        size_mb = self.calculate_size_mb()
        return f"Dataset ({self.__id}, {self.__dataset_name}, {self.__category}, {size_mb:.2f} MB)"