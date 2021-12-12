from worker import Worker
from manager import Manager
from Contractor import Contractor

employee1 = Worker(123, 'liza', 'tel aviv', 1997, 55, 78)
print(employee1)

employee2 = Manager(867, 'Adi', 'hedera', 1993, 96, 120)
print(employee2)

employee3 = Contractor(7878, 'hagag', 'TLV', 1960, 70000, 8876)
print(employee3)
