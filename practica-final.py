#paso 1
tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

#paso 2

tipo_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD): ")

#paso 3
monto_conversion = float(input("Ingrese el monto a convertir: "))
#paso 4
if tipo_conversion.upper() == "EUR":
    resultado = monto_conversion*tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es: ", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_conversion*tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es: ", resultado)
else:
    print("No está disponible este tipo de conversión actualmente")



