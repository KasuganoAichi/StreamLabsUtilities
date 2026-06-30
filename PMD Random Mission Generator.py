import random

def listcommands():
    print("Below you can see a list with the available commands,")
    print("just type the number of the desired command and press Enter to run it")
    print("\n")
    print("1 - Pick a Random Digimon from specified Area")
    print("2 - Pick one Random Digimon from each Area")
    print("3 - Pick one Random Rookie Digimon from each Attribute")
    print("4 - Roll a Dice to determine Digivolution")
    print("0 - Close the Program\n")

def ler_areas(f, n):
    lista_areas = []
    read = f.readline().rstrip('\n').rstrip('\t')
    lista_areas.append(read)
    n = n - 1
    while n != 0:
        while read != 'end':
            read = f.readline().rstrip('\n').rstrip('\t')
        read = f.readline().rstrip('\n').rstrip('\t')
        lista_areas.append(read)
        n = n - 1
    return lista_areas

def ler_digimons(f, n):
    lista_digimons = []
    auxlist = []
    f.readline()
    f.readline()
    read = f.readline().rstrip('\n').rstrip('\t')
    while n != 0:
        while read != 'end':
            auxlist.append(read)
            read = f.readline().rstrip('\n').rstrip('\t')
        lista_digimons.append(auxlist)
        n = n - 1
        if n != 0:
            f.readline()
            read = f.readline().rstrip('\n').rstrip('\t')
            auxlist = []
    return lista_digimons

def randomdigimongenerator(digimon_list, n):
    x = len(digimon_list[n]) - 1
    y = random.randint(0, x)
    return digimon_list[n][y]

# --- PROGRAMA PRINCIPAL ---
end = 0
command = '450'
finished = 0

f = open('areas.txt', mode='r')
n_areas = int(f.readline().rstrip('\n'))
area_data = ler_areas(f, n_areas)
f.seek(0)
digimon_data = ler_digimons(f, n_areas)
f.close()

nuzlocke = []
x = 1
print("Hello and welcome to the Digimon Time Stranger Nuzlocke Assistant.")

while end != 1:
    print('\n')
    listcommands()
    command = input()
    print('\n')
    
    if command == '0':
        end = 1
        
    elif command == '1':
        while finished != 1:
            for item in area_data[:-3]:
                print(str(x) + ' - ' + item)
                x = x + 1
            print('\n')
            n = int(input("Type the number of area to choose from: "))
            if 0 < n < x:
                n = n - 1
                print('\n')
                chosen = randomdigimongenerator(digimon_data, n)
                print('Digimon: ' + chosen)
                finished = 1
            else:
                print("Input number out of index range, please try again")
                print('\n')
            x = 1
        finished = 0
        print('\n')
        chosen = input("Press any key to continue...")
        
    elif command == '2':
        n = 0
        for item in area_data[:-3]:
            while finished != 1:
                chosen = randomdigimongenerator(digimon_data, n)
                if chosen not in nuzlocke:
                    nuzlocke.append(chosen)
                    finished = 1
            finished = 0
            n = n + 1
        n = 0
        for item in nuzlocke:
            print(area_data[n] + ' : ' + nuzlocke[n])
            n = n + 1
        nuzlocke.clear()
        print('\n')
        chosen = input("Press any key to continue...")    
        
    elif command == '3':
        n = m = len(area_data) - 3
        for item in area_data[-3:]:
            chosen = randomdigimongenerator(digimon_data, n)
            n = n + 1
        n = m
        m = 0
        for item in nuzlocke:
            print(area_data[n] + ' : ' + nuzlocke[m])
            m = m + 1
        nuzlocke = list()
        print('\n')
        chosen = input("Press any key to continue...")    
        
    elif command == '4':
        n = int(input("Type the number of Digivolutions available for your Digimon: "))
        n = random.randint(1, n)
        print('Roll result: ' + str(n))
        print('\n')
        chosen = input("Press any key to continue")
    else:
        print("Unidentified command, please try again.")
        print('\n')
        chosen = input("Press any key to continue")

print("Thanks for using the Nuzlocke Assist Manager")
print("Made by KasuganoAichi(Github Username)")
