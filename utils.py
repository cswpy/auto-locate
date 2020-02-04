import json 
from access_points import *

def get_bssid(scanner):
    return scanner.get_access_points()[0]['bssid']

def load_json():
    with open('location.json','r') as f:
        location = json.load(f)
    return location

def dump_json(dict):
    with open('location.json','w') as f:
        json.dump(dict,f,indent=4,default=str)

def recent_known_visit(dict):
    recent_time="0"
    for bssid in dict:
        time = dict[bssid][0]['last_visit']
        loc = dict[bssid][0]['location']
        if time and loc and str(time)>recent_time:
            recent_time=time
            recent_loc=loc
    return recent_loc,recent_time
