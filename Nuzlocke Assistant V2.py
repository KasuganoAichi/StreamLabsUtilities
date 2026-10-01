import random
import tkinter as tk
from tkinter import ttk



#Versão com interface gráfica e mudanças no código, eventualmente serão criados
#módulos como para reduzir ainda mais o tamanho do códgio dentro de cada arquivo
#a versão original ficará em um arquivo separada, como um backup de uma versão funcional
#até que está versão esteja concluída e pronta para uso.




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
        while read != 'end' and read != '':
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
        while read != 'end' and read != '':
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

# --- Classe para interface ---
end = 0
command = '450'
finished = 0

f = open('areas.txt', mode='r')
n_areas = int(f.readline().rstrip('\n'))
area_data = ler_areas(f, n_areas)
f.seek(0)
digimon_data = ler_digimons(f, n_areas)
f.close()
class AppRandomizador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assistente para Nuzlocke Time Stranger.")
        self.geometry("500x500")
        self.criar_widgets()

    def criar_widgets(self):
        #Título da Janela
        self.lb_windowtitle = tk.Label(self, text="Digimon Time Stranger Nuzlocke Assistant")
        self.lb_windowtitle.grid(row=0,column=1)

        #Linha 1 - Randomizar uma área
        self.lb_specificarea = tk.Label(self, text="Pick a Random Digimon from a chosen area: ")
        self.lb_specificarea.grid(row=1,column=0, sticky="w")
        
        self.cb_areas = ttk.Combobox(self, values=area_data[:-3], state="readonly")
        self.cb_areas.grid(row=1,column=1,pady=5)
        
        #Linha 2 - Randomizar uma área resultado/botão
        self.lb_res_specificarea = tk.Label(self, text="")
        self.lb_res_specificarea.grid(row=2,column=0,pady=5)
        self.bt_specificarea = tk.Button(self, text="Roll")
        self.bt_specificarea.grid(row=2,column=1,pady=5)
        
        #Linha 3 - Randomizar todas as aréas
        self.lb_allareas = tk.Label(self, text="Pick one Random Digimon from each area: ")
        self.lb_allareas.grid(row=3,column=0,pady=5, sticky="w")
        self.bt_allareas = tk.Button(self, text="Roll")
        self.bt_allareas.grid(row=3,column=1,pady=5)
        
        #Linha 4 - Randomizar os iniciais
        self.lb_starters = tk.Label(self, text="Pick one Random Rookie Digimon from each Attribute: ")
        self.lb_starters.grid(row=4,column=0,pady=5, sticky="w")
        self.bt_starters = tk.Button(self, text="Roll")
        self.bt_starters.grid(row=4,column=1,pady=5)
        
        #Linha 5 - Randomizar Digievoluções
        self.lb_digivolution = tk.Label(self, text="Inform the number of available Digivolutions: ")
        self.lb_digivolution.grid(row=5,column=0,pady=5, sticky="w")
        self.entry_digivolution = tk.Entry(self)
        self.entry_digivolution.grid(row=5,column=1,pady=5)
        
        #Linha 6 - Randomizar Digievoluções resultado/botão
        self.lb_res_digivolution = tk.Label(self, text="")
        self.lb_res_digivolution.grid(row=6,column=0,pady=5)
        self.bt_digivolution = tk.Button(self, text="Roll")
        self.bt_digivolution.grid(row=6,column=1,pady=5)
        
        #Linha 7 - Fechar o programa
        self.bt_close = tk.Button(self, text="Close Program")
        self.bt_close.grid(row=7,column=0,pady=5)
        
        #Linha 8 - Créditos
        self.lb_credits = tk.Label(self, text="Made by KasuganoAichi")
        self.lb_credits.grid(row=8,column=0,pady=5)
        


# --- PROGRAMA PRINCIPAL ---

randomizador = AppRandomizador()

randomizador.mainloop()