import datetime, random, math, time
while True:
    print('-=-'*21)
    print('MENU:')
    print('  [1] parabens')
    print('  [2] jogo da adivinhação')
    print('  [3] calcular o imc')
    print('  [4] calcular ano bissexto')
    print('  [5] calculadora')
    print('  [6] PythonHelp')
    print('  [7] Sair')
    print('-=-'*21)
    f = int(input('qual você escolhe? '))
    if (f == 1):
        nome = input('digite seu nome: ')
        d1 = -1
        while d1 < 10:
            d1 += 1
            print(d1)
            time.sleep(1)
        print('parabens {}!!!'.format(nome))
        break
    elif(f == 2):
        computador = random.randint(0, 10)
        print('-=-' * 20)
        print('vou pensar em um número até 10...')
        print('-=-' * 20)
        jogador = int(input('que número eu pensei? '))
        while jogador != computador:
            jogador = int(input('tente novamente: '))
        if jogador == computador:
            print('acertou eu pensei no número {}'.format(computador))
        break
    elif(f == 3):
        altura = float(input('qual e a sua altura? '))
        peso = float(input('qual o seu peso? '))
        imc = ( peso ) / ( altura ** 2 )
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
    elif(f == 4):
        ano = int(input('que ano você quer analisar?, para analisar o ano atual digite 0: '))
        if (ano == 0):
            ano = datetime.date.today().year
        if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
            print('o ano {} é bissexto'.format(ano))
        else:
            print('o ano {} não é bissexto'.format(ano))
        break
    elif(f == 5):
        sinal = int(input( 'para somar digite 1, para subtrair digite 2, para dividir digite 3, para multiplicar digite 4,  para fazer uma raiz quadrada digite 5, potencia digite 6: '))
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
    elif (f == 6):
        def ajuda(com):
            help(com)


        def titulo(MSG):
            tam = len(MSG) + 4
            print('~' * tam)
            print(MSG)
            print('~' * tam)


        comando = ''
        while True:
            titulo('   Ajuda Python')
            comando = str(input('digite a biblioteca ou função que  quer ver > '))
            if comando.upper() == 'FIM':
                break
            else:
                ajuda(comando)
        titulo('   Ate mais')
        break
    elif (f == 7):
        break
    else:
        print(' ')
        print(' ')
        print('-#' * 18 + '-')
        print('     Selecione um valor valido')
        print('-#' * 18 + '-')
        print(' ')
        print(' ')
print(' ')
print(' ')
print('-#' *8 + '-')
print('    Até mais')
print('-#' *8 + '-')
