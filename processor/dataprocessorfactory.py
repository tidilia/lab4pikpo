from abc import ABC, abstractmethod
from processor.dataprocessor import *
from typing import Optional
# подключаем все реализации обработчиков (DataProcessor)
import os

"""
    В данном модуле объявляются классы, реализующие фабричный метод get_processor, 
    который возвращает соответствующие классы обработчиков данных
"""

class DataProcessorFactory(ABC):
    def __init__(self):
        self.instance = None

    @abstractmethod
    def get_processor(self, datasource) -> DataProcessor:
        pass

"""
    Фабричный метод может не только возвращать класс соответствующего обработчика,
    здесь также может быть реализована логика, которая меняет поведение данного обработчика,
    например, меняет тип разделителя и кодировку для CSV-файла (через атрибуты класса),
    применяет различные режимы обработки и т.д.
"""

# Фабрика CsvDataProcessor
class CsvDataProcessorFactory(DataProcessorFactory):
    # Фабричный метод для CsvDataProcessor читает файл с сепаратором по умолчанию (;),
    # если неудачно, то читаем с сепаратором ','
    # Если все попытки чтения неудачны возвращаем None
    def get_processor(self, datasource) -> DataProcessor:
        self.instance = CsvDataProcessor(datasource)
        if self.instance.read():
            return self.instance
        elif self.read_with_separator(','):
            return self.instance
        return None

    def read_with_separator(self, sep) -> bool:
        self.instance.separator = sep
        if self.instance.read():
            return True
        return False

# Фабрика TxtDataProcessor
class TxtDataProcessorFactory(DataProcessorFactory):
    def get_processor(self, datasource) -> DataProcessor:
        self.instance = TxtDataProcessor(datasource)
        if self.instance.read():
            return self.instance
        return None

class DataProcessorFactory:
    """ Фабрика DataProcessor """
    def __init__(self):
        self._processor = None

    """
        Фабричный метод может не только возвращать класс соответствующего обработчика,
        здесь также может быть реализована логика, которая меняет поведение данного обработчика,
        например, меняет тип разделителя и кодировку для CSV-файла (через атрибуты класса),
        применяет различные режимы обработки и т.д.
    """

    def get_processor(self, datasource: str) -> Optional[DataProcessor]:
        """ Основной фабричный метод, возвращающий необходимый объект класса DataProcessor
            в зависимости от расширения файла """
        if datasource.endswith('.csv'):
            self.create_csv_processor(datasource)
        elif datasource.endswith('.txt'):
            self.create_txt_processor(datasource)
        return self._processor

    def create_txt_processor(self, datasource: str) -> None:
        """ Создаем TxtDataProcessor и пытаемся прочитать данные, если удачно, сохраняем объект в атрибуте класса """
        processor = TxtDataProcessor(datasource)
        if processor.read():
            self._processor = processor

    def create_csv_processor(self, datasource: str) -> None:
        """ Создаем CsvDataProcessor и пытаемся прочитать данные, если удачно, сохраняем объект в атрибуте класса """
        processor = CsvDataProcessor(datasource)
        if processor.read():
            self._processor = processor