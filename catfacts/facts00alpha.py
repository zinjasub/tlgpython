#!/usr/bin/env python3

import requests

def main():
    """Run time code"""

    r = requests.get("https://cat-fact.herokuapp.com/facts")

    print( dir(r) )

main()
