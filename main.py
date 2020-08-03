board = [' 'for x in range(10)] # preenchendo o quadro com 9 espaços em branco
 #basicamente o board esta assim: [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

#coloca o X na posição escolhida
def insertLetter(letra,pos):
    board[pos] = letra

#função para saber se o espaço está livre  
def spaceIsFree(pos):
    return board[pos] == ' ' #condição booleana

#construindo o quadro da velha
def printBoard(board):

    print('---------------------------------')
    
    print('   |   |')
    print(' ' + board[1]+' | ' + board[2] +' | '+ board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4]+' | ' + board[5] +' | '+ board[6])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[7]+' | ' + board[8] +' | '+ board[9])

    print('---------------------------------')

#função retorna true checando se jogador ganhou
def isWinner(bo, le): #variaveis: board e letter
    return (bo[7]== le and bo[8]==le and bo[9] == le) or (bo[4]== le and
    bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3] == le) or (bo[1]==le
    and bo[4]==le and bo[7] == le) or (bo[2]==le and bo[5]==le and bo[8] == le) or (bo[3]==le 
    and bo[6]==le and bo[9] == le) or (bo[1]==le and 
    bo[5]==le and bo[9] == le) or (bo[3]==le and bo[5]==le and bo[7] == le)


#jogador faz a jogada
def playerMove():
    run = True
    while run: #looping até entrar um dado válido
        move = input("Digite uma posição para colocar o X (1-9): ")
        #validação de dados
        try:
            move = int(move) #tem que ser um int!
            if move>0 and move<10: #numero tem que ser entre 1 e 9!
                if spaceIsFree(move):
                    run=False
                    insertLetter('X', move) #coloca o X
                else:
                    print('Este espaço ja esta ocupado!')
            else :
                print('Entre com um número válido!')
        #caso não entre com um valor int
        except:
            print('Entre com um número!')
#jogada do computador
#função analisa o board e escolhe a melhor jogada
def compMove():
    movimentosPossiveis = [x for x, letter in enumerate(board) if letter == ' ' and x!=0 ] #checa todas as posições possiveis
    move = 0

    #procurando movimento que leva a vitória ou que impede a vitória do oponente
    for let in ['O','X']:
        for i in movimentosPossiveis:
            boardCopia = board[:] #cria uma copia do board
            boardCopia[i] = let #passa a letra para a posicao escolhida
            if isWinner(boardCopia,let): #chaca a função para ver se é vencedor
                move = i #caso for verdadeira, ele move para essa posição
                return move #isso também faz com que o computador bloqueie uma possível vitória
    
    #caso não tenha nenhum "movimento vencedor" seleciona algum canto(pos = 1,3,7,9) de forma random
    cantoLivre = []
    for i in movimentosPossiveis:
        if i in [1,3,7,9]:
            cantoLivre.append(i) #caso o canto esteja vazio, é adicionado na string cantoAberto
    if len(cantoLivre)>1:
        move = selectRandom(cantoLivre)
        return move
    
    #caso os cantos estejam tomados, o computador tenta selecionar o centro(pos = 5)
    if 5 in movimentosPossiveis:
        move = 5 #posição 5 = centro do board
        return move

    #caso o centro esteja tomado, computador tenta em alguma posição nas bordas(pos = 2,4,6,8): 
    #mesma lógica do cantoLivre
    bordaLivre = []
    for i in movimentosPossiveis:
        if i in [2,4,6,8]:
            bordaLivre.append(i)
    if len (bordaLivre)>1:
        move = selectRandom(bordaLivre)

    return move

#função para gerar numeros aleatorios
def selectRandom(li):
    import random
    ln = len(li)#pegando o tamanho da lista
    r = random.randrange(0,ln)#pega um numero aleatório entre zero e o tamanho da lista
    return li[r]


#para ver se o quaro está cheio não pode haver nenhum espaço ' ' vazio
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    board = [' 'for x in range(10)] # preenchendo o quadro com 9 espaços em branco
 #basicamente o board esta assim: [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    print('Bem Vindo ao jogo da velha!')
    printBoard(board) #printando o quadro

    while not(isBoardFull(board)):
        #checando pra ver se o computador ganhou
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Computador Venceu!")
        
        #checando pra ver se o jogador ganhou
        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                 print("Deu Velha!")
            else:
                insertLetter('O', move)
                print('Computador ecolheu a posição: ', move,':')
                printBoard(board)
            printBoard(board)
        else:
            print("Parabéns, você venceu!")

    if isBoardFull(board):
        print("Velha!")

#looping para dar restart no jogo    
    while True:
        resposta = input("Quer continuar jogando?(s/n)")
        if(resposta.lower() == 's' or resposta.lower() == 'sim'):
            board = [' 'for x in range(10)] #cria um board branco
            print('------------------------------------------')
            main()
        else:
            break


main()