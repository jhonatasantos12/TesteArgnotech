'''
1. Crie rotinas para conversão de temperaturas da escala Celsius (°C) para a escala
Fahrenheit (°F) e vice-versa, usando as seguintes fórmulas de conversão:
- De Celsius para Fahrenheit: subtraia 32, multiplique por 5 e divida por 9
- De Fahrenheit para Celsius: a conversão é feita pela função inversa da conversão
Celsius para Fahrenheit 
'''

def FahrenheitParaCelsius(temperatura):
    conversao = (temperatura-32)*5/9
    return conversao

def CelsiusParaFahrenheit(temperatura):
    conversao = (temperatura*9/5)+32
    return conversao
#Exemplo de chamada 
#Print(CelsiusParaFahrenheit(20))

'''
2. Crie uma rotina para a conversão de uma lista de temperaturas. Utilize a lista abaixo
como exemplo de argumento de entrada para a rotina. Para o último item da lista, crie a
rotina para a conversão da escala Kelvin para Celsius, usando a seguinte fórmula:
 De Kelvin para Celsius: subtraia 273,15 
'''

def FahrenheitParaKelvin(temperatura):
    conversao = ((temperatura-32)*5/9)+273.15
    return conversao

def CelsiusParaKelvin(temperatura):
    conversao = (temperatura+273.15)
    return conversao

def KelvinParaFahrenheit(temperatura):
    conversao = ((temperatura-273.15)*9/5)+32
    return conversao
    
def KelvinParaCelsius(temperatura):
    conversao = (temperatura-273.15)
    return conversao
graus =['C','F','K']
Lista =[]
def AdicionaLista(temp,O,D):
    O = O.upper()
    D = D.upper()
    if O  not in graus or D not in graus:
        return print('Por favor informe um grau valido ')

    json ={}
    json['Temperatura'] =temp
    json['Origem'] = O
    json['Destino'] = D
    Lista.append(json)

def AutoConversao(list):
    for x in list:
        if x['Origem'] == 'C':
            if x['Destino'] == 'F':
                x['Resultado']=CelsiusParaFahrenheit(x['Temperatura'])
            elif x['Destino'] =='K':
                x['Resultado']=CelsiusParaKelvin(x['Temperatura'])
        if x['Origem'] == 'F':
            if x['Destino'] == 'C':
                x['Resultado']=FahrenheitParaCelsius(x['Temperatura'])
            elif x['Destino'] =='K':
                x['Resultado']=FahrenheitParaKelvin(x['Temperatura'])
        if x['Origem'] =='K':
            if x['Destino'] =='C':
                x['Resultado']=KelvinParaCelsius(x['Temperatura'])
            elif x['Destino'] =='F':
                x['Resultado'] = KelvinParaFahrenheit(x['Temperatura'])
AdicionaLista(37,'F','C')
AdicionaLista(212,'F','C')
AdicionaLista(0,'C','F')
AdicionaLista(-40,'F','C')
AdicionaLista(0,'K','F')
AutoConversao(Lista)


'''
3. Assumindo um edifício com 10 andares e 4 apartamentos por andar, crie uma rotina
que apresente o número que deve ser colocado na porta de cada apartamento do edifício.
Considere que esta rotina também será utilizada em prédios com diferentes números de
andares e apartamentos por andar. 
'''

def apartamentos(n_andar,n_ap_andar):
    contandar =0 
    andar = 0
    ap = 0
    json={}
    while andar <n_andar:
        stringandar = str(andar+1)
        json[stringandar]= [] 
        andar +=1
        while contandar < n_ap_andar:
            ap +=1
            json[stringandar].append(ap)
            contandar+=1
        contandar = 0 
    return json
'''
4. Crie uma rotina que calcule a soma dos 100 primeiros elementos da séria de
Fibonacci (0, 1, 1, 2, 3, 5, 8, ...). 
'''
def sequenciafibonacci(limite):
    lista = []
    t1 = 0 
    t2 = 1
    x = 3 
    lista.append(t1)
    lista.append(t2)
    while x <= limite:
        t3 = t1 +t2 
        t1 = t2
        t2 = t3
        lista.append(t3)
        x +=1
    resultado = sum(lista)
    return resultado
'''
5. Elabore uma rotina que identifique quais os cartões listados abaixo foram emitidos pelas
bandeiras Kappa ou Gamma e estão expirados, assumindo que a data corrente é
23/11/2020.
'''
trilhas = []
def AdicionaTrilha(id,trilha):

    json ={}
    json['id'] = id
    json['trilha'] = trilha
    trilhas.append(json)
def definebanco(trilhas):
    for x in trilhas:
        if (x['trilha'][1] == '2'):
            x['banco'] = 'Kappa'
        elif (x['trilha'][1] == '7' and x['trilha'][2] == '2') or(x['trilha'][1] == '7' and x['trilha'][2] == '6'):
            x['banco'] = 'Gamma'
        else:
            x['banco']='Undefined'
AdicionaTrilha(1,';854922420655947=20087011490683843?')
AdicionaTrilha(2,';722792821249=190220153666234?')
AdicionaTrilha(3,';8657607910110=2209701507597562?')
AdicionaTrilha(4,';6034523459017=24032012187993726?')
AdicionaTrilha(5,';83407977524115=2010701164703842?')
AdicionaTrilha(6,';22554987787910=1903201221224791?')
AdicionaTrilha(7,';7621767951747=21112018460506111?')
AdicionaTrilha(8,';24478927568913=230470179307259?')
AdicionaTrilha(9,';88674481889649=19062014166695784?')
AdicionaTrilha(10,';76985229117350=1805701127970335? ')
AdicionaTrilha(11,';2147686439882=2712701977197697?')
AdicionaTrilha(12,';86392841965929=2108201878359745?')
definebanco(trilhas)
def vencido(trilhas):
    expirados =[]
    for x in trilhas:
        if x['banco'] =='Kappa' or x['banco'] =='Gamma':
            posicao = x['trilha'].index('=')
            anovencimento = int(x['trilha'][posicao+1] + x['trilha'][posicao+2])
            mesvencimento = int(x['trilha'][posicao+3] + x['trilha'][posicao+4])
            if (anovencimento < 20) or (anovencimento <=20 and mesvencimento<11):
                x['vencido'] = True
                expirados.append(x)
    return expirados