from collections import namedtuple

Device = namedtuple('Device', ['devicetype', 'model'])

device1 = Device(**{'devicetype': 'keyboard', 'model': 'Logitech G213'})
device2 = Device(*{'devicetype': 'keyboard', 'model': 'Logitech G213'})

print(*device1, sep=', ')
print(*device2, sep=', ')
