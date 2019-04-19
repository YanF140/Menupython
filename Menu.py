# Importa as bibliotecas necessárias
import datetime, random, math, time

# Gera um laço para quando um valor invalido for colocado ele reinicia
while True:

    # Mostra o menu
    print('-=-' * 21)
    print('MENU:')
    print('  [1] parabens')
    print('  [2] jogo da adivinhação')
    print('  [3] calcular o imc')
    print('  [4] calcular ano bissexto')
    print('  [5] calculadora')
    print('  [6] PythonHelp')
    print('  [7] Sair')
    print('-=-' * 21)

    # Pergunta o que ele escolhe
    f = int(input('qual você escolhe? '))

    # Verifica se ele escolheu o valor 1
    if (f == 1):
        nome = input('digite seu nome: ')
        d1 = -1
        while d1 < 10:
            d1 += 1
            print(d1)
            time.sleep(1)
        print('parabens {}!!!'.format(nome))
        break

    # Verifica se ele escolheu o valor 2
    elif (f == 2):

        # Randomiza um número de 1 a 10
        computador = random.randint(0, 10)
        Jogadas = 0
        print('-=-' * 20)
        print('vou pensar em um número até 10...')
        print('-=-' * 20)

        # Pergunta para o jogador qual valor ele acha
        jogador = int(input('que número eu pensei? '))

        if jogador > computador:
            print('Chute um valor mais baixo')
        elif jogador < computador:
            print('Chute um valor mais alto')
                
        # Verifica se o jogador venceu
        while jogador != computador:
            Jogadas += 1
            jogador = int(input('tente novamente: '))
            if jogador > computador:
                print('Chute um valor mais baixo')
            elif jogador < computador:
                print('Chute um valor mais alto')
            if jogador == computador:
                print('acertou eu pensei no número {}, você acertou em {} tentativas'.format(computador, Jogadas))
                break

    # Verifica se ele escolheu o valor 3
    elif (f == 3):

        # pergunta a altura e o peso do usuário
        altura = float(input('qual e a sua altura? '))
        peso = float(input('qual o seu peso? '))

        # Calcula o IMC do usuário
        imc = (peso) / (altura ** 2)

        # mostra a pesagem ideial de acordo com o IMC do usuário
        if (imc < 18.5):
            print('você esta abaixo do peso')
        elif (imc <= 24.9):
            print('você esta no seu peso ideal')
        elif (imc <= 29.9):
            print('você esta com sobrepeso')
        elif (imc <= 34.9):
            print('você esta com obesidade de primeiro grau')
        elif (imc <= 39.9):
            print('você esta com obesidade de segundo grau')
        elif (imc >= 40):
            print('você esta com obesidade morbida')
        break

    # Verifica se ele escolheu o valor 4
    elif (f == 4):

        # pergunta o ano que ele escolhe
        ano = int(input('que ano você quer analisar?, para analisar o ano atual digite 0: '))

        # se ele escolher o valor 0 ele analisa o ano atual do computador
        if (ano == 0):
            ano = datetime.date.today().year
        if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
            print('o ano {} é bissexto'.format(ano))

        # se não ele analisa o ano colocado
        else:
            print('o ano {} não é bissexto'.format(ano))
        break

    # Verifica se ele escolheu o valor 5
    elif (f == 5):

        # pergunta qual sera a operação feita
        sinal = int(input(
            'para somar digite 1, para subtrair digite 2, para dividir digite 3, para multiplicar digite 4,  para fazer uma raiz quadrada digite 5, potencia digite 6: '))

        # faz as verificações necessarias
        if (sinal == 1):
            valor1 = float(input('digite o primeiro valor: '))
            valor2 = float(input('digite o segundo valor: '))
            resultado = (valor1 + valor2)
            print('o resultado é {}'.format(resultado))
        elif (sinal == 2):
            valor1 = float(input('digite o primeiro valor: '))
            valor2 = float(input('digite o segundo valor: '))
            resultado = (valor1 - valor2)
            print('o resultado é {}'.format(resultado))
        elif (sinal == 3):
            valor1 = float(input('digite o primeiro valor: '))
            valor2 = float(input('digite o segundo valor: '))
            resultado = (valor1 / valor2)
            print('o resultado é  {}'.format(resultado))
        elif (sinal == 4):
            valor1 = float(input('digite o primeiro valor: '))
            valor2 = float(input('digite o segundo valor: '))
            resultado = (valor1 * valor2)
            print('o resultado é  {}'.format(resultado))
        elif (sinal == 5):
            raiz = float(input('digite o valor da raiz: '))
            resultado = math.sqrt(raiz)
            print('o resultado dessa raiz e {}'.format(resultado))
        elif (sinal == 6):
            valor1 = float(input('digite o primeiro valor: '))
            valor2 = float(input('digite o segundo valor: '))
            resultado = valor1 ** valor2
            print('o resultado dessa potencia é  {}'.format(resultado))
        break

    # verifica se ele escolheu o valor 6
    elif (f == 6):

        # cria a função de ajuda
        def ajuda(com):
            help(com)


        # cria a função de uma mensagem na tela
        def titulo(MSG):
            tam = len(MSG) + 4
            print('~' * tam)
            print(MSG)
            print('~' * tam)


        # cria a variavel do comando
        comando = ''

        # Cria o laço de repetição para funcionaro o flag
        while True:

            # modifica a função de mensagem
            titulo('   Ajuda Python')

            # modifica a variavel do comando
            comando = str(input('digite a biblioteca ou função que  quer ver > '))

            # verifica se o comando se flag foi acionado
            if comando.upper() == 'FIM':
                break

            # se nao mostra a função do comando
            else:
                ajuda(comando)

        # mostra a despedida
        titulo('   Ate mais')
        break

    # verifica se o valor 7 foi escolhido
    elif (f == 7):

        # para o programa
        break

    # verifica se um valor invalido foi adicionado
    else:

        # mostra uma mensagem para ele escolher um valor valido
        print(' ')
        print(' ')
        print('-#' * 18 + '-')
        print('     Selecione um valor valido')
        print('-#' * 18 + '-')
        print(' ')
        print(' ')

# mostra a despedida
print(' ')
print(' ')
print('-#' * 8 + '-')
print('    Até mais')
print('-#' * 8 + '-')
