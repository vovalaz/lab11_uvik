from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Animal(ABC):
    weight: float
    height: float
    age: int

    @abstractmethod
    def count_ration(self):
        raise NotImplementedError