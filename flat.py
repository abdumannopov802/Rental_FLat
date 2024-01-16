import calendar

from client import Client

class Flat:
    def __init__(self, flat_code, flat_dimention, flat_type, flat_price) -> None:
        self._flat_code = flat_code
        self._flat_dimention = flat_dimention
        self._flat_price = flat_price
        self._flat_type = flat_type
        self._availablility = [0 for _ in range(52)]
    #     # self._ordered_info = [0 ]

    # def order_flat(self, client: Client):
    #     self._ordered_info.append(client)
    #     return f"{self.code}- flat {client.id}-id tomonidan band qilindi"

    @property
    def code(self):
        return self._flat_code
    @property
    def dimention(self):
        return self._flat_dimention
    @property
    def price(self):
        return self._flat_price