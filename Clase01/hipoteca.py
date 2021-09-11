# hipoteca.py
# Ejercicio de hipoteca

#David solicitó un crédito a 30 años para comprar una vivienda, con una tasa
#fija nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo
#de $2684,11.
#¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando
#en el sexto año de la hipoteca (es decir, luego de 5 años)?
#Modificá tu programa de forma que la información sobre pagos extras sea
#incorporada de manera versátil. Agregá las siguientes variables antes del
#ciclo, para definir el comienzo, fin y monto de los pagos extras.
#Modicá tu programa para que imprima una tabla mostrando el mes, el total pagado
#hasta el momento y el saldo restante.
#Ya que estamos, corregí el código anterior de forma que el pago del último mes
#se ajuste a lo adeudado.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    mes += 1
    saldo = saldo * (1+tasa/12)
    if saldo < pago_mensual:
        pago_mensual = saldo
    else:
        pass
    saldo -= pago_mensual
    total_pagado = total_pagado + pago_mensual
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo -= pago_extra
        total_pagado += pago_extra
    else:
        pass
    print(f"{mes:3d}   {total_pagado:6.2f}   {saldo:6.2f}")

print(f"Total pagado {total_pagado:6.2f} meses requeridos: {mes}")
