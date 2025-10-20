import os, time

# Criando uma matriz 3x3 que será o tabuleiro.
tabuleiro = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]
# Criando variavéis de jogadores globais.
jogador1= ""
jogador2= ""

# Função que exibirá o tabuleiro.
def mostrar_tabuleiro():
    # Definindo indicador para contagem de linhas e colunas.
    indicador = 0
    print("coluna:  0 1 2")

    # Percorrendo linhas da matriz.
    for linha in tabuleiro: 
        print(f"linha: {indicador}", end= " ")

        # Percorrendo e exibindo cada elemento de linha.
        for elemento in linha:
            print(elemento, end= " ")

        # Adicionando valor para indicar o index de cada linha percorrida.
        indicador+=1
        print()

# Função que verifica se houve um vencedor e quem seria.
def verificar_vencedor():

    # Verifica se houve 3 valores iguais em cada linha que sejam diferentes de _.
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != "_":
            return linha[0]
    
    # Verifica se houve 3 valores iguais em cada coluna que sejam diferentes de _.
    for contador in range(3):
        if tabuleiro[0][contador]== tabuleiro[1][contador]== tabuleiro[2][contador] != "_":
            return tabuleiro[0[contador]]
    
    # Verifica se houve 3 valores iguais da esquerda pra direita que sejam diferentes de _.
    if tabuleiro[0][0]== tabuleiro[1][1]== tabuleiro[2][2] != "_":
        return tabuleiro[0][0]
    

    # Verifica se houve 3 valores iguais da direita para a esquerda que sejam diferentes de _.
    if tabuleiro[2][2]== tabuleiro[1][1]== tabuleiro[0][0] != "_":
        return tabuleiro[2][2]
    
    # Se nenhum dos valores acimas forem verdadeiros, retorna falso.
    return False

# Função que verifica que houve empante. 
def verificar_empate():

    # Verifica se existe algum elemento na matriz igual a _. Se sim o tabuleiro ainda não está totalmente preenchido.
    for linha in tabuleiro:
        for elemento in linha:
            if elemento == "_":
                return False

    # Se não tiver nenhum valor _, então o jogo empatou.
    return True

# Função que verifica se a jogada está valida de acordo com a dimensão da matriz.
def verificar_jogada_valida(jogada_col, jogada_lin, jogador):

    # Utilizando "try" para captar valores válidos.
    try:
        # Verificando se o index da matriz já foi preenchido.
        if tabuleiro[jogada_lin][jogada_col] != "_":
            print(f"O jogador {tabuleiro[jogada_lin][jogada_col]} já jogou nessa posição.")
            
            # Se o index já foi preenchido retorna falso.
            return False
       
        # Quando o valor do index é válido, o selecionado pelo jogador será preenchido.
        tabuleiro[jogada_lin][jogada_col] = jogador
        return True
    
    # Se o jogador tiver informado um caractere não númerico ou fora da dimensão da matriz.
    except Exception as e:
        print(f"Jogada inválida. Jogador {jogador} tente novamente.")
        
        #Se o valor for desconhecido, informa ao jogador e retorna falso.  
        return False 
    
# Função que controla o funcionamento do jogo.
def loop_principal():

    # Variavel para controlar o jogador atual. Na primeira rodada será o jogador 1.
    jogador_atual = jogador1
    print()

    # Informando aos jogadores seus "peões" e aguardando 5s para o jogo iniciar.
    print(f'Você é o Jogador 1 e escolheu {jogador1}. O seu adversário é o Jogador 2 e escolheu {jogador2}\n O seu jogo já vai iniciar')
    time.sleep(5)

    #  Definido que enquanto verdadeiro, o jogo irá continuar.
    while True:

        #  Limpa o terminal para manter organização.
        os.system('cls')
        
        # Informa a vez do atual jogador e mostra o estado do tabuleiro.
        print(f"Vez do jogador {jogador_atual}")
        print()
        mostrar_tabuleiro()
        print()

        #  Define que a resposta do jogador precisa ser um número inteiro.
        try:
            jogada_col= int(input("Escolha a coluna de destino: "))
            jogada_lin= int(input("Escolha a linha de destino: "))

        #  Se não for um número inteiro retorna ao início do while para o jogador inserir um número válido.
        except Exception as e:
            time.sleep(2)
            print("Digite uma coluna e linha válida. (0, 1 ou 2)")
            continue
    
        # Chama a função que verifica se a jogada foi válida.
        jogadada_valida = verificar_jogada_valida(jogada_col, jogada_lin, jogador_atual)

        # Se ela não for válida, retorna ao início do while para o jogador inserir um valor válido. 
        if jogadada_valida == False:
            continue
        
        # Faz a lógica para definir o próximo jogador.
        else:
            if jogador_atual == "X": 
                jogador_atual = "O"
            else:
                jogador_atual = "X"


        # Valida se houve um vencedor na jogada atual.
        vencedor= verificar_vencedor()
        if vencedor != False:
            print()
            print(10*"~-",f'Parabéns {vencedor}, você venceu!',10*"~-")
           
            # Encerra o jogo atual.  
            break

        #  Verifica se houve empate na jogada atual.
        empate= verificar_empate()
        if empate == True:
            mostrar_tabuleiro()
            print()
            print(10*"~-","Jogo empatado. Nenhum vencedor.",10*"~-")
          
            # Encerra o jogo atual.
            break

# Código principal para iniciar a jogatina.
while True:

    # Limpa o terminal e dá boas vindas aos jogadores.
    os.system('cls')
    print()
    print(10*"~-", "BEM VINDO AO JOGO DA VELHA DO CLAUDIO ALVES", 10*"~-")
    print()
    time.sleep(0.5)
    
    #  identifica o primeiro jogador.
    jogador1 = input("Escolha X ou O: ").upper()

    # Valida se o jogador escolheu um peão válido e define o peão adversário.
    if jogador1 == "X" or jogador1 == 'O':
        if jogador1 == "X": 
            jogador2 = "O"
        else:
            jogador2 = "X"
   
    # Caso o jogador não tiver escolhido um peão válido, ele será informado e o jogo será reiniciado.
    else:
        print("Opção invalida. Escolha X ou O")
        time.sleep(2)
        os.system('cls')
        continue

    # Se os valores forem válidos o loop principal irá se iniciar.
    loop_principal()

    print()
    
    #  Após o loop principal se encerrar o jogador poderá escolher se deseja jogar novamente.
    continuar = input("Deseja iniciar um novo jogo? \nDigite S para SIM e N para NÃO: ").upper()

    # Caso os jogadores desejarem, o tabuleiro será reiniciado, assim como o jogo.
    if continuar == 'S':
        tabuleiro = [["_", "_", "_"],
                    ["_", "_", "_"],
                    ["_", "_", "_"]]
        continue

    # Caso não queiram, o jogo será encerrado.
    else:
        break