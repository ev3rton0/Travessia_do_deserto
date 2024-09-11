import random

print("TRAVESSIA DO DESERTO\n")
print("A = -> Consome uma unidade de água.\n    -> Reduz a sede pra zero.\n")
print("B = -> Avança uma pequena distância.\n    -> Aumenta a sede e o cansaço do camelo.\n    -> Os nativos também avançam.\n")
print("C = -> Avançar uma longa distância.\n    -> Aumenta significativamente a sede e o cansaço do camelo.\n    -> Os nativos também avançam.\n")
print("D = -> Parar para descansar.\n    -> Reduz o cansaço do camelo a zero\n    -> Os nativos se aproximam.\n")
print("E = -> Visualizar o status atual.\n    -> Verificar a distância percorrida.\n    -> Verificar sede.\n    -> Verificar Cansaço do camelo.\n    -> Verificar Distância dos nativos.\n    -> Verificar a quantidade de água restante.\n")
print("F = -> Desistir da travessia e o jogo termina.\n")


def beber_agua(agua_restante, sede):
    if agua_restante > 0:
        agua_restante -= 1
        sede = 0
        print(f"\n-> Você bebeu água!"
            f"\n-> Sua sede = {sede}\n")
    else:
        print(f"\n-> Seu abastecimento de água é = {agua_restante}\n")

    return agua_restante, sede

def avancar_curta_distancia(distancia_jogador, sede, cansaco_camelo, distancia_nativos):
    distancia_percorrida = random.randint(5, 12) #gera um numero aleatorio da distancia percorrida.
    distancia_jogador += distancia_percorrida #incrementa esse valor aleatorio ao distancia_jogador que inicialmente começa em 0.
    sede += 1 #incrementa 1 na sede que começa em 0.
    cansaco_camelo += 1
    distancia_nativos += random.randint(7, 14)
    
    print(f"\n-> Você avançou {distancia_percorrida} unidades.\n")
    return distancia_jogador, sede, cansaco_camelo, distancia_nativos

def avancar_longa_distancia(distancia_jogador, sede, cansaco_camelo, distancia_nativos):
    distancia_percorrida = random.randint(10, 20)
    distancia_jogador += distancia_percorrida
    sede += 2
    cansaco_camelo += 2
    distancia_nativos += random.randint(7, 14)
    
    print(f"-> Você avançou {distancia_percorrida} unidades.\n")
    return distancia_jogador, sede, cansaco_camelo, distancia_nativos

def jogador_descansar(cansaco_camelo, distancia_nativos):
    cansaco_camelo=0
    distancia_nativos += random.randint(7, 14)

    print(f"\n-> O cansaço do camelo é = {cansaco_camelo}\n")
    return cansaco_camelo,distancia_nativos

def verificar_status(distancia_jogador, sede, cansaco_camelo, distancia_nativos, agua_restante):
    print("\n-------------STATUS-------------\n"
          f"-> Distancia percorrida = {distancia_jogador}\n"
          f"-> Sede = {sede}\n"
          f"-> Cansaço do camelo = {cansaco_camelo}\n"
          f"-> Distancia dos nativos = {distancia_nativos}\n"
          f"-> Água restante = {agua_restante}\n"
          )

def desistir():
    print(" -> Você desistiu da travessia. <-")
    return True

def main():
    fim_do_jogo = False
    distancia_jogador = 0
    distancia_nativos = -20  # Nativos começam 20 unidades atrás
    agua_restante = 5
    sede = 0
    cansaco_camelo = 0
    # Constantes
    limite_sede = 6
    limite_cansaco = 8
    limite_distancia = 200
    while not fim_do_jogo:
        choice_user = input("Digite a ação desejada (A,B,C,D,E,F): ").upper()

        if choice_user == 'A':
            agua_restante, sede = beber_agua(agua_restante, sede)
        elif choice_user == 'B':
            distancia_jogador, sede, cansaco_camelo, distancia_nativos =  avancar_curta_distancia(distancia_jogador, sede, cansaco_camelo, distancia_nativos)
        elif choice_user == 'C':
            distancia_jogador, sede, cansaco_camelo, distancia_nativos = avancar_longa_distancia(distancia_jogador, sede, cansaco_camelo, distancia_nativos)
        elif choice_user == 'D':
            cansaco_camelo, distancia_nativos = jogador_descansar(cansaco_camelo, distancia_nativos)
        elif choice_user == 'E':
            verificar_status(distancia_jogador, sede, cansaco_camelo, distancia_nativos, agua_restante)
            #distancia_jogador, sede, cansaco_camelo, distancia_nativos, agua_restante)
        elif choice_user == 'F':
            fim_de_jogo = desistir()
            if fim_de_jogo: break


        if sede >= limite_sede:
            print('-> Morreu de sede X-X')
            fim_de_jogo = True
        elif cansaco_camelo >= limite_cansaco:
            print("Seu camelo morreu de exaustão.")
            fim_de_jogo = True
        elif distancia_nativos >= distancia_jogador:
            print("Os nativos te alcançaram!")
            fim_de_jogo = True
        elif distancia_jogador >= limite_distancia:
            print("Você chegou ao oásis e venceu o jogo!")
            fim_de_jogo = True  

main()
            
