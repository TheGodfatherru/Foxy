import json
import os


def get_data():
    data = {}
    os.system('sudo ~/pydatertc.sh')
    with open('data.txt') as file:
        for i in file.read().split('\n'):
            if not i or i.split()[-1].lower() == 'hub':
                continue
            i = i.split()
            data[i[5]] = {"Bus": i[1],
                          "Device": i[3][:-1],
                          "Name": ' '.join(i[6:])}
        return data


if __name__ == '__main__':
    with open('data.json', 'w') as data:
        json.dump(get_data(), data)
