from worker import Worker
from manager import Manager
from Contractor import Contractor

employee1 = Worker(123, 'liza', 'tel aviv', 24, 55, 78)
print(employee1)

employee2 = Manager(867, 'Adi', 'hedera', 67, 96, 120)
print(employee2)

employee3 = Contractor(7878, 'hagag', 'TLV', 50, 70000, 8876)
print(employee3)
