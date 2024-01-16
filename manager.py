from flat import Flat
from client import Client
from datetime import datetime

class Manager:
    def __init__(self) -> None:
        self.flat_list: list[Flat] = []
        self.client_list: list[Client] = []
        self.orderedFlats_list = []
        self.tariffs_list = [{"High" : []}, {"Middle" : []}, {"Low" : []}]

    def new_Flat(self, new_flat: Flat): ###
            self.flat_list.append(new_flat)
            return new_flat

    def set_Tariff(self, tariff_name): ###
        for tarif in self.get_Tariffs():
            if tariff_name not in tarif.keys():
                return f"Yangi tariff qo'shib bo'lmadi. {tariff_name} <- nomdagi triff allaqachon mavjud."
        new_tariff = { tariff_name : [] } 
        self.tariffs_list.append(new_tariff)
        return new_tariff

    def get_Tariffs(self): ###
        if self.tariffs_list != []:
            return self.tariffs_list
        else:
            return f"Tizimda tariflar hali mavjud emas!"

    def new_Client(self, client: Client): ###
        self.client_list.append(client)
        return client
    
    def get_Client(self, id): ###
        for client in self.client_list:
            if client.id == id:
                 return client
        return f"ID: {id} client mavjud emas"
    
    def get_Clients(self): ###
        if self.client_list != []:
            return self.client_list
        else:
            return "Tizimda hali mijozlar mavjud emas!"
        
    def get_Flat(self, flat_code): ###
        for flat in self.flat_list:
            if flat.code == flat_code:
                return flat
            else:
                return f"Code: {flat_code} raqamli hona mavjud emas"
            
    def book_Flat(self, flat_code, client_id, duration):
        flat: Flat = self.get_Flat(flat_code)
        client: Client = self.get_Client(client_id)
        if flat != f"Code: {flat_code} raqamli hona mavjud emas":
            if client != f"ID: {id} client mavjud emas":
                get = f"Band qilingan hona - {flat.code} \nBand qilingan sana - {datetime.now()} \nDavomiylik davri - {duration}"
                client.flat_list.append([get])
                return get
            else:
                return f"ID: {id} client mavjud emas"
        else:
            return f"Code: {flat_code} raqamli hona mavjud emas"