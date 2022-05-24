from attr import attrs, attrib
from animal_holding_area import AnimalHoldingArea


@attrs
class Zoo(AnimalHoldingArea):
    antelope = attrib()
    bear = attrib()
    animals_list = attrib(factory=list)

    def print_animals(self) -> None:
        print(f'Antelope: {self.antelope}, Bear: {self.bear}')