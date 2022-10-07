lista_parcelas = []
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', "novembro", "dezembro"]
emprestimo = None
quant_parcelas = None

salario = float(input("Informe o seu salário:"))
maximo_liberado = (35 * salario) / 100 * 12
print("O valor maximo liberado para empréstimo é de:", maximo_liberado)
score = int(input("Informe o seu Score:"))

if score <= 300:
    print("Score muito baixo para solicitar um empréstimo:")
elif score > 1000:
    print("Valor do score inválido.")

else:
    while emprestimo is None or emprestimo > maximo_liberado:
        emprestimo = float(input("Informe o valor do empréstimo:"))
        if emprestimo > maximo_liberado:
            print("Valor para empréstimo negado, seu limite é de:", maximo_liberado)



    while quant_parcelas is None or quant_parcelas > 12:
        quant_parcelas = int(input("Informe para quantas vezes deseja dividir o empréstimo:"))
        if quant_parcelas > 12:
            print("Desculpe mas o limite de parcelas é de até 12 meses, por favor escolha outra quantidade.")


    if quant_parcelas < 12:
        print("Informe em qual mês irá começar a pagar as parcelas:")
        print("1-JAN||2-FEV||3-MAR||4-ABR||5-MAI||6-JUN||7-JUL||8-AGO||9-SET||10-OUT||11-NOV||12-DEZ")
        primeiro_mes = int(input(""))
    else:
        primeiro_mes = 1
     
    def retirarMeses():
        quant_meses = 0
        for i in lista_meses:
            quant_meses += 1
        while quant_parcelas < quant_meses:
            lista_meses.pop()
            quant_meses -=1

    if primeiro_mes == 1:
        retirarMeses()
    else:    
        for x in range(primeiro_mes - 1):
            lista_meses.pop(x)
        retirarMeses()

    parcelas = emprestimo / quant_parcelas
    if score <= 600:
        juros_a_m = (6.57 * parcelas) / 100
    elif score <= 1000:
        juros_a_m = (2.69 * parcelas) / 100

    while quant_parcelas > 0:
        parcelas = parcelas + juros_a_m
        lista_parcelas.append(parcelas)

        quant_parcelas -=1

print("=" * 50)

num = 1
for a, b in zip(lista_meses, lista_parcelas):
    print(f'A {num}ª parcela será paga em {a}, no valor de {"%.2f" % b}.')
    num +=1
