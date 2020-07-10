#!/usr/bin/env python3
import requests
import json

#variables
max_year = int(2011)
while True:
    #input Year
    while True:
        y = int(input('Enter Year in YYYY format: '))
        if y <= max_year:
            print("Invalid Year. No Years older than 2011 ")
        if y > max_year:
            break 
    #input Month
    while True:
        m = int(input('Enter Month in MM format: '))
        if m not in range(3, 12):
            print("Invalid Month, pick between 03 and 11 ")
        if m in range(3, 12 ):
            break
    #input Day
    while True:
        d = int(input('Enter Day in DD format: '))
        if d not in range(1, 32):
            print("Invalid Day select 1-31 ")
        if d in range(1, 32):
            break

    #add date for game and send request
    mlb = requests.get(f'https://api.sportradar.us/mlb/trial/v7/en/games/{y}/{m}/{d}/boxscore.json?api_key=')
    #strip the json
    data = mlb.json()
    ##print out attendance, capacity, home and away team abbreviation and home and away score
    #while True:
    try:
        for game in data["league"]["games"]:
            print('')
            print(f"Venue: {game['game']['venue']['name']}")
            print('')
            print(f"Home Team: {game['game']['home']['name']}, {game['game']['home']['runs']} runs. ")  # league.games[0].game.home.name
            print(f"Away Team: {game['game']['away']['name']}, {game['game']['away']['runs']} runs. ")
            print('')
            print(f"Capacity:{game['game']['venue']['capacity']}")
            print(f"Attendance: {game['game']['attendance']} ")
        break
    except KeyError:
            input('No games on this day. Press enter to search again.')
