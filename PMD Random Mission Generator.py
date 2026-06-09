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
    print("1 - Set up a complete quest (quest title, dungeon, client, rank, reward and final enemy)")
    print("2 - Set up a random encounter")
    print("3 - Set up a quest name")
    print("4 - Set up a dungeon")
    print("5 - Set up a client")
    print("6 - Set up a difficult rank")
    print("7 - Set up a random enemy based on difficult")
    print("8 - Set up a random enemy based on location")
    print("9 - Set up a reward")
    print("0 - Close the Program\n")

"""Collect the possible quest names from the quest.txt file"""

def quest():
    questf = "quest.txt" 
    quest = list()
    read = 'm'
    f = open(questf,mode = 'r')
    read = f.readline()
    read = read.rstrip('\n')
    read = read.rstrip('\t')
    while read != '':
        quest.append(read)
        read = f.readline()
        read = read.rstrip('\n')
        read = read.rstrip('\t')
    f.close()
    return quest

"""Collect the possible dungeon names from the dungeon.txt file"""

def dungeon():
    dungeonf = 'dungeon.txt'
    dungeon = list()
    read = 'd'
    f = open(dungeonf,mode = 'r')
    read = f.readline()
    read = read.rstrip('\n')
    read = read.rstrip('\t')
    while read != '':
        dungeon.append(read)
        read = f.readline()
        read = read.rstrip('\n')
        read = read.rstrip('\t')
    f.close()
    return dungeon

"""Collect the possible clients names from the clients.txt file"""

def client():
    clientf = 'client.txt'
    client = list()
    read = 'c'
    f = open(clientf,mode = 'r')
    read = f.readline()
    read = read.rstrip('\n')
    read = read.rstrip('\t')
    while read != '':
        client.append(read)
        read = f.readline()
        read = read.rstrip('\n')
        read = read.rstrip('\t')
    f.close()
    return client

"""Collect the possible enemies names (based on difficult level) from the enemies.txt file"""

def enemies(n):
    enemiesf = 'enemies.txt'
    enemies = list()
    auxlist = list()
    read = 'e'
    f = open(enemiesf,mode = 'r')
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
        enemies.append(auxlist)
        n = n - 1
        if n != 0:
            "Ignores next line because it will be a difficult name"
            read = f.readline()
            read = f.readline()
            read = read.rstrip('\n')
            read = read.rstrip('\t')
            auxlist = list()
    f.close()
    return enemies

"""Collect the possible enemies names (by dungeon) from the enemiesbyplace.txt file"""
   
def enemiesbyplace():
   enemiesdungeonf = 'enemiesbydungeon.txt'
   enemiesdungeon = list()
   auxlist = list()
   read = 'e'
   f = open(enemiesdungeonf,mode = 'r')
   n = f.readline()
   n = n.rstrip('\n')
   n = n.rstrip('\t')
   n = int(n)
   "Collects number of dungeons then ignores next line, since it will be a dugeon name"
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
      enemiesdungeon.append(auxlist)
      n = n - 1
      if n != 0:
         "Ignores next line because it will be a dungeon name"
         read = f.readline()
         read = f.readline()
         read = read.rstrip('\n')
         read = read.rstrip('\t')
         auxlist = list()
   f.close()
   return enemiesdungeon                   
   
"""Collect the possible mental state of an enemy from the adjectives.txt (anngry, happy, scared, etc)"""

def adjectives():
   adjectivesf = 'adjectives.txt'
   adjectives = list()
   read = 'c'
   f = open(adjectivesf,mode = 'r')
   read = f.readline()
   read = read.rstrip('\n')
   read = read.rstrip('\t')
   while read != '':
      adjectives.append(read)
      read = f.readline()
      read = read.rstrip('\n')
      read = read.rstrip('\t')
   f.close()
   return adjectives

   
"""Collect the possible difficulty ranks from the reward.txt file"""

def rank(f,n):
    rank = list()
    read = 'r'
    read = f.readline()
    read = read.rstrip('\n')
    read = read.rstrip('\t')
    rank.append(read)
    n = n - 1
    while n != 0:
        while read != 'end':
            read = f.readline()
            read = read.rstrip('\n')
            read = read.rstrip('\t')
        read = f.readline()
        read = read.rstrip('\n')
        read = read.rstrip('\t')
        rank.append(read)
        n = n - 1
    return rank  
   
"""Collect the possible difficulty rewards from the reward.txt file"""   

def reward(f,n):
    reward = list()
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
        reward.append(auxlist)
        n = n - 1
        if n != 0:
            "Ignores next line because it will be a difficult name"
            read = f.readline()
            read = f.readline()
            read = read.rstrip('\n')
            read = read.rstrip('\t')
            auxlist = list()
    return reward

"""Choose random quest title only"""

def randomtitlegenerator(quest):
    x = len(quest) - 1
    y = random.randint(0,x)
    print('Quest: ' + quest[y])
   
"""Choose a random dungeon for the quest"""

def randomdungeongenerator(dungeon):
    x = len(dungeon) - 1
    y = random.randint(0,x)
    print('Dungeon: ' + dungeon[y])
    return y

"""Choose a random quest client"""

def randomclientgenerator(client):
    x = len(client) - 1
    y = random.randint(0,x)
    print('Client: ' + client[y])
      
"""Choose a random adjevtice for the enemy"""

def randomadjectivegenerator(adjectives):
    x = len(adjectives) - 1
    y = random.randint(0,x)
    return y
    
   
"""Choose a random enemy for the quest"""

def randomenemygenerator(enemies,n):
    x = len(enemies[n]) - 1
    y = random.randint(0,x)
    print('Enemy: ' + enemies[n][y])

"""Choose a random enemy for an encounter"""
def randomenemyencountergenerator(enemies,n):
    x = len(enemies[n]) - 1
    y = random.randint(0,x)
    return y

"""Choose a random difficult rank for the quest"""

def randomrankgenerator(rank):
    x = len(rank) - 1
    y = random.randint(0,x)
    print('Rank: ' + rank[y])
    return y

"""Choose a random reward for the quest"""

def randomrewardgenerator(reward,n):
    x = len(reward[n]) - 1
    y = random.randint(0,x)
    print('Reward: ' + reward[n][y])

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
"Instead of opening the reward.txt twice, opens a single time and already save"
"information that will be used for both, ranks and rewards"
rewardf = 'rewards.txt'
f = open(rewardf,mode = 'r')
n = f.readline()
n = n.rstrip('\n')
n = n.rstrip('\n')
n = int(n)
enemies = enemies(n)
rank = rank(f,n)
f.seek(0)
reward = reward(f,n)
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
            n = randomrankgenerator(rank)
            randomenemygenerator(enemies,n)
            randomrewardgenerator(reward,n)
        elif command == 2:
            randomtitlegenerator(quest)
            d = randomdungeongenerator(dungeon)
            randomclientgenerator(client)
            n = randomrankgenerator(rank)
            randomenemygenerator(enemies,d)
            randomrewardgenerator(reward,n)
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
        n = randomrankgenerator(rank)
        print('\n')
    elif command == '7':
        "Index starts at 0, thus x-1 will provide the correct placement of the item on the list"
        while finished != 1:
            for item in rank:
                strx = str(x)
                print(strx + ' - ' + rank[x-1])
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
            for item in rank:
                strx = str(x)
                print(strx + ' - ' + rank[x-1])
                x = x + 1
            n = int(input("Type the number of the difficult of the quest: "))
            if 0 < n < x:
                n = n - 1
                print('\n')
                randomrewardgenerator(reward,n)
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
