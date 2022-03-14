import random
import os

class Victmins_gen:
    def __init__(self, mazeSizeX, mazeSizeY):
        self.mazeSizeX = mazeSizeX
        self.mazeSizeY = mazeSizeY
        self.qtdVictims = random.randint(5, mazeSizeY)
        self.posVictims = []
        self.walls = []
        self.vitalSignals = {}
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
        while qtdGen < self.qtdVictims:
            pos = (random.randint(0, self.mazeSizeX), random.randint(0, self.mazeSizeY))
            if pos not in self.posVictims and (pos not in self.walls) and pos != (0,0):
                self.posVictims.append(pos)
                self.vitalSignals[str(pos)] = [
                    round(random.random()*5,2),
                    round(random.random()*5,2),
                    round(random.random()*5,2),
                    round(random.random()*5,2),
                    round(random.random()*5,2),
                    round(random.random()*5,2),
                    round(random.random()*5,2)]
                qtdGen += 1
    def savePos(self):
        arquivo = open(os.path.join("pkg","mesh", "loads", "victimsMaze.txt"), "w")
        strSave = "Robô 0,0\n"
        strSave += "Vitima"
        for i in self.posVictims:
            strSave += " " + str(i[0]) + "," + str(i[1])
        strSave += "\nParede"
        for i in self.walls:
            strSave += " " + str(i[0]) + "," + str(i[1])
        arquivo.writelines(strSave)
        arquivo.close()

