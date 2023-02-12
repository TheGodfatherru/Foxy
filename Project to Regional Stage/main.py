from app import application
from get_data import get_data
from hashlib import md5

while True:
    if a := get_data():
        application(device_id=md5(a[-1].encode()).hexdigest(), device_type=a[0]['Type'], device_name=a[0]['Name'])
