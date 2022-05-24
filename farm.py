from attr import attrs, attrib
from animal_holding_area import AnimalHoldingArea


@attrs
class Farm(AnimalHoldingArea):
    antelope1 = attrib()
    antelope2 = attrib()
    animals_list = attrib(factory=list)

    def print_animals(self) -> None:
        print(f'Antelope1: {self.antelope1}, Antelope2: {self.antelope2}')