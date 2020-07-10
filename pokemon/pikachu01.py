#!/usr/bin/python3

import requests

POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    for poke in pokemon["results"]:
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

if __name__ == "__main__":
    main()

