total = 0 
while True:
    entrada = raw_input('+ ')
    if not entrada.strip(): break
    try:
        parcela = float(entrada)
    except ValueError:
        print 'digite um numero ou nada para encerrar'
    else:    
        total += parcela
print '---------'
print total
