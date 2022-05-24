from __future__ import annotations
from dataclasses import dataclass
from animal import Animal


@dataclass
class Antelope(Animal):
    speed: float

    @classmethod
    def make_with_speed_multiplier(cls: type, params: dict) -> Antelope:
        return cls(params['weight'],
                   params['height'],
                   params['age'],
                   params['speed']*params['multiplier'])

    def count_ration(self) -> float:
        return self.weight * 0.01


def check_area(instance, attribute, value) -> None:
    if value < 0:
        raise ValueError(f'Area must be positive number! got {value}')