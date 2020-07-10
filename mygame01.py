#!/usr/bin/python3

def showInstructions():
    print('''

RPG Game

========

Commands:
  go [direction]
  get [item]
''')

def showStatus():

    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))

    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

inventory = []

rooms = {

            'Hall' : { 
                  'south' : 'Kitchen'
                },

            'Kitchen' : {
                  'north' : 'Hall'
                }

         }

currentRoom = 'Hall'

showInstructions()

while True:

    showStatus()
    move = ' '
    while move == ' ':
     move = input('>')

    move = move.lower().split(" ", 1)

if move[0] == 'go':
    if move[1] in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][move[1]]

    else:
        print('You can\'t go that way!')

    if move[0] == 'get' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']

        else:
            print('Can\'t get ' + move[1] + '!')

