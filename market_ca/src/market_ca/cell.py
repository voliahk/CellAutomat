from src.market_ca.units import MapUnit


class Cell:
    PRICE_PER_MOVE = 5

    def __init__(self, unit=None):
        self.unit = unit

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, map_object):
        if map_object is not None:
            if not isinstance(map_object, MapUnit):
                raise ValueError("\'unit\' must be an instance of MarketUnit or its subclass!")
        self._unit = map_object
