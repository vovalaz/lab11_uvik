from bear import Bear
from antelope import Antelope
from zoo import Zoo


bear1 = Bear(80, 150, 16, 100)
print(bear1)
antelope1 = Antelope(60, 160, 11, 9)
print(antelope1)


zoo = Zoo(area=1234, official_name="abcdefgh",
          capacity=40, antelope=antelope1, bear=bear1)
print(zoo)