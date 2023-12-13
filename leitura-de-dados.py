# maiores temperaturas
temperaturasMensais = []

# meses
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mesesInseridos = set()

# entrada de dados para cada mês
for i in range(12):
    numMes = int(input(f'Insira o número do mês [1;12]: '))
    # Verifica se o mês já foi inserido
    if numMes < 1 or numMes > 12 or numMes in mesesInseridos:
      numMes = int(input('Valor inválido ou mês já inserido. Digite novamente.'))
    mesesInseridos.add(numMes)

    # substituir ',' por '.' na entrada da temperatura
    temperaturaStr = input(f'Digite a temperatura máxima do mês {meses[numMes-1]}: ').replace(',', '.')

    # converter a string para um número float
    temperatura = float(temperaturaStr)
    if temperatura < -60 or temperatura > 50:
        temperatura = float(input('Temperatura inválida. Digite novamente: '))
    temperaturasMensais.append(temperatura)

# cálculo média máxima anual
mediaMaxima = sum(temperaturasMensais) / 12
print(f'A temperatura média máxima anual é: {mediaMaxima:.2f}°C')

# meses escaldantes, quantidade de meses com registro maior que 38 graus
mesesEscaldantes = [meses[i] for i in range(12) if temperaturasMensais[i] > 38]
qtdeMesesEscaldantes = sum(1 for temperatura in temperaturasMensais if temperatura > 38)
print('Quantidade de meses com temperatura maior que 38 graus:', qtdeMesesEscaldantes)

# mês mais escaldante do ano, escrito por extenso
mesMaisEscaldante = meses[0]
temperaturaMaisEscaldante = temperaturasMensais[0]

for i in range(12):
    if temperaturasMensais[i] > temperaturaMaisEscaldante:
        mesMaisEscaldante = meses[i]
        temperaturaMaisEscaldante = temperaturasMensais[i]

print(f'O mês mais escaldante do ano é: {mesMaisEscaldante}')

# mês menos quente do ano, escrito por extenso
mesMenosQuente = meses[0]
temperaturaMenosQuente = temperaturasMensais[0]

for i in range(12):
    if temperaturasMensais[i] < temperaturaMenosQuente:
        mesMenosQuente = meses[i]
        temperaturaMenosQuente = temperaturasMensais[i]

print(f'O mês menos quente do ano é: {mesMenosQuente}')