class Doente :
    def __init__(self, idade, sexo, tensao, colesterol, batimento, tem_doenca):
    self.idade = idade
    self.sexo = sexo
    self.tensao = tensao
    self.colesterol = colesterol
    self.batimento = batimento
    self.temDoenca = tem_doenca
    
    def __str__(self):
        return f"Idade: {self.idade}, Sexo: {self.sexo}, Tensao: {self.tensao}, Colesterol: {self.colesterol}, Batimento: {self.batimento}, Tem Doenca: {self.temDoenca}"
    
    def read (file):
        buffer_doentes=[]
        maior_idade=0
        maior_colestrol=0
        menor_colestrol=0

        with open (file, 'r') as f
            f.readline()
            for line in f:
            line=line.restrip().split(,)
            p=Doente=(int(line[0]), line[1], int (line[3]), int (line[4]), True if line[5]==1 else False) 
            buffer_doentes.append(p)
            if(p.idade>maior_idade):
                maior_idade= p.idade
            if (p.colestrol>maior_colestrol):
                maior_colestrol=p.colestrol
            if (p.colestrol < menor_colestrol):
                menor_colestrol=p.colestrol

        return buffer_doentes, maior_idade, maior_colestrol, menor_colestrol

#distribuição por sexos
    def dist_by_gender (buffer_doentes):
        buffer_doentes= list(filter (lambda x: x.temDoenca, buffer_doentes))
        total= len(buffer_doentes)
        masc, fem= 0,0
        masc, fem = list(filter(lambda x: x.sexo == 'M', buffer_doentes)), list(filter(lambda y: y.sexo == 'F', buffer_doentes))
        masc= len(masc)
        fem= len (fem)
        return {"Masculino": (float(masc)/total), "Feminino": float(fem)/total}

#distribuição por idades
    def dist_by_age (buffer_doentes, limite_idade):
        data = list(filter(lambda x: x.temDoenca, buffer_doentes))
        total_doenca = len(data)
        min_age = 30
        max_age = limite_idade
        age_array_size = 5
        age_ranges = {f"[{age}-{age + age_array_size - 1}]": 0.0 
                     for age in range(min_age, max_age + 1, age_array_size)}

    for person in buffer_doentes:
        for age_range in age_ranges.keys():
            start, end = map(int, age_range[1:-1].split('-'))
            if person.idade >= start and person.idade <= end:
                age_ranges[age_range] += 1
                break

    for age_range in age_ranges.keys():
        age_ranges[age_range] /= total_doenca
    return age_ranges

#distribuição por colesterol
    def dist_by_colesterol (buffer_doentes, limite_sup_colesterol, limite_inf_colesterol):
        data = list(filter(lambda x: x.temDoenca, buffer_doentes))
        totalDoenca = len(buffer_doentes)
        min = limite_inf_colesterol
        max = limite_sup_colesterol
        array_range_size = 11
        colesterol_ranges = {f"[{colesterol}-{colesterol + array_range_size - 1}]": 0.0 
                             for colesterol in range(min, max + 1, array_range_size)}

        for person in buffer_doentes:
            for colesterol_range in colesterol_ranges.keys():
                start, end = map(int, colesterol_range[1:-1].split('-'))
                if person.colesterol >= start and person.colesterol <= end:
                    colesterol_ranges[colesterol_range] += 1
                    break

        for colesterol_range in colesterol_ranges.keys():
            colesterol_ranges[colesterol_range] /= totalDoenca
        return colesterol_ranges

    def get_tabela(distribuicao):
        res = ""
        for key, value in distribuicao.items():
            res += f"{key: ^20} | {(value * 100): ^20}\n"
        return res

    def main():
    buffer_doentes, limite_idade, limite_sup_colesterol, limite_inf_colesterol = read_file('myheart.csv')
    distribuicoes = {1: dist_by_gender(buffer_doentes), 2: dist_by_age (buffer_doentes, limite_idade), 3: dist_by_colesterol (buffer_doentes, limite_sup_colesterol, limite_inf_colesterol)}
    escolha = 1
    while escolha != 0:
        escolha = int(input("Qual distribuicao deseja visualizar: \n1 - Sexo\n2 - Idade\n3 - Colesterol\n0- Sair: "))
        if escolha != 0:
            distribuicao = distribuicoes[escolha]
            print(get_tabela(distribuicao))

if __name__ == "__main__":
    main()




