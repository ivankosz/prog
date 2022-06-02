def impuesto(importe, iva=21):
    print(f"Total a pagar: {importe + importe*(iva/100)}")

pago=float(input("Importe: "))
iva=input("Iva: ")

if iva=="":
    impuesto(pago)
else:
    impuesto(pago, float(iva))