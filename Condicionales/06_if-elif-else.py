sueldo= 1000000
gasto= 900000

if sueldo>100000:
    print("Ganás bien.")
    if gasto>sueldo:
        print("Pero estás en déficit.")
    elif gasto >= sueldo//3*2:
        print("Pero estás gastando mucho.")        
elif sueldo>50000:
    print("Ganás poco.")
else:
    print("Sos pobre.")