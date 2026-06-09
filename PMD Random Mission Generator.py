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
command = '450'
finished = 0
"""Stores in lists the data provided by the user"""
"Instead of opening the areas.txt twice, opens a single time and already save"
"information that will be used for both, areas and digimons"
digimonf = 'areas.txt'
f = open(digimonf,mode = 'r')
n = f.readline()
n = n.rstrip('\n')
n = n.rstrip('\n')
n = int(n)
area = area(f,n)
f.seek(0)
digimon = digimon(f,n)
f.close()
nuzlocke = list()
chosen = 'DIGIMON'
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
    """Pick one random digimon from one choosen area"""
    elif command == '1':
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
    """Pick one random digimon from each area (no duplicates will show up)"""
    elif command == '2':
        n = 0
        for item in area:
            while finished != 1:
                chosen = randomdigimongenerator(digimon,n)
                if chosen not in nuzlocke:
                   nuzlocke.append(chosen)
                   finished = 1
            finished = 0
        n = 0
        for item in nuzlocke
            print(area[n] + ' : ' + nuzlocke[n])
            print('\n')
            n = n + 1
    """Generate a random number from 1 to 6"""
    elif command == '3':
        n = int(input("Type the number of Digivolutions available for your Digimon: "))
        n = random.randint(1,n)
        print('Roll result: ' + n)
        print('\n')
    else:
        print("Unidentified command, please try again.")
        print('\n')
print("Thanks for using the Nuzlocke Assist Manager")
print("Made by KasuganoAichi(Github Username)")
time.sleep(10)
