import re
import json
import numpy

#abrir o ficheiro
ficheiro= input("Qual o nome do ficheiro?\n")

file=open (ficheiro)
data=file.readlines()

header=data[0]
conteudo= data[1::]

#padroes para expressões regulares
padrao_header=r"Número,Nome,Curso(,?Notas?(?P<Notas>{\d,\d})?(?:::)?(?P<agregator>\w*)?(?:.*))?"

padrao_conteudo=r"(?P<Número>\d*),(?P<Nome>.*[^\W\d_]),(?P<curso>.*[^\W\d_]),?(?P<Notas>[\d,]*)?\n?"

headerP= re.compile(padrao_header)
conteudoP= re.compile(padrao_conteudo)

#possiveis padroes do header
match=re.search(headerP,header)
limite=(0,0)
temAgregado= False
if match:
    info_h=match.groupdict()
    temAgregado= True if info_h.get('agregator') else False

    if info_h ['Notas'] is not None:
        if ',' not in info_h['Notas']:
            limite = (int((info_h['Notas'])[1]),
                      int((info_h['Notas'])[1]))
        else:
            limite = (int((info_h['Notas'])[1]),
                      int((info_h['Notas'])[-2]))


data_dict=dict()
notas=[]
acumulado=0

for line in conteudo:
    match_c=re.fullmatch(conteudoP, line)

    if match_c:
        info_c=match_c.groupdict()
        notas = list(filter(str.strip, info_c['Notas'].split(',')))
        if limite[0] <= len(notas) <= limite[1]:
            if temAgregado:
                agregator_type = info_h['agregator']
                if agregator_type == 'sum':
                    for num in notas:
                        acumulado += int(num)
                    info_c['Notas'] = acumulado
                elif agregator_type == 'media':
                    tmp = []
                    for i, num in enumerate(notas):
                        tmp.append(int(num))
                info_c['Notas'] = numpy.average(tmp)

            data_dict[info_c['Número']] = info_c

try:
    output = list (data_dict.items())
    with open('alunos.json', 'w') as file:
        json.dump(output, file, indent=4)
    print('JSON file created sucessfully!')
except Exception as e:
    print(e)
