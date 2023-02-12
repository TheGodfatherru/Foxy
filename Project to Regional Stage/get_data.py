import os
import re
from hashlib import md5


def get_data() -> tuple[dict, str]:
    data = {}
    os.system('lsusb > data.txt')
    with open('data.txt') as file, open('ids.txt') as ids:
        for i in file.read().strip().split('\n'):
            if 'hub' in i.lower():
                continue
            i = re.split(' ', i, 6)
            data[i[5]] = {'Bus': i[1],
                          'Device': i[3][:-1],
                          'Type': 'Mouse' if 'Mouse' in i[-1] else 'Keyboard' if 'Keyboard' in i[-1]
                          else 'Flash Drive' if 'Flash Drive' in i[-1] else 'Undefined',
                          'Name': i[-1]
                          }
        ids = set(ids.read().split(';'))
        for k in data.keys():
            if md5(k.encode()).hexdigest() not in ids:
                return data[k], k


if __name__ == '__main__':
    print(get_data())
