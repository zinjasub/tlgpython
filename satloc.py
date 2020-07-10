#!/usr/bin/python3
'''
this will show distance and direction to closest satellite to the user.
'''

import json
import requests

def main():
    #bring in host ip (simulate as text file for this)
    #translate host ip to location
    #bring in list of sat
 r = requests.get('https://www.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2/&apiKey=589P8Q-SDRYX8-L842ZD-5Z9')
 loc =  r.json()
 print(loc['satname'])
 print(r.json())
#Request: /positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}


    #sort by distance from host ip location

    #display distance and direction

main()
