import sys
import os
import time
## Importa as classes que serao usadas
sys.path.append('pkg')
sys.path.append('.')
from victims_generator import Vict_gen




def main():
    # Lê arquivo config.txt
    arq = open(os.path.join("..", "config_data","config.txt"),"r")
    configDict = {} 
    for line in arq:
        ## O formato de cada linha é:var=valor
        ## As variáveis são 
        ##  maxLin, maxCol que definem o tamanho do labirinto
        ## Tv e Ts: tempo limite para vasculhar e tempo para salvar
        ## Bv e Bs: bateria inicial disponível ao agente vasculhador e ao socorrista
        ## Ks :capacidade de carregar suprimentos em número de pacotes (somente para o ag. socorrista)

        values = line.split("=")
        configDict[values[0]] = int(values[1])

    print("dicionario config: ", configDict)

    vict = Vict_gen(configDict["maxLin"], configDict["maxCol"], 42)

        
if __name__ == '__main__':
    main()
