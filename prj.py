from console import *
from time import sleep
from random import randrange
from jogoConst import *
from jogoMath import solve1, solve2

def jogar(): #talvez pedir o nome do jogador...

    dif = 0
    while (dif != 1 and dif != 2 and dif!= 3):
        clear()
        print("Configuracoes do JOGO:")
        print("- Dificuldade:\n  1 - Difícil\n  2 - Médio\n  3 - Fácil")
        try: 
            dif = int(input('Qual a dificuldade desejada? '))
        except: 
            dif = 0
        clear()

    pause()
    init(LIMITE_VERT)
    #gotoxy(0, 0)
    #print('▬' * LIMITE, end='', flush=True)
    gotoxy(0, LIMITE_VERT)
    print('▬' * LIMITE, end='', flush=True)
    gotoxy(1, LIMITE_VERT - 4)
    print('▬' * LIMITE, end='', flush=True)
    gotoxy((LIMITE / 2) - 5, 0)
    print("Pontos:", end='', flush=True)
    gotoxy((LIMITE / 2) - 5, LIMITE_VERT - 3)
    print("Vidas:", end='', flush=True)
    input()

    passaros = [ {"img": "^v^", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C":0} },
                {"img": "^v^", "x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C":0} } ]

    prqn = [ { "img":"^(oo)^", "x":0, "y":0, "ativo": False }, #porquinho 1, 2, 3, 4, 5 (não possuem trajetoria)// a gente pode trocar a imagem...
             { "img":"^(oo)^", "x":0, "y":0, "ativo": False },
             { "img":"^(oo)^", "x":0, "y":0, "ativo": False },
             { "img":"^(oo)^", "x":0, "y":0, "ativo": False } ]
    
    pontuacaoJogador = 0.0
    coefAng = 0
    intervalo = 5
    posicaoCanhao = LIMITE_VERT/2
    if (dif == 1): 
        numeroVidasJogador = 5
    elif (dif == 2): 
        numeroVidasJogador = 8
    elif (dif == 3):
        numeroVidasJogador = 10

    gotoxy(LIMITE/2 + 2,0)
    print('0')

    gotoxy (LIMITE/2 + 1, LIMITE_VERT - 3)
    print(numeroVidasJogador)

    while True: 
        if (randrange(15) % len(prqn) == 0 and intervalo < 0): #perguntar joabe
            intervalo = len(prqn) + randrange(10)
            j=0
            for porco in prqn:
                if (not porco["ativo"]):
                    porco["ativo"] = True
                    porco["x"] = 25 + randrange(70)
                    porco["y"] = 5 + randrange(15)
                    break
                j += 1

        j = 0
        for porco in prqn:
            # Apaga o porco
            gotoxy(porco["x"], porco["y"])
            print("       ", end='')
            
            if porco["ativo"]:
                    gotoxy(porco["x"], porco["y"])
                    print(porco["img"], end='') # ou print("@" + chr(ord('1')+j), end='')
            else:
                # Limpa exibição da trajetória
                print(' ' * 30, end='')
        
        #apagar o canhao
        gotoxy(1, posicaoCanhao+1)
        print('  ', end='', flush=True)
        gotoxy(2, posicaoCanhao+1)
        print('  ', end='', flush=True)
        gotoxy(3, posicaoCanhao+1)
        print('  ', end='', flush=True)
        gotoxy(4, posicaoCanhao+1)
        print('  ', end='', flush=True)
        gotoxy(1, posicaoCanhao)
        print('  ', end='', flush=True)
        gotoxy(2, posicaoCanhao)
        print('  ', end='', flush=True)
        gotoxy(3, posicaoCanhao)
        print('  ', end='', flush=True)
        gotoxy(1, posicaoCanhao-1)
        print('  ', end='', flush=True)
        gotoxy(2, posicaoCanhao-1)
        print('  ', end='', flush=True)
        gotoxy(3, posicaoCanhao-1)
        print('  ', end='', flush=True)
        gotoxy(4, posicaoCanhao-1)
        print('  ', end='', flush=True)

        if (kbhit()):
            c = hitKey()
            
            #texto do lado do canhao          
            # Atirar bala?
            if (ord(c) == ord(' ')): # tecla de espaço em branco usada para disparar
                for pssr in passaros:
                    if (not pssr["ativo"]):
                        pssr["ativo"] = True
                        pssr["x"] = 5
                        pssr["y"] = posicaoCanhao
                        pssr["traj"]["C"] = pssr["y"]
                        pssr["traj"]["A"] = 0.005 #(max(-15, 4 - pssr["traj"]["C"])) / ((LIMITE/2) * (LIMITE/2 - LIMITE))
                        pssr["traj"]["B"] = - coefAng
                        break
            elif (ord(c) == ord('q') or ord(c) == ord('Q')): #Professor, coloquei a variação do angulo pequena pra dar mais precisao pro tiro
                coefAng = (coefAng+1/50)                     #Mas é so apertar mais algumas vezes que a altura da parabola fica maior
                gotoxy(10, LIMITE_VERT - 3)
                print('                        ')
                gotoxy((10), LIMITE_VERT - 3)
                print('Angulo = {:0.2f}'.format(coefAng), flush=True)                
                if (coefAng > 60/50):
                    coefAng = 0 
                    gotoxy(10, LIMITE_VERT - 3)
                    print('                        ')
                    gotoxy(10, LIMITE_VERT - 3)
                    print('Angulo = {:0.2f}'.format(coefAng), flush=True)
            elif (ord(c) == ord('a') or ord(c) == ord('A')):
                coefAng = (coefAng-1/50)
                gotoxy(10, LIMITE_VERT - 3)
                print('                        ')
                gotoxy((10), LIMITE_VERT - 3)
                print('Angulo = {:0.2f}'.format(coefAng), flush=True)
                if (coefAng <= -36/50):
                    coefAng = 0
                    gotoxy(10, LIMITE_VERT - 3)
                    print('                        ')
                    gotoxy((10), LIMITE_VERT - 3)
                    print('Angulo = {:0.2f}'.format(coefAng), flush=True)
            elif (ord(c) == ord('w') or ord(c) == ord('W')):
                posicaoCanhao -= 1
                if (posicaoCanhao <= 2):
                    posicaoCanhao = LIMITE_VERT/2 #canhao nao passar dos limites da tela
            elif (ord(c) == ord('s') or ord(c) == ord('S')):
                posicaoCanhao += 1
                if (posicaoCanhao >= 24):
                    posicaoCanhao = LIMITE_VERT/2 #canhao nao passar dos limites da tela
        
        # apaga, move e desenha pssrs
        for pssr in passaros:
            gotoxy(pssr["x"], pssr["y"])
            print("    ", end='') #apagar o passaro
            if (pssr["ativo"]):

                pssr["x"] += 2    # Passaro se move para direita (aumenta x)
                pssr["y"] = int(solve2(pssr["traj"]["A"], pssr["traj"]["B"], pssr["traj"]["C"], pssr["x"]))

                if pssr["x"] >= LIMITE or pssr["y"]>=24 or pssr["y"]<=2:
                    pssr["ativo"] = False
                    numeroVidasJogador -= 1
                    gotoxy (LIMITE/2 + 1, LIMITE_VERT - 3)
                    print('{:0.1f}'.format(numeroVidasJogador))
                else: #printa o passaro varias vezes
                    gotoxy(pssr["x"], pssr["y"])
                    print(pssr["img"], end='') # ou print("@" + chr(ord('1')+j), end='')
            else:
                # Limpa exibição da trajetória
                print(' ' * 30, end='')

        # Desenha canhão:
        if (coefAng == 0):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng > 0 and coefAng < 10/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print("'", end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng >= 10/50 and coefAng <= 20/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print("'", end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng > 20/50 and coefAng <= 30/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print("'", end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print("'", end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng > 30/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print("-", end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print("-", end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print("/", end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng < 0 and coefAng >= -10/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print('\ ', end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng < -10/50 and coefAng >= -20/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print('\ ', end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng < -20/50 and coefAng >= -30/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('-', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print('\ ', end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print('\ ', end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)
        elif (coefAng < -30/50):
            gotoxy(1, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao+1)
            print('▄', end='', flush=True)
            gotoxy(1, posicaoCanhao)
            print('\ ', end='', flush=True)
            gotoxy(2, posicaoCanhao)
            print('\ ', end='', flush=True)
            gotoxy(3, posicaoCanhao)
            print('\ ', end='', flush=True)
            gotoxy(1, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(2, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(3, posicaoCanhao-1)
            print('▄', end='', flush=True)
            gotoxy(4, posicaoCanhao-1)
            print('▄', end='', flush=True)


        acertou = 0
        for porco in prqn:
            for pssr in passaros:
                if(pssr["ativo"] and porco["ativo"] and (pssr["x"] == porco["x"] or pssr["x"]+1 == porco["x"] or pssr["x"] == porco["x"]+1 or pssr["x"]+3 == porco["x"] or pssr["x"] == porco["x"]+3 or pssr["x"]+2 == porco["x"] or pssr["x"] == porco["x"]+2) and (pssr["y"] == porco["y"])):
                    acertou = True
                    pssr["ativo"] = False
                    porco["ativo"] = False
                    break

        if (acertou):
            pontuacaoJogador += PONTOS_ACERTO
            gotoxy(LIMITE/2 + 2,0)
            print('{:0.2f}'.format(pontuacaoJogador), end='')

        fimDoJogo = lambda : pontuacaoJogador >= 1000
        if (fimDoJogo()):
            gotoxy(35, LIMITE_VERT / 2)
            print("YOU WIN!")
            break
        
        gameOver = lambda : numeroVidasJogador == 0
        if (gameOver()):
            gotoxy(35, LIMITE_VERT / 2)
            print("GAME OVER!")
            break

        print(end='',flush=True)
        sleep(0.08)
        intervalo -= 1 #perguntar joabe

    pause()


            
