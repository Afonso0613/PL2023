import re;

def parsing():
    regex_string=r"(?P<numero_processo>\d+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>[\w\s]+)::(?P<pai>[\w\s]+)?::(?P<mae>[\w\s]+)?::(?P<obs>.*)?::"

    r1=re.compile(regex_string)

    processDirectory=[]

    file= open ('processos.txt', 'r')
    for linha in file.readlines():
        match=r1.match(linha)
        if match:
            processDirectory.append(match.groupdict())
    return processDirectory



def processoAnos(processDirectory):
    freq={} #Guardar frequencia de processos aqui
    for processo in processDirectory:
        ano= processo['data'] [:4] #Pegar no campo específico da data, neste caso ano
        if ano not in freq:
            freq[ano]=0 #Inicializar caso seja primeira ocorrência. Iniciar a 0 pois irá sempre incrementar 1 
        freq[ano]+=1 
    return freq

def nomesPorSec(processDirectory):
    reg_PrimeiroNome=r"(\w+)\s"
    reg_UltimoNome=r"[\w\s]+\s(\w+)"

    r1=re.compile(reg_PrimeiroNome)
    r2=re.compile(reg_UltimoNome)

    seculos={}

    for processo in processDirectory:
        seculo=0
        ano= processo['data'] [:4]
        if ano<1000:
            seculo=1
        else:
            seculo=(ano//100)+1
        if seculo not in seculos:
            seculos[seculo]=0
        nome= processo['nome']
        if nome is not None:
            primeiroNome= r1.match(nome).group(1)
            ultimoNome= r2.match(nome).group(1)
            if primeiroNome not in seculos[seculo]:
                seculos[seculo][primeiroNome]=0
            if ultimoNome not in seculos[seculo]:
                seculos[seculo][ultimoNome]=0
            seculos[seculo][primeiroNome]+=1
            seculos[seculo][ultimoNome]+=1
    return seculos

def getGrau(obs):
    graus={"Irmao", "Tio", "Sobrinho", "Primo", "Irmaos", "Pai", "Filho", "Sobrinhos", "Avo", "Neto", "Filhos", "Primos", "Bisavo"}

    reg = r"\w+,(?P<grau>\w+)"
    r = re.compile(reg)

    grau= r.findall(obs)
    grau=list(filter(lambda x: x in graus, grau))

    return grau

def tiposRelacao(processDirectory):
        relacao={}

        for processo in processDirectory:
            observacoes=processo['obs']
            graus_processo= getGrau(observacoes)
            for grau in graus_processo:
                if grau not in relacao:
                    relacao[grau]=0
                relacao[grau]+=1
        return relacao

def processoJson(processo):
    res="{\n"
    for campo in processo:
        if campo is not None:
            r+=f"\t\"{campo}\": \"{processo[campo]}\",\n"
    return res + "}\n"

def jsonConvert (out, processDirectory):
    res="[\n"
    for processo in processDirectory:
        res+= processoJson(processo)
    res+="]\n"

    with open(out,"w") as file:
        file.write(res)




def main():

    processDirectory= parsing()

    frequencias_ano= list(processoAnos(processDirectory).items())
    frequencias_ano.sort(key=lambda x:x[0])

    frequencias_nome= list(nomesPorSec(processDirectory).items())
    frequencias_nome.sort(key=lambda x: x[1], reverse=True)

    frequencias_graus = list(tiposRelacao(processDirectory).items())
    frequencias_graus.sort(key=lambda x: x[1], reverse=True)

    option= input("-----Menu-----\n1. Calcular a frequência de processos por ano\n2. Top 5 de frequência de nomes próprios e apelidos por séculos\n3. Calcular frequência dos diferentes tipos de relação\n4. Converter os 20 primeiros registos num novo ficheiro de output em formato Json")
    
    match option:
        case "1":
            for (ano, value) in frequencias_ano:
                print(f"{ano}: {value}")
        case "2":
            for (seculo, frequencias) in frequencias_nome:
                print(f"Seculo {seculo}")
                frequencias = list(frequencias.items())
                frequencias.sort(key=lambda x: x[1], reverse=True)
                for frequencia in frequencias[:5]:
                    print(f"\t{frequencia[0]}: {frequencia[1]}")

        case "3":
                for (grau, value) in frequencias_graus:
                    print(f"{grau}: {value}")
        case "4":
                file = input("Nome do ficheiro: ")
                jsonConvert(file, processDirectory[:20])
