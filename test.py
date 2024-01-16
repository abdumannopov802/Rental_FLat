from manager import Manager
from flat import Flat
from client import Client

manager1 = Manager()
flat1 = Flat(100, 80, "single", 1000)
client1 = Client('Ali', 'Aliyev', 1)

print(manager1.new_Flat(flat1))
print(manager1.new_Client(client1))
print(manager1.get_Clients())
print(manager1.get_Flat(10))
print(manager1.set_Tariff("High"))
print(manager1.get_Tariffs())
print(manager1.book_Flat(100, 1, 7))
print(manager1.new_Flat())
