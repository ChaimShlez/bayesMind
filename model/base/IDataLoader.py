from abc import ABC, abstractmethod
class IDataLoader(ABC):
    def read_data(self):
        pass