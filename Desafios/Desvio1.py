# PU - PREÇO UNITÁRIO | PO - PAÍS DE ORIGEM | MT - MEIO DE TRANSPORTE | CP - CARGA PERIGOSA
pu = int(input("Digite o preço unitário: "))
po = input("Digite o país de origem: (1-Brasil, 2-México,3-Outros) ")
mt = input("Digite o meio de transporte: (T-Terrestre, F-Fluvial, A-Aéreo) ")
cp = input("É carga perigosa? S/N ")

mt.upper()
cp.upper()

if pu > 0 and pu <=100:
    juros = 0.05
    pu = (pu*juros) + pu

else:
    juros = 0.2
    pu = (pu*juros) + pu

if cp == "S":
    if po == 1:
        vt = 21
    if po == 2:
        vt = 27
    if po == 3:
        vt = 50
elif cp == "N":
    if po == 1:
        vt = 21
    if po == 2:
        vt = 25
    if po == 3:
        vt = 40

if po == 2 and mt == "A":
    seguro = pu/2
else:
    pu = 0

pf = pu + juros + vt + seguro

print("Valor total: " + pf)