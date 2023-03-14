string = input("Somador ON/OFF:\n")

string = string.rstrip().split(' ')

soma=0
on=0

for element in string:
    if element == "ON" or element == "on":
        on = 1

    if element == "OFF" or element == "off":
        on = 0
        soma = 0

    if element.isnumeric() == True:
        if on == 1:
            soma = soma + int(element)

    if element == "=":
        if on == 1:
            print("Soma: %d" % soma)
            soma = 0
        else:
            print("Sem operações a realizar.")
