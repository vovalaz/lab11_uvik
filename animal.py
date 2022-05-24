from dataclasses import dataclass
from abc import ABC, abstractmethod

'''Abstract class representing animals'''
@dataclass
class Animal(ABC):
    weight: float
    height: float
    age: int

    @abstractmethod
    def count_ration(self):
        raise NotImplementedError