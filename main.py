#import get_access_point
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    #response, last_location, last_time = get_access_point.get_location()
    #ans = response + '. He is last seen ' + last_location + ' at '+last_time
    #print(ans)
    return "LOL"

if(__name__=='__main__'):
    app.run()