"""THIS PROGRAM ONLY USE IS TO GENERATE THE TITLE OF A RANDOM QUEST/ENCOUNTER
   FOR POKEMON MYSTERY DUNGEON STYLE GAMES, IT WILL NOT GENERATE ENEMIEs
   POKEMON FOR YOU, IT WILL NOT GENERATE DETAILS OF THE QUEST, IT WILL
   NOT GENERATE RANDOM ENCOUNTERS"""

"""Import random functions to the program"""

import random

"""Prints on screen a list of the available commands
   for the user"""

def listcommands():
    print("Hello and welcome to the random quest generator.")
    print("Below you can see a list with the available commands,")
    print("just type the number of the desired command and press Enter to run it")
    print("1 - Pick a Random Digimon from specified Area")
    print("2 - Pick one Random Digimon from each Area")
    print("3 - Roll a Dice to determine Digivolution")
    print("0 - Close the Program\n")

"""Collect the possible difficulty areas from the areas.txt file"""

def area(f,n):
    area = list()
    read = 'r'
    read = f.readline()
    read = read.rstrip('\n')
    read = read.rstrip('\t')
    area.append(read)
    n = n - 1
    while n != 0:
        while read != 'end':
            read = f.readline()
            read = read.rstrip('\n')
            read = read.rstrip('\t')
        read = f.readline()
        read = read.rstrip('\n')
        read = read.rstrip('\t')
        area.append(read)
        n = n - 1
    return area  
   
"""Collect the possible difficulty digimons from the areas.txt file"""   

def digimon(f,n):
    digimon = list()
    auxlist = list()
    read = 'r'
    "the first two lines are irrevelant, they contain the number of difficulties and the first difficult name"
    read = f.readline()
    read = f.readline()
    read = f.readline()
    read = read.rstrip('\n')
    read = read.rstrip('\t')
    while n != 0:
        while read != 'end':
            auxlist.append(read)
            read = f.readline()
            read = read.rstrip('\n')
            read = read.rstrip('\t')
        digimon.append(auxlist)
        n = n - 1
        if n != 0:
            "Ignores next line because it will be a difficult name"
            read = f.readline()
            read = f.readline()
            read = read.rstrip('\n')
            read = read.rstrip('\t')
            auxlist = list()
    return digimon

"""Choose a random difficult area for the quest"""

def randomareagenerator(area):
    x = len(area) - 1
    y = random.randint(0,x)
    print('area: ' + area[y])
    return y

"""Choose a random digimon for the quest"""

def randomdigimongenerator(digimon,n):
    x = len(digimon[n]) - 1
    y = random.randint(0,x)
    print('digimon: ' + digimon[n][y])

"""START OF THE MAIN PROGRAM"""
"""Flow control variables"""
end = 0
command = '810'
finished = 0
"""Stores in lists the data provided by the user"""
quest = quest()
dungeon = dungeon()
client = client()
adjectives = adjectives()
enemiesbyplace = enemiesbyplace()
"Instead of opening the areas.txt twice, opens a single time and already save"
"information that will be used for both, areas and digimons"
digimonf = 'areas.txt'
f = open(digimonf,mode = 'r')
n = f.readline()
n = n.rstrip('\n')
n = n.rstrip('\n')
n = int(n)
enemies = enemies(n)
area = area(f,n)
f.seek(0)
digimon = digimon(f,n)
f.close()
"""Extra variables"""
n = 0
x = 1
y = 0
"""Print the user commands on screen"""
listcommands()

while end != 1:
    command = input()
    if command == '0':
        end = 1
    elif command == '1':
        print("Type 1 to pick the final enemy based on the quest difficult")
        print("Type 2 to pick the final enemy based on the dungeon\n")
        command = input()
        if command == 1:
            randomtitlegenerator(quest)
            d = randomdungeongenerator(dungeon)
            randomclientgenerator(client)
            n = randomareagenerator(area)
            randomenemygenerator(enemies,n)
            randomdigimongenerator(digimon,n)
        elif command == 2:
            randomtitlegenerator(quest)
            d = randomdungeongenerator(dungeon)
            randomclientgenerator(client)
            n = randomareagenerator(area)
            randomenemygenerator(enemies,d)
            randomdigimongenerator(digimon,n)
    elif command == '2':
        while finished != 1:
            "Index starts at 0, thus x-1 will provide the correct placement of the item on the list"
            for item in dungeon:
                strx = str(x)
                print(strx + ' - ' + dungeon[x-1])
                x = x + 1
            n = int(input("Type the number of the dungeon where the event takes place: "))
            if 0 < n < x:
                n = n - 1
                y = randomenemyencountergenerator(enemiesbyplace,n)
                x = randomadjectivegenerator(adjectives)
                print("While exploring through the " + dungeon[n]
                      + " the group encountered a(n) " +
                      adjectives[x] + " " + enemiesbyplace[n][y])
                finished = 1
            else:
                print("Input number out of index range, please try again")
            x = 1
        finished = 0
    elif command == '3':
        randomtitlegenerator(quest)
        print('\n')
    elif command == '4':
        randomdungeongenerator(dungeon)
        print('\n')
    elif command == '5':
        randomclientgenerator(client)
        print('\n')
    elif command == '6':
        n = randomareagenerator(area)
        print('\n')
    elif command == '7':
        "Index starts at 0, thus x-1 will provide the correct placement of the item on the list"
        while finished != 1:
            for item in area:
                strx = str(x)
                print(strx + ' - ' + area[x-1])
                x = x + 1
            n = int(input("Type the number of the difficult of the quest: "))
            if 0 < n < x:
                n = n - 1
                print('\n')
                randomenemygenerator(enemies,n)
                print('\n')
                finished = 1
            else:
                print("Input number out of index range, please try again")
            x = 1
        finished = 0
    elif command == '8':
        "Index starts at 0, thus x-1 will provide the correct placement of the item on the list"
        while finished != 1:
            for item in dungeon:
                strx = str(x)
                print(strx + ' - ' + dungeon[x-1])
                x = x + 1
            n = int(input("Type the number of the dungeon where the enemy lives: "))
            if 0 < n < x:
                n = n - 1
                print('\n')
                randomenemygenerator(enemiesbyplace,n)
                print('\n')
                finished = 1
            else:
                print("Input number out of index range, please try again")
            x = 1
        finished = 0
    elif command == '9':
        while finished != 1:
            for item in area:
                strx = str(x)
                print(strx + ' - ' + area[x-1])
                x = x + 1
            n = int(input("Type the number of the difficult of the quest: "))
            if 0 < n < x:
                n = n - 1
                print('\n')
                randomdigimongenerator(digimon,n)
                print('\n')
                finished = 1
            else:
                print("Input number out of index range, please try again")
            x = 1
        finished = 0
    else:
        print("Unidentified command, please try again.")
        print('\n')
print("Thanks for using the Random Quest Generator")
print("Made by KasuganoAichi(Github Username)")
time.sleep(10)
