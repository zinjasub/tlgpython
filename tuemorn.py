#!/usr/bin/env python3
import requests
import sys
import json
import webbrowser

#add date for game and send request
nhl = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

if nhl.status_code == 200:
    game = nhl.json()
else:
    print(f'invalid request - response code {nhl.status_code}')
    sys.exit("Unable to process response") # only ditch if the response is not a 200 code


#input nhl team 3 letter abbreviation
abrv = input("NHL Team Abbreviation: ")


#match inputed nhl 3 letter abbreviation and open team url
for team in game['teams']:
    if abrv == team['abbreviation']:
        print("you have a match")
        webbrowser.open(team['officialSiteUrl'])
  # print(team)
   # for abbreviation in teams:
    #    if abrv == abbreviation
     #   webbrowser.open("officialSiteUrl")

    
