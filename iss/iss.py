#!/usr/bin/env python3
import requests
from time import ctime


#  https://maps.google.com/maps/api/js?sensor=false&fake=.js#downloadJSON=true

def main():
    print("Where is the ISS now?")

    location = requests.get('http://api.open-notify.org/iss-now.json')

    isspos = location.json()
    
    lat = isspos['iss_position']['latitude']
    lon = isspos['iss_position']['longitude']
    
    time = ctime(isspos['timestamp'])
    
    print(time)

    print(isspos['timestamp'])
    
    print(lat + " " + lon)

    


if __name__ == "__main__":
    main()
