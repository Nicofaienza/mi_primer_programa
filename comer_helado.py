apetece_helado_input = input("Te apetece un helado? (Si/No) ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("No me dijiste ninguna de las dos opciones, voy a tomarlo como un NO")
    apetece_helado = False


tiene_dinero_input = input("Tiene dinero para un helado? (Si/No) ").upper()

if tiene_dinero_input == "SI":
    tiene_dinero = True
elif tiene_dinero_input == "NO":
    tiene_dinero = False
else:
    print("No me dijiste ninguna de las dos opciones, voy a tomarlo como un NO")
    tiene_dinero = False


senor_de_de_los_helados_input = input("Esta el hobre de los helados? (Si/No) ").upper()

if senor_de_de_los_helados_input == "SI":
    senor_de_de_los_helados = True
elif senor_de_de_los_helados_input == "NO":
    senor_de_de_los_helados = False
else:
    print("No me dijiste ninguna de las dos opciones, voy a tomarlo como un NO")
    senor_de_de_los_helados = False

esta_tu_tia_input = input("Esta tu tia? (Si/No) ").upper()

if esta_tu_tia_input == "SI":
    esta_tu_tia = True
elif esta_tu_tia_input == "NO":
    esta_tu_tia = False
else:
    print("No me dijiste ninguna de las dos opciones, voy a tomarlo como un NO")
    esta_tu_tia = False


if tiene_dinero == True or esta_tu_tia == True:
    puede_permitirselo = True
else:
    puede_permitirselo = False


if apetece_helado and puede_permitirselo and senor_de_de_los_helados:
    print("Pues, comete un helado")
else:
    print("Pues nada")

