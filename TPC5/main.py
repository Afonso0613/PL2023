import re

#Definir as expressões que vão dar match com os inputs

op1=re.compile(r'LEVANTAR')
op2=re.compile(r'POUSAR')
op3=re.compile(r'MOEDA ([0-9]+(c|e))+')
op4_1=re.compile(r'T=00[0-9]{9}')
op4_2=re.compile(r'T=(601|604)[0-9]{6}')
op4_3=re.compile(r'T=2[0-9]{8}')
op4_4=re.compile(r'T=800[0-9]{6}')
op4_5=re.compile(r'T=808[0-9]{6}')
op5=re.compile(r'ABORTAR')

#Biblioteca das possíveis moedas que se podem introduzir
moedas={'5c', '10c', '20c', '50c', '1e', '2e'}

#Função que valida uma lista de moedas inseridas e calcula o seu valor total
def validar_moedas (lista_moedas):
    euro=0
    cent=0
    for element in lista_moedas:
        if element not in moedas:
            print(str(element)+ 'nao e uma moeda valida. ')
    else:
        if 'c' in element:
            aux=element.strip('c')
            cent+= int(aux)
        
        if 'e' in element:
            aux=element.strip('e')
            euro+= int(aux)
    ##print('O saldo e ' +str(euro)+'e'+str(cent)+'c')
    return euro,cent
    
def comparar_montante (euro,cent,euro1, cent1):
    result=True
    if euro<euro1:
        result= False
    if euro==euro1:
        if cent<cent1:
            result=False
    return result

def calcula_troco (euro, cent, euro1,cent1):
    if euro==euro1:
        return 0,cent-cent1
    if euro>euro1:
        if cent>=cent1:
            return euro-euro1, cent-cent1
        else:
            return euro-(euro1+1), cent+(1-cent1)


def deal_inputs (entrada):
    exit=1
    e=0
    c=0
    trc=0,0
    montante=0,0
    levantou=0

    while exit !=0:

        if re.fullmatch(op1, entrada):
            levantou=1
            entrada=input('Introduza moedas')

        elif re.fullmatch(op2, entrada):
            if levantou==1:
                print('troco= '+str(e)+'e'+str(c)+'c; Volte Sempre!')
                exit=0
            else:
                entrada=input('Pegue primeiro no Telefone!')

        elif re.fullmatch(op3,entrada):
            if levantou==1:
                res_1 = re.sub('MOEDA ', '', entrada)
                res_2 = re.sub('\.','',res_1)
                res_3= re.sub ('\,','',res_2)
                lista_moedas= res_3.spli(' ')
                montante=validar_moedas(lista_moedas)
                e+=montante[0]
                c+=montante[1]
                entrada=input('saldo= ' +str(e)+'e'+str(c)+'c ')
            else:
                entrada=input('Pegue primeiro no Telefone!')
                

        elif re.fullmatch(op4_1, entrada):
            entrada= input('Numero invalido, introduza outro' )

        if re.fullmatch(op4_2, entrada):
            if comparar_montante(e,c,1,50):
                trc= calcula_troco(e,c,1,50)
                e=trc[0]
                c=trc[1]
                entrada=input('saldo= ' +str(e)+'e'+str(c)+'c ')
            else:
                entrada= input('nao tem saldo suficiente, insira mais')

        if re.fullmatch(op4_3, entrada):
            if comparar_montante(e,c,0,25):
                trc= calcula_troco(e,c,0,25)
                e=trc[0]
                c=trc[1]
                entrada=input('saldo= ' +str(e)+'e'+str(c)+'c ')
            else:
                entrada= input('nao tem saldo suficiente, insira mais')
        
        if re.fullmatch(op4_4, entrada):
            if comparar_montante(e,c,0,0):
                trc= calcula_troco(e,c,0,0)
                e=trc[0]
                c=trc[1]
                entrada=input('saldo= ' +str(e)+'e'+str(c)+'c ')

        if re.fullmatch(op4_5, entrada):
            if comparar_montante(e,c,0,10):
                trc= calcula_troco(e,c,0,10)
                e=trc[0]
                c=trc[1]
                entrada=input('saldo= ' +str(e)+'e'+str(c)+'c ')
            else:
                entrada= input('nao tem saldo suficiente, insira mais')

        if re.fullmatch(op5, entrada):  
            print=('Operacao abortada. Dinheiro devolvido ') 
            exit=0
             


        




                


