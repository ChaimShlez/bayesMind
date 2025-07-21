from abc import ABC ,abstractmethod


class IExtract(ABC):
    @abstractmethod
    def extract_data(self,content):
        pass
