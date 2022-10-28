from matplotlib import pyplot as plt
def sum(tall1,tall2):
    result = tall1+tall2
    return result
def subtraksjon(tall1, tall2):
    result = tall1-tall2
    return result
def multiplikasjon(tall1, tall2):
    result = tall1*tall2
    return result
def divisjon(tall1, tall2):
    result = tall1/tall2
    return result
renta = []
tb = []
avdrag = []
kjøpesum = int(input('please insert price'))
egenk =int(input('insert egen kapital'))
nedbetalingstid =int(input('insert years'))
ønsket_bel = int(input('insert ønsket beløp'))
n_renta = float(input('insert renta'))
i = 0
for i in range(nedbetalingstid) : 
    årlig_avdrag = ønsket_bel/nedbetalingstid
    årlig_renta = (ønsket_bel * n_renta)/100 

    avdrag.append(årlig_avdrag)
    renta.append(årlig_renta)
for q in range(nedbetalingstid):
    result = sum(avdrag[q], renta[q])
    tb.append(result)
print("renta")
for s in range(nedbetalingstid):
    print(s)
    print(renta[s])
print(renta)
print("avdrag")
print(avdrag)
print("årlig terminbeløp")
print(tb)
