from attr import attrs, attrib, validators
from abc import ABC, abstractmethod


def check_area(instance, attribute, value) -> None:
    if value < 0:
        raise ValueError(f'Area must be positive number! got {value}')


@attrs
class AnimalHoldingArea(ABC):
    area = attrib(validator=[validators.instance_of(int), check_area])
    official_name = attrib()
    capacity = attrib()

    @capacity.validator
    def check_capacity(self, attribute, value):
        if value < 0:
            raise ValueError(f'Capacity must be positive number! got {value}')

    @abstractmethod
    def print_animals(self) -> None:
        raise NotImplementedError