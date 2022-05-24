from __future__ import annotations
from dataclasses import dataclass
from animal import Animal
from functools import singledispatch


@dataclass(repr=False)
class Bear(Animal):

    hibernation_period: int = 90

    def add_hibernation_days(cls: type, additional_hibernation: int) -> None:
        cls.hibernation_period += additional_hibernation

    add_hibernation_days = classmethod(add_hibernation_days)

    def count_ration(self) -> float:
        return self.weight * 0.02

    def __str__(self) -> str:
        return f'Bear[weight: {self.weight}, height: {self.height}, \
age: {self.age}, hibernation_period: {self.hibernation_period}]'

    def __repr__(self) -> str:
        return f'Bear(weight={self.weight}, height={self.height}, \
age={self.age}, hibernation_period={self.hibernation_period})'

    def __lt__(self, sec_obj: Bear) -> bool:
        return self.age < sec_obj.age

    def __gt__(self, sec_obj: Bear) -> bool:
        return self.age > sec_obj.age

    def __eq__(self, sec_obj: Bear) -> bool:
        return all(self.weight == sec_obj.weight,
                   self.height == sec_obj.height,
                   self.age == sec_obj.age,
                   self.hibernation_period == sec_obj.hibernation_period)

    @singledispatch
    def __add__(self, sec_obj: Bear) -> Bear:
        return Bear(self.weight + sec_obj.weight,
                    self.height,
                    self.age,
                    self.hibernation_period)

    @__add__.register
    def _(self, sec_obj: float) -> Bear:
        return Bear(self.weight + sec_obj,
                    self.height,
                    self.age,
                    self.hibernation_period)

    @__add__.register
    def _(self, sec_obj: int) -> Bear:
        return Bear(self.weight,
                    self.height,
                    self.age,
                    self.hibernation_period + sec_obj)

    def __copy__(self) -> Bear:
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        return newone