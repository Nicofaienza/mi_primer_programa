
pokemon_elegido = input("Contra qué pokémon quieres combatir? (Squirtle / Charmander / Bulbasaur) ").upper()

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = 0

if pokemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    ataque_enemigo = 8
elif pokemon_elegido == "BULBASAUR":
   vida_enemigo = 100
   ataque_enemigo = 10
elif pokemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    ataque_enemigo = 7

print("Elegiste luchar contra {}, su vida es de {} y posee un ataque de {}pts de dano".format(pokemon_elegido, vida_enemigo, ataque_enemigo))
print("Que comience el combate, tu empiezas!")

onda_voltio = 10
chispazo = 12

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque deseas usar? (Onda voltio(10pts) / Chispazo(12pts)): ").upper()
    if ataque_elegido == "ONDA VOLTIO":
        vida_enemigo -= onda_voltio
        print("Atacaste a {} con {}pts de dano, la vida de tu enemigo ahora es {}".format(pokemon_elegido, onda_voltio, vida_enemigo))
    elif ataque_elegido == "CHISPAZO":
        vida_enemigo -= chispazo
        print("Atacaste a {} con {}pts de dano, la vida de tu enemigo ahora es {}".format(pokemon_elegido, chispazo, vida_enemigo))


    vida_pikachu -= ataque_enemigo
    print("{} te ha atacado con 10pts de dano, la vida de tu PIKACHU ahora es de {} ".format(pokemon_elegido, vida_pikachu))

if vida_enemigo <= 0:
    print("Has ganado el combate, {} no puede continuar".format(pokemon_elegido))
elif vida_pikachu <= 0:
    print("Has perdido el combate, PIKACHU ya no puede continuar")


print("Combate terminado")