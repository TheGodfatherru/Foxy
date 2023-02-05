import hashlib
from get_data import get_data
while True:
    with open('ids.txt') as file:
        file = set(file.read().split())
        a = get_data()
        for i in a.keys():
            if hashlib.md5(i.encode()).hexdigest() not in file:
                print("ERORR")
                exit(0)