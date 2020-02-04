from access_points import *
import json
import datetime
from utils import *

def get_location():
    scanner = get_scanner()

    datetime_now = datetime.datetime.now()
    default_arg = [{'location': None, 'last_visit': datetime_now}]

    location= load_json() #location is a dictionary
    bssid_lib = location['location'][0]  #bssid_lib is a dict containing dictionaries that has bssid as keys and details as values
    bssid_now = get_bssid(scanner)
    parameter = bssid_lib.setdefault(bssid_now, default_arg)[0]
    answer = parameter['location']

    last_known_place = None
    last_known_time = None

    if answer:
        response = answer
        parameter['last_visit']=datetime_now
    else:
        response = 'A corner where no one knows'
        last_known_place, last_known_time = recent_known_visit(bssid_lib)

    print('Current location:')
    print(response+', visited at '+str(datetime_now))

    if last_known_place:
        print('--------------\n')
        print("He was in "+last_known_place+' at '+last_known_time)

    print('--------------\nJson file to write:\n')
    print(location)
    dump_json(location)
    return response, last_known_place, last_known_time

if __name__ == "__main__":
    get_location()

#print(type(bssid_lib))
#print(bssid_lib)
#bssid_lib.setdefault()
#print(location)
#print(type(location))