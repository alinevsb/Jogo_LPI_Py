import console
import prj

def exibirMenu():
    print("    PEGUE O PORCO!!\n")
    print("MENU INICIAL DO JOGO")
    print("1 - JOGAR")
    print("2 - INSTRUÇÕES")
    print("3 - SAIR")
    print("Escolha uma opcao: ", end='')

while True:
    opcao = 0
    while (opcao != 1 and opcao != 2 and opcao != 3):
        console.clear()
        exibirMenu()
        try:
            opcao = int(input())
        except:
            opcao = 0

    if (opcao == 1):
        console.clear()
        console.pause()
        prj.jogar()
    elif (opcao == 2):
        console.clear()
        print('Instruções:')
        print('Aperte Q para aumentar o angulo de lançamento.\n')
        print('Aperte A para diminuir o angulo de lançamento.\n')
        print('Aperte W para subir a posição do canhao.\n')
        print('Aperte S para descer a posição do canhao.\n')
        print('Aperte ESPAÇO para atirar\n')
        console.pause()
    else:
        print("Bye bye!")
        exit(0)