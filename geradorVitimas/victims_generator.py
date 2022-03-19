import random
import os

class Vict_gen:
    def __init__(self, mazeSizeX, mazeSizeY, qtdVictims):
        self.mazeSizeX = mazeSizeX
        self.mazeSizeY = mazeSizeY
        ##self.qtdVictims = random.randint(5, mazeSizeY)
        self.qtdVictims = qtdVictims
        self.posVictims = []
        self.walls = []
        self.vitalSignals = []
        self.diffAccess = []
        self.generatorVictims()
        self.savePos()
        

    def generateWalls(self):
        walls = []
        qtd = random.randint(10, self.mazeSizeX*4)
        cont = 0
        while cont < qtd:
            row = random.randint(0, self.mazeSizeX-1)
            col = random.randint(0, self.mazeSizeY-1)
            if (row > 0 or col > 0) and (row, col) not in walls:
                self.walls.append((row, col))
                cont += 1
    
    def generatorVictims(self):
        self.generateWalls()
        qtdGen = 0
        arq_gravidade = open(os.path.join(".", "gravidade.txt"), "r")
        arq_tempo = open(os.path.join(".", "temposocorro.txt"), "r")
        while qtdGen < self.qtdVictims:
            pos = (random.randint(0, self.mazeSizeX-1), random.randint(0, self.mazeSizeY-1))
            if pos not in self.posVictims and (pos not in self.walls) and pos != (0,0):
                self.posVictims.append(pos)
                g_line = arq_gravidade.readline()

                if g_line:
                    g_value = float(g_line)
                else:
                    print("faltou valor de gravidade para vitima: ", qtdGen, "\n")
                    g_value = round(random.random(),2)
                    
                self.vitalSignals.append([
                    round(random.random(),2),
                    round(random.random(),2),
                    round(random.random(),2),
                    round(random.random(),2),
                    round(random.random(),2),
                    g_value])

                t_line = arq_tempo.readline()
                if t_line:
                    ##print("read: ", t_value, " vlr: ", float(t_line))
                    t_value = float(t_line)
                else:
                    print("faltou valor de tempo de socorro para vitima: ", qtdGen, "\n")
                    t_value = round(random.random(),2)
                    
                self.diffAccess.append([
                    round(random.random(),2),
                    round(random.random(),2),
                    round(random.random(),2),
                    round(random.random(),2),
                    round(random.random(),2),
                    round(random.random(),2),
                    t_value])
                
                qtdGen += 1
                
    def savePos(self):
        arquivo = open(os.path.join(".", "new_ambiente.txt"), "w")
        strSave = "Agente 0,0\n"
        strSave += "Vitima"
        for i in self.posVictims:
            strSave += " " + str(i[0]) + "," + str(i[1])
        strSave += "\nParede"
        for i in self.walls:
            strSave += " " + str(i[0]) + "," + str(i[1])
        arquivo.writelines(strSave)
        arquivo.close()
        print("gerou new ambiente.txt\n")

        strSave=""
        sinaisvitais = open(os.path.join(".", "new_sinaisvitais.txt"), "w")
        for i in self.vitalSignals:
            strSave += str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + " " + str(i[5]) + "\n"
        sinaisvitais.writelines(strSave)
        sinaisvitais.close()
        print("gerou new sinaisvitais.txt\n")

        strSave=""
        difacesso = open(os.path.join(".", "new_difacesso.txt"), "w")
        for i in self.diffAccess:
            strSave += str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + " " + str(i[5]) + " " + str(i[6]) + "\n"
        difacesso.writelines(strSave)
        difacesso.close()
        print("gerou new difacesso.txt\n")

