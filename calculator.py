x = int(raw_input("Unesite vrijednost prvog broja: "))
print x

y= int(raw_input("Unesite vrijednost drugog broja: "))

print y

operation = raw_input("Izaberite matematicku operaciju (+, -, *, /, %:)")
print operation

if operation== "+":
    print x + y
elif operation == "-":
    print x - y
elif operation== "*":
    print x * y
elif operation== "/":
    print x / y
elif operation== "%":
    print x % y

else:
    print("Niste izabrali pravu operaciju")

