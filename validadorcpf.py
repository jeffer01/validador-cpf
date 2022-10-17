''' 
    CPF contém 11 dígitos. Os 9 primeiros números são numeros base e os outros 2 são 
    dígitos verificados e esses digitos verificados validam se os números bases estão
    corretos, mas mesmo estando corretos, não garante que estejam cadastrados na
    Receita Federal.

'''
#   Validação do CPF
'''
    Número de CPF de exemplo para entender como funciona a validação:
    ~> 344858610-23
'''

#   Cálculo do primeiro dígito verificador
'''
    O primeiro dígito verificador é 2(posição 10) e o segundo é 3(posição 11)

    A primeira validação é multiplicar o primeiro dígito verificador por cada número
    base em separado começando com 10 e terminando com 2.
    Ex: 
    ~> 3    4   4   8   5    8   6   10  -   23
    3 x 10 = 30 / 4 x 9 = 36 / 4 x 8 = 32 / 8 x 7 = 56 / 5 x 6 = 30 / 8 x 5 = 40 / 6 x 4 = 24
    1 x 3 = 3 / 0 x 2 = 0

    Depois somamos todos os resultados:
    30 + 36 + 32 + 56 + 30 + 40 + 24 + 3 + 0 = 251

    Depois se divide o resultado por 11:
    251 / 11 = 22,81

    Agora pegamos o resto desta divisão:
    
    Resto = 251 - (11 * 22 ) = 9

    Regra 1: Se o resto for 1 ou 0, então o primeiro dígito verificador é igual a 0
    Regra 2: Se o resto for 2,4,5,6,7,8,9 ou 10 então o primeiro dígito verificador é a
    diferença(subtração) entre o número 11 e o resto da divisão por 11.

    No caso do primeiro dígito verificador, se aplica a regra 2.
    Primeiro digito verificador = 11 - 9 = 2

    Cálculo do segundo dígito verificador
    O mesmo processo se repete no segundo dígito verificador, começando com 11 e terminando
    com 2.
    ~> 3    4   4   8   5    8   6   10  -   23
    3 x 11 = 33 / 4 x 10 = 40 / 4 x 9  = 36 / 8 x 8 = 64 / 5 x 7 = 35 / 8 x 6 = 48 /
    6 x 5 = 30 / 1 x 4 = 4 / 0 x 3 = 0 / 2 x 2 = 4

    Faz se a soma dos resultados:
    33 + 40 + 36 + 64 + 35 + 48 + 30 + 4 + 0 + 4 = 294

    Depois se divide o resultado por 11:
    294 / 11 = 26

    Vamos pegar o resto da divisão
    Resto = 204 (11 * 26) = 8

    Regra 1: Se o resto for 1 ou 0, então o primeiro dígito verificador é igual a 0
    Regra 2: Se o resto for 2,4,5,6,7,8,9 ou 10 então o primeiro dígito verificador é a
    diferença(subtração) entre o número 11 e o resto da divisão por 11.
    No segundo dígito verificador também se aplica a segunda regra.
    Segundo dígito verificador:
    11 - 8 = 3

    O número do CPF tem mais um ponto. O último número base(localizado na posição 9), serve
    para marcar qual o estado de origem daquele cadastro.

    0 - Rio Grande do Sul / 1 - Distrito Federal, Goiás, Mato grosso, Mato Grosso do Sul,
    Tocantins / 2 - Amazonas, Pará, Roraima, Amapá, Acre e Rondônia / 3 - Ceará, Maranhão e
    Piauí / 4 - Paraiba, Pernambuco, Alagoas e Rio Grande do Norte / 5 - Bahia e Sergipe /
    6 - Minas Gerais / 7 - Rio de Janeiro e Espiríto Santo / 8 - São Paulo / 9 - Paraná e 
    Santa Cantarina

'''

#   Validador de CPF com Python
#CPF = input('Dígite seu CPF sem pontos e traços: ')

#   Função para validar CPF
def checaCPF(cpf):
    CPF = cpf   # Constante CPF que recebe o valor de parâmetro
    '''   
        A condição verifica se a variável constante CPF tem o tamanho diferente
        de 11(quantidade de números que um CPF tem) e se é apenas números e também
        verifica se a repetições de números nos números bases e números sequenciais.
        Se sim, a função retornará False e se encerrará.

        Obs: CPFs com números iguais como 111.111.111-11 e etc, podem
        ser validos pelo algoritmo, mas não existe registro oficial, 
        então não pode ser usado.
    '''
    if len(CPF) != 11 and CPF.isdigit() or CPF == "00000000000"\
    or CPF == "11111111111" or CPF == "22222222222" or CPF == "33333333333"\
    or CPF == "44444444444" or CPF == "55555555555" or CPF == "66666666666"\
    or CPF == "77777777777" or CPF == "88888888888" or CPF == "99999999999"\
    or CPF == "01234567890":
        return False
    '''
        Variável usada para somar os valores resultantes da multiplicação
        dos números bases pelos números de 10 até 2 no primeiro dígito verificador.
    '''
    soma = 0;

    '''
        Loop para fazer o calculo do número base(passado pelo argumento) 
        com o número sequencial(10 até 2) do primeiro dígito verificador.

        Ex: Valor associado ao índice 0
        soma = soma + 3 * (10 - 0) = 10 - 0 = 0 = 3 * 10 = 30 = soma(0) + 30
        soma = 30
        soma = soma + 4 * (10 - 1) = 10 - 1 = 9 = 4 * 9 = 36 = soma(30) + 36
        soma = 66
        ...
    '''
    for number in range(0,9):
        soma += int(CPF[number]) * (10 - number)
    '''
      A expressão abaixo verifica o resto entre soma e 11(Tamanho do CPF)
      e diminui com 11 novamente.
    '''
    resto = 11 - (soma % 11)
    '''
        Referente a primeira regra. Se o resto da divisão for 10 ou maior,
        o primeiro dígito verificador será 0 e isso também vale para o segundo
        dígito verificador.
    '''
    if resto == 10 or resto == 11:
        resto = 0
    
    #   Verifica se o resto da divisão é diferente do primeiro dígito verificador
    if resto != int(CPF[9]):
        return False
    soma = 0

    for number in range(0,10):
        soma += int(CPF[number]) * (11 - number)
    resto = 11 - (soma % 11)

    if resto == 10 or resto == 11:
        resto = 0
    #   Verifica se o resto da divisão é diferente do segundo dígito verificador
    if resto != int(CPF[10]):
        return False

    return True
    
print(checaCPF("34485861023"))
