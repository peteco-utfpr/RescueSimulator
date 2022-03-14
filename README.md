# RescueSimulator
Projeto em Python que simula vítimas dispersas em um ambiente com paredes

**Autores**
Luan Carlos Klein & Cesar Augusto Tacla
UTFPR, Câmpus Curitiba, grupo PET ENGENHARIA DE COMPUTAÇÃO

**RESCUE SIMULATOR**
Permite construir um ambiente na forma de um labirinto onde há um agente. A arquitetura do agente é baseada no modelo BDI (Beliefs, Desires and Intentions). 
O agente possui um ciclo de raciocínio e a cada iteração recebe percepções do ambiente por meio dos seus sensores, processa estas percepções para verificar o estado atual do ambiente e construir uma representação do estado atual do ambiente. Com esta representação atualizada e com suas crenças (fornecidas pelo programador ou inferidas), delibera sobre a próxima ação que o levará mais próximo do estado objetivo. Tendo escolhido a ação, o agente atua no ambiente modificando o estado deste último. A partir daí o ciclo se reinicia.

**PARA RODAR**
Basta baixar o código na sua máquina e executar o main.py.
Um agente anda aleatoriamente em um ambiente a procura de vítimas. Quando encontra alguma, lê os sinais vitais e imprime na tela. 
O processo de deliberação também pode ser acompanhado por prints na tela.

Ver o RescueSimulator.pdf para maiores detalhes.
